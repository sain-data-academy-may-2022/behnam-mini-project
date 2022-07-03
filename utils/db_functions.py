import pymysql.cursors
from pymysql.constants import CLIENT
import os
from dotenv import load_dotenv


load_dotenv()

host = os.environ.get("mysql_host")
user = os.environ.get("mysql_user")
password = os.environ.get("mysql_pass")
database = os.environ.get("mysql_db")


# Connect to the database
connection = pymysql.connect(
    host=host,
    user=user,
    password=password,
    database=database,
    client_flag=CLIENT.MULTI_STATEMENTS,
)

cursor = connection.cursor()


def read_from_db(query):
    cursor.execute(query)
    return cursor.fetchall()


def execute_on_db(query):
    cursor.execute(query)
    connection.commit()


def close_db_connections():
    cursor.close()
    connection.close()


def initialize_db(sql_file_path):
    with open(sql_file_path, "r") as f:
        query = f.read()
        execute_on_db(query)
