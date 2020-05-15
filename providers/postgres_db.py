import time
import psycopg2
import psycopg2.extras
from psycopg2.extensions import AsIs

from common.config import get_config


class MySqlDB:
    my_db = None

    def __init__(self):
        self.my_db = None

    def connect(self):
        db_config = get_config("db_provider_cloud")
        self.my_db = psycopg2.connect(
            host=db_config.get("db_host"),
            user=db_config.get("db_user"),
            passwd=db_config.get("db_password"),
            database=db_config.get("db_name")
        )

        return self.my_db

    @staticmethod
    def insert_from_dict(data, table, cursor, data_type=0):

        columns = list(data)
        if not columns:
            return None

        if data_type == 1 and columns:
            cols = ','.join(columns)
            values = f"%({columns[0]})s"
            for column in columns[1:]:
                values = values + f",%({column})s"
            insert_statement = f'insert into {table} ({cols}) values({values})'
        else:
            values = tuple([data[column] for column in columns])
            insert_statement = f'insert into {table}  (%s) values %s'
            insert_statement = cursor.mogrify(
                insert_statement, (AsIs(','.join(columns)), values)
            )

        return insert_statement

    @staticmethod
    def update_from_dict(data, cursor):
        sql_template = "({}) = %s"
        sql = sql_template.format(', '.join(data.keys()))
        params = (tuple(data.values()),)
        update_statement = cursor.mogrify(sql, params)
        return update_statement

    def insert_to_db(self, table, data, update_query=None):

        cursor = self.my_db.cursor()
        insert_sql = self.insert_from_dict(data, table, cursor)
        if update_query:
            insert_sql += bytes(update_query, 'utf-8') + \
                          self.update_from_dict(data, cursor)
        cursor.execute(insert_sql)
        self.my_db.commit()

    def insert_to_db_batch(self, table, data):

        if data:
            with self.my_db.cursor() as cursor:
                insert_sql = self.insert_from_dict(data[0], table, cursor,
                                                   data_type=1)
                if insert_sql:
                    iter_data = ({**val, } for val in data)
                    psycopg2.extras.execute_batch(cursor, insert_sql,
                                                  iter_data,
                                                  page_size=200)
                    self.my_db.commit()

    def get_dict_resultset(self, sql):

        psycopg2.extras.wait_select(self.my_db)
        cur = self.my_db.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cur.execute(sql)
        psycopg2.extras.wait_select(cur.connection)
        ans = cur.fetchall()
        dict_result = []
        for row in ans:
            dict_result.append(dict(row))
        return dict_result

    def execute_sql(self, sql):
        cur = self.my_db.cursor()
        cur.execute(sql)
        self.my_db.commit()
        return cur.statusmessage
