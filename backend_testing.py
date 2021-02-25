import requests
import db_connector

try:
    res = requests.post('http://127.0.0.1:5000/users/27', json={"user_name":"daniel_1"})
    if res.status_code == 500:
        raise Exception('Error')
    else:
        print(res)
        res_1 = requests.get('http://127.0.0.1:5000/users/27')
        print(res_1)
except:
    print('user_already_exist')


result_from_db = db_connector.backend('daniel_1')
print(result_from_db)
user_id = result_from_db[0]['user_id']
if user_id == 27:
    print('good')
else:
    print('not good')
