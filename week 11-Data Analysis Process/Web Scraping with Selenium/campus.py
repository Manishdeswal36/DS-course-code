# open google.com
# search campusx
# learnwith.campusx.in
# dsmp course page
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

options = Options()
options.binary_location = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"
options.add_argument('user-agent=Your Realistic User Agent Here')

s = Service(r"C:\Users\sumit\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe")
# driver = webdriver.Chrome(service=s, options=options) # For Brave
driver = webdriver.Chrome(service=s) # For Chrome

driver.get('http://google.com')
time.sleep(4)


# fetch the search input box using xpath

user_input = driver.find_element(
    by=By.XPATH,
    value='//*[@id="APjFqb"]'
    #value='/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input'
    )
user_input.send_keys('Campusx')
time.sleep(5)


user_input.send_keys(Keys.ENTER)
time.sleep(20)


link = driver.find_element(
    by= By.XPATH,
    #value= '//*[@id="rso"]/div[1]/div/div/div/div/div/div/div/div[1]/div/span/a'
    value='//*[@id="rso"]/div[1]/div/div/div/div/div/div/div/div[1]/div/span/a'
    #value = '/html/body/div[3]/div/div[11]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div/div/div[1]/div/span/a'
)
link.click()
time.sleep(230)

#input("Press Enter to close the browser...")  # Keeps window open until you press Enter
