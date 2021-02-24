import requests, db_connector
from numpy import random
from selenium import webdriver


try:
    x = random.randint(100)
    print(x)
    res_post = requests.post('http://127.0.0.1:5001/users/' + str(x), json={"user_name":"new_user_testing"})
    res_get = requests.get('http://127.0.0.1:5001/users/' + str(x))
    result = db_connector.get_username(x)
    print(result)
    driver = webdriver.Chrome(executable_path="C:/Users/hayon/OneDrive/שולחן העבודה/ChromeDriver.exe")
    driver.get('http://127.0.0.1:5001/users/get_user_data/' + str(x))
except:
    if res_post.status_code and res_get.status_code == 500:
        raise Exception('Error')