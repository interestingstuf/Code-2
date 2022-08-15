

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
PATH="/Users/parthamradkar/Desktop/chromedriver"
driver=webdriver.Chrome(PATH)
driver.get("https://youtube.com")
print(driver.title)
search=driver.find_element("s")
#search.send_keys("test")
#search.send_keys(Keys.RETURN)
time.sleep(5)
driver.quit()