from selenium import webdriver

from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException






driver = webdriver.Firefox(executable_path="/home/hector/testing/geckodriver")
driver.get("http://facebook.com")


username = driver.find_element_by_id("email")
password = driver.find_element_by_id("pass")
submit = driver.find_element_by_id( "loginbutton" )


username.send_keys("hector_chidori@hotmail.com")
password.send_keys("Alwaysmestizo22!")
submit.click()


wait = driver.implicitly_wait(5)

if driver.current_url == 'https://www.facebook.com/?sk=welcome':
    print("Login correcto")

else:
    print("Error")



