import db_connector
from flask import Flask, request
app = Flask(__name__)
from dateutil.parser import parse
from datetime import datetime
import os
import signal


app.route('stop_server')


def stop_server():
    os.kill(os.getpid().signal.CTRAL_C_EVENT)
    return 'Server stopped'


def isDate(string, fuzzy=False):
    try:
        parse(string, fuzzy=fuzzy)
        return True
    except ValueError:
        return False

def Check_creation_date_format(creatin_date):
    try:
        if bool(datetime.datetime.strptime(creatin_date, "%Y-%m-%d %H:%M:%S")):
            return True
        else:
            return False
    except:
        return False

@app.route('/users/get_user_data/<user_id>', methods=['GET'])
def existing_user2(user_id):
    try:
        username = db_connector.get_username(user_id)  # username if exits or None if  not exits
        if username:  # username is not none
            return "<h1 id='user'>" + username[0]['user_name'] + "</h1>"
        else:
            return "<H1 id='error'>"' no such user' + user_id + "</H1>"
    except:
        print("Error in DB - From GET")
        return {'status': 'error', 'reason': 'Error in DB_1'}, 500

# check existing user
@app.route('/users/<user_id>', methods=['GET'])
def existing_user(user_id):
    try:
        username = db_connector.get_username(user_id)  # username if exits or None if  not exits
        print("username = ",username)
        if username: # username is not none
            return {'status': 'ok', 'reason': username}, 200
        else:
            return {'status': 'error', 'user_name': 'no such id'}, 201
    except:
        print("Error in DB - From GET")
        return {'status': 'error', 'reason': 'Error in DB'}, 500


@app.route('/users/<user_id>', methods=['POST'])
def create_user(user_id):
    resultFromDb = db_connector.checkIfUserIdExists(user_id) # true or False
    if resultFromDb:
        return {'status': 'error', 'reason': 'id already exists'}, 500
    else:
        request_date = request.get_json()
        user_name = request_date.get('user_name')
        creation_date = request_date.get('creation_date') # body param

        if not Check_creation_date_format(creation_date): # is in worng format
            creation_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S") # create
        if user_name != None  and  type(user_name) == str:
            print("\nAll Params = ",user_id," | ",user_name, " | ",creation_date,"\n")

            user_added = db_connector.post_user(user_id, user_name, creation_date)
            print("\n app | create_user | user_added = ",user_added)
            if not user_added: # if user_added is empty so enterd to the if statement
                return {'status': 'ok', 'user_added': user_name}, 201
            else:
                return {'status': 'error', 'reason': 'Error in DB'}, 500
        else:
            return {'status': 'error', 'reason': 'Bad request- body parm error'}, 500






app.run(host='127.0.0.1', debug=True, port=5001)