# proje rastgele instagram hesabi olusturmak icin hazirlanmistir.
# email_register projesi ile baglantilidir. 


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time 
# from email_register import *
from sourchs import name, username, password 


driver = webdriver.Chrome()

url = "https://www.instagram.com/accounts/emailsignup/"

driver.get(url)
time.sleep(3)

phoneOrEmail = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/section/main/div/div/div[1]/div/form/div[3]/div/label/input')
phoneOrEmail.send_keys("a")
name = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/section/main/div/div/div[1]/div/form/div[4]/div/label/input')
name.send_keys(name)
userName = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/section/main/div/div/div[1]/div/form/div[5]/div/label/input')
username.send_keys(username)
password = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/section/main/div/div/div[1]/div/form/div[6]/div/label/input')
password.send_keys(password)
time.sleep(2)
password.send_keys(Keys.ENTER)
time.sleep(5)

driver.close()

# xpathlerde sorun var duzelt.

# proje hala yapim asamasindadir.
# proje gelistirilecek ve bunlari tek fonksiyonla yapilabilir hale getirilecek.

