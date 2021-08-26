# proje rastgele emailler olusturulmak icin hazirlanistir.
# instagram_register projesi icin olusturulmustur.


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from sourchs import password , email
import time 


driver = webdriver.Chrome()

url = "https://signup.live.com/signup?wa=wsignin1.0&rpsnv=13&ct=1626181493&rver=7.0.6737.0&wp=MBI_SSL&wreply=https%3a%2f%2foutlook.live.com%2fowa%2f%3fnlp%3d1%26RpsCsrfState%3d7e288bbe-9653-1a3e-3c9d-d1332c75da4a&id=292841&aadredir=1&CBCXT=out&lw=1&fl=dob%2cflname%2cwld&cobrandid=90015&contextid=C846EEB648B4B8DB&bk=1629806775&uiflavor=web&lic=1&mkt=TR-TR&lc=1055&uaid=bc995a4ec0564d209740e656af0eab7e"

driver.get(url)


time.sleep(2)
emailInput = driver.find_element_by_xpath('//*[@id="MemberName"]')
emailInput.send_keys(email)
forHotmail = driver.find_element_by_xpath('//*[@id="LiveDomainBoxList"]')
forHotmail.send_keys("h")
forHotmail.send_keys(Keys.ENTER)
time.sleep(2)
emailInput.send_keys(Keys.ENTER)
time.sleep(2)
passwordInput = driver.find_element_by_xpath('//*[@id="PasswordInput"]')
passwordInput.send_keys(password)
time.sleep(2)
passwordInput.send_keys(Keys.ENTER)
time.sleep(2)
firstName = driver.find_element_by_xpath('//*[@id="FirstName"]')
firstName.send_keys(email) 
secondName = driver.find_element_by_xpath('//*[@id="LastName"]')             
secondName.send_keys(email)
time.sleep(2)
secondName.send_keys(Keys.ENTER)
time.sleep(2)

driver.close()

# proje hala yapim asamasindadir.
#secenek secme arastiriliyor. sonuclandiginda proje guncellenecektir.

