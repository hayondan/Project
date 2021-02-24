from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:/Users/hayon/OneDrive/שולחן העבודה/ChromeDriver.exe")
driver.get("http://127.0.0.1:5001/users/get_user_data/1")
driver.maximize_window()
# element id="user"
element = driver.find_element_by_id("user")
element_text = element.text
if element:
    print(element_text)
else:
    print('not here')
    print('bla')


