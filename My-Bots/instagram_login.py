from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


username = input("username: ")
password = input("password: ")

driver = webdriver.Chrome()

url = 'https://www.instagram.com/accounts/login/'

driver.get(url)
time.sleep(2)
usernameInput = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
usernameInput.send_keys(username)
time.sleep(2)
passwordInput = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
passwordInput.send_keys(password)
time.sleep(2)
passwordInput.send_keys(Keys.ENTER)
time.sleep(10)

driver.close()


# proje hala yapim asamasindadir.
# proje gelistirilecek ve bunlari tek fonksiyonla yapilabilir hale getirilecek.