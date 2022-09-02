import time #para el tiempo de espera
# import outlook
from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# driver = webdriver.Firefox()
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("http://localhost:8122")
elemento1 = driver.find_element(By.ID, "user")
elemento1.clear()
elemento1.send_keys("root")

elemento2 = driver.find_element(By.NAME, "pass")
elemento2.clear()
elemento2.send_keys("password")
driver.find_element(By.XPATH, "//input[contains(@type,'submit')]").click()
driver.get("http://localhost:8122")


elemento3 = driver.find_element(By.XPATH, "//input[@value='Create new ticket']")
elemento3.click()

elemento4 = driver.find_element(By.XPATH, "//input[@name='Subject']")
elemento4.send_keys("soy un ticket - Michel Sanchez")
time.sleep(5)

elemento5= driver.find_element(By.XPATH, "//input[@name='SubmitTicket']")
elemento5.click()
time.sleep(6)
driver.close()

