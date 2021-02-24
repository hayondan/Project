import pymysql.cursors
import re

# Connect to the database
connection = pymysql.connect(host='remotemysql.com',
                             user='zKGM8cOKAS',
                             password='RCcSpmoiOO',
                             database='zKGM8cOKAS',
                             autocommit=True,
                             cursorclass=pymysql.cursors.DictCursor)


def backend(user_name):
    with connection.cursor() as cursor:
        sql = "SELECT user_id FROM zKGM8cOKAS.users WHERE user_name=%s"
        cursor.execute(sql, user_name)
        result = cursor.fetchall()
        return result


def post_user(user_id, user_name, creation_date):
    with connection.cursor() as cursor:
        # Create a new record
        sql = "INSERT INTO zKGM8cOKAS.users (user_id, user_name, creation_date) VALUES (%s, %s, %s)"
        cursor.execute(sql, (user_id, user_name, creation_date))
        result = cursor.fetchall()
        print('re = ', result)
        return result


def get_username(user_id):
    with connection.cursor() as cursor:
        sql = "SELECT user_name FROM zKGM8cOKAS.users WHERE user_id=%s"
        cursor.execute(sql, (user_id))
        username = cursor.fetchall()
        print("\ntest_db | get_username | username = ",username)
        return username



def checkIfUserIdExists(user_id):
        with connection.cursor() as cursor:
            sql= "SELECT user_id FROM users WHERE user_id=%s"
            cursor.execute(sql,(user_id))
            userid = cursor.fetchall() # if Tuple is not tmpty
            if userid:
                return True
            else:
                return False



def user_update(user_id,user_name):
    with connection.cursor() as cursor:
        insert_name = "UPDATE users SET user_name=%s WHERE user_id =%s"
        cursor.execute(insert_name, (user_name, user_id))
        user_creationdate = cursor.fetchall()
    return user_creationdate



def delete_user_from_db(user_id):
    with connection.cursor() as cursor:
        sql = "DELETE from users WHERE user_id =%s"
        cursor.execute(sql, (user_id))
        user_deleted = cursor.fetchall()
        print("user_deleted ", user_deleted)
    return user_deleted