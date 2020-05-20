import mysql.connector
from common.config import get_config
from datetime import datetime


def datetime_format(datestr, fr="%m/%d/%Y %H:%M:%S", to="%Y-%m-%d %H:%M:%S"):
    dt = datetime.strptime(datestr, fr)
    return datetime.strftime(dt, to)


class MySqlDB:
    my_db = None

    def __init__(self):
        self.my_db = None

    def connect(self):
        db_config = get_config("db_provider")
        self.my_db = mysql.connector.connect(
          host=db_config.get("db_host"),
          user=db_config.get("db_user"),
          passwd=db_config.get("db_password"),
          database=db_config.get("db_name")
        )

    # query the DB to get JSON data (dict)
    def query(self, sql, is_dict=True):
        my_cursor = self.my_db.cursor(dictionary=is_dict)
        my_cursor.execute(sql)
        my_result = my_cursor.fetchall()

        return my_result

    # insert into a DB  table
    def insert(self, sql, values):
        my_cursor = self.my_db.cursor()
        if isinstance(values, tuple):
            my_cursor.execute(sql, values)
        elif isinstance(values, list):
            my_cursor.executemany(sql, values)

        self.my_db.commit()
        return my_cursor.rowcount

    # other SQL commands like delete/Alter
    def query_commit(self, sql):
        my_cursor = self.my_db.cursor()
        my_cursor.execute(sql)
        self.my_db.commit()
        return my_cursor.rowcount
