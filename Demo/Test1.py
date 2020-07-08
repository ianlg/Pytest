import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

url = "https://google.com"

driver = webdriver.Chrome("../Webdrivers/chromedriver.exe")

driver.set_page_load_timeout(20)

driver.get(url)
driver.maximize_window()
driver.find_element_by_name("q").send_keys("formula  1")
#driver.find_element_by_css_selector("button[jsname='Tg7LZd']").click()
time.sleep(2)
driver.find_element_by_id('hplogo').click()
driver.find_element_by_xpath("//body[@id='gsr']/div[@id='viewport']/div[@id='searchform']/form[@id='tsf']/div/div/div/center/input[1]").click()

time.sleep(2)


driver.close()
driver.quit()