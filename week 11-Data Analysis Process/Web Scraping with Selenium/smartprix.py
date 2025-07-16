import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_object = Service(r"C:\Users\sumit\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe")

# sent your serive object into chrome class
driver = webdriver.Chrome(service=service_object)

driver.get('https://www.smartprix.com/mobiles')

time.sleep(200)
# now click on exlcude out of the stocks 
exculde_button = driver.find_element(
    by= By.XPATH,
    value='//*[@id="app"]/main/aside/div/div[5]/div[2]/label[1]/input'
)
exculde_button.click()
time.sleep(2)

upcoming_button = driver.find_element(
    by=By.XPATH,
    value='//*[@id="app"]/main/aside/div/div[5]/div[2]/label[2]/input'
)
upcoming_button.click()
time.sleep(2)

driver.find_element(
    by= By.XPATH,
    value='//*[@id="app"]/main/div[1]/div[3]/div[3]'
)
time.sleep(100)
#//*[@id="app"]/main/aside/div/div[5]/div[2]/label[1]/input
#//*[@id="app"]/main/aside/div/div[5]/div[2]/label[2]/input