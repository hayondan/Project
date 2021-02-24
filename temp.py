
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# 1+2
driver = webdriver.Chrome(executable_path="C:/Users/hayon/OneDrive/שולחן העבודה/ChromeDriver.exe")
driver.get("https://walla.co.il")
websitetitle_1 = driver.title
print(websitetitle_1)
driver.refresh()
print(websitetitle_1)
driver.quit()

driver = webdriver.Chrome(executable_path="C:/Users/hayon/OneDrive/שולחן העבודה/ChromeDriver.exe")
driver.get("https://ynet.co.il")
print(driver.current_url)
print(driver.title)
driver.quit()
# 3
yes
#4
driver = webdriver.Chrome(executable_path="C:/Users/hayon/OneDrive/שולחן העבודה/ChromeDriver.exe")
driver.get("https://translate.google.com")
driver.find_element_by_class_name("er8xn").send_keys("בלהבלהבלה")
print(driver.current_url)
print(driver.title)
# 5
driver = webdriver.Chrome(executable_path="C:/Users/hayon/OneDrive/שולחן העבודה/ChromeDriver.exe")
driver.get("https://www.youtube.com")
driver.find_element_by_name("search_query").send_keys("stairway to heaven")
driver.find_element_by_id("search-icon-legacy").click()
print(driver.current_url)
print(driver.title)
driver.close()
# 6
driver = webdriver.Chrome(executable_path="C:/Users/hayon/OneDrive/שולחן העבודה/ChromeDriver.exe")
driver.get("https://translate.google.com")
by_class_name = driver.find_element_by_class_name("er8xn")
print(by_class_name)
by_xpath = driver.find_element_by_xpath("/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[2]/c-wiz[1]/span/span/div/textarea")
print(by_class_name)
print(by_xpath)
print(driver.current_url)
print(driver.title)
driver.close()
# 7
driver = webdriver.Chrome(executable_path="C:/Users/hayon/OneDrive/שולחן העבודה/ChromeDriver.exe")
driver.get("https://www.facebook.com/")
driver.find_element_by_id("email").send_keys("******")
driver.find_element_by_id("pass").send_keys("******")
driver.implicitly_wait(10)
driver.find_element_by_id("u_0_b").send_keys(Keys.ENTER)
driver.close()
# 8
driver = webdriver.Chrome(executable_path="C:/Users/hayon/OneDrive/שולחן העבודה/ChromeDriver.exe")
driver.get("https://www.google.com/")
driver.delete_all_cookies()
driver.close()
# 9
# driver = webdriver.Chrome(executable_path="C:/Users/hayon/OneDrive/שולחן העבודה/ChromeDriver.exe")
# driver.get("https://github.com/")
# driver.maximize_window()
# driver.implicitly_wait(10)
# driver.find_element_by_class_name("form-control input-sm header-search-input jump-to-field js-jump-to-field js-site-search-focus").send_keys("Selenium")
# print(driver.current_url)
# print(driver.title)
# driver.close()