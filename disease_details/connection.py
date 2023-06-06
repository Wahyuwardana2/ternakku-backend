import pymysql


def create_connection():
    connection = pymysql.connect(
        host="34.101.184.157",
        user="root",
        password="root",
        db="ternakku",
        charset="utf8mb4",
        cursorclass=pymysql.cursors.DictCursor,
    )
    return connection