import pymysql
from config import host, user, password, database

if __name__ == '__main__':
    print(f"connecting to database '{database}'...")

    try:
        connection = pymysql.connect(
            host=host,
            database=database,
            user=user,
            password=password,
            cursorclass=pymysql.cursors.DictCursor
        )

        print('successfully connected.')
        print('=' * 20)

        try:
            # command functions & interpreter
            pass
        finally:
            connection.close()  # close connection
    except Exception as e:
        print(f'failed to connect: {e}')