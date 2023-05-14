from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import Keys

 # Получаем в переменную browser указатель на браузер
browser=webdriver.Chrome()

# Переходим на страницу, на которой находится форма для авторизации
browser.get('https://www.ozon.ru/')
search = browser.find_element(By.NAME, value="text")
time.sleep(2)
search.send_keys("одежда")
time.sleep(2)
search.send_keys(Keys. ENTER)
time.sleep(5)

browser.close()

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# from selenium.webdriver import Keys

#  # Получаем в переменную browser указатель на браузер
# browser=webdriver.Chrome()

# # Переходим на страницу, на которой находится форма для авторизации
# browser.get('https://www.ozon.ru/')
# button = browser.find_element(By.CLASS_NAME, value='c1w:nth-child(4) .c4w')
# time.sleep(5)
# button.click()
# time.sleep(5)
# browser.close()

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# from selenium.webdriver import Keys

#  # Получаем в переменную browser указатель на браузер
# browser=webdriver.Chrome()

# # Переходим на страницу, на которой находится форма для авторизации
# browser.get('https://www.ozon.ru/')
# button = browser.find_element(By.CLASS_NAME, value='dd9 .a2-e4')
# button.click()
# time.sleep(5)
# button = browser.find_element(By.CLASS_NAME, value='a9-a8')
# button.click()
# time.sleep(5)
# browser.close()