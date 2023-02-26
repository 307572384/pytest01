from selenium import webdriver
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
option = webdriver.ChromeOptions()
option.add_experimental_option("detach", True)
driver = webdriver.Chrome(chrome_options=option)
driver.get('file:///C:/Users/Administrator/Documents/tencent%20files/307572384/filerecv/table.html')
driver.find_element(By.XPATH,'/html/body/form/table/tbody/tr[2]/td[2]/input').send_keys("AK0087123")
time.sleep(2)
driver.find_element(By.XPATH,'/html/body/form/table/tbody/tr[3]/td[2]/input').send_keys('123456')
time.sleep(2)
driver.find_element(By.XPATH,'/html/body/form/table/tbody/tr[4]/td[2]/input').send_keys('123456')
time.sleep(2)
driver.find_element(By.XPATH,'/html/body/form/table/tbody/tr[5]/td[2]/input[1]').click()
time.sleep(2)
driver.find_element(By.XPATH,'/html/body/form/table/tbody/tr[6]/td[2]/input[1]').click()
time.sleep(2)
driver.find_element(By.XPATH,'/html/body/form/table/tbody/tr[7]/td[2]/select').click()
time.sleep(2)
driver.find_element(By.XPATH,'/html/body/form/table/tbody/tr[7]/td[2]/select/option[2]').click()
time.sleep(2)
driver.find_element(By.XPATH,'/html/body/form/table/tbody/tr[8]/th/input[2]').click()