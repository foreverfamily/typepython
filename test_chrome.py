#!/usr/bin/python  
# -*- coding: utf-8 -*-  
from selenium import webdriver  
import time
import os
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

#driverOptions = webdriver.ChromeOptions()
#driverOptions.add_argument(r"user-data-dir=C:\\Users\\yulu\\AppData\\Local\\Google\\Chrome\\User Data")
#chromepath = os.path.abspath(r"C:\driver\chromedriver.exe")
#driver = webdriver.Chrome(chromepath)
driver = webdriver.Chrome()

first_url = 'https://shop.dianjia.io'
print("now access %s" %(first_url))
driver.get(first_url)
print("全屏显示")
driver.maximize_window()

second_url = 'https://pos.dianjia.io'
print("now access %s" %(second_url))
driver.get(second_url)
driver.refresh()

third_url = 'https://www.baidu.com'
print("now access %s" %(third_url))

print("back to %s" %(first_url))
driver.back()

print("forward to %s" %(first_url))
driver.forward()

brandId = driver.find_element_by_id("brandId")
brandId.send_keys("10010")
size = brandId.size
print(size)

driver.implicitly_wait(2)
username = driver.find_element_by_id("username")
username.send_keys("187671579777")
username.send_keys(Keys.BACK_SPACE)
username.send_keys(Keys.CONTROL, 'a')
username.send_keys(Keys.CONTROL, 'x')
username.send_keys(Keys.CONTROL, 'v')


search_text = driver.find_element_by_id("password")
search_text.send_keys("88888888")
#search_text.submit()
search_text.send_keys(Keys.ENTER)
driver.refresh()
#driver.quit()
time.sleep(2)
print(driver.title)
print(driver.current_url)

try:
    print(time.ctime())
    order_list_v = driver.find_element_by_class_name("order-list-v")
except NoSuchElementException as e:
    print e
finally:
    print time.ctime()
#定位有问题。。。
headers = driver.find_elements_by_xpath("//div[@id='root']/div[@class=dj-menu]/div[@class=dj-menu-header]")
for t in headers:
    print(driver.t.text)

driver.get(third_url)
above = driver.find_element_by_link_text("设置")
ActionChains(driver).move_to_element(above).perform()

driver.quit()