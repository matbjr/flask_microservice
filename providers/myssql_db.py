import mysql.connector
from common.config import get_config


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

    def query(self, sql):
        my_cursor = self.my_db.cursor(dictionary=True)
        my_cursor.execute(sql)
        my_result = my_cursor.fetchall()

        return my_result

    def insert(self, sql, values):
        my_cursor = self.my_db.cursor()
        if isinstance(values, tuple):
            my_cursor.execute(sql, values)
        elif isinstance(values, list):
            my_cursor.executemany(sql, values)

        self.my_db.commit()
        return my_cursor.rowcount

    def query_commit(self, sql):
        my_cursor = self.my_db.cursor()
        my_cursor.execute(sql)
        self.my_db.commit()
        return my_cursor.rowcount
