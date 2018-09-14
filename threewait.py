# -*- coding: utf-8 -*-
import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.get("http://test-yi007.weilian.cn")
driver.find_element_by_id("login-username").send_keys("sg0002")
driver.find_element_by_id("login-password").send_keys("123456")
driver.find_element_by_xpath("//button[@type='submit']").click()
WebDriverWait(driver, 10, 0.5).until(EC.presence_of_element_located((By.LINK_TEXT, u"基础设置")))
driver.find_element_by_link_text("基础设置").click()
WebDriverWait(driver, 10, 0.5).until(EC.presence_of_element_located((By.LINK_TEXT, u"组织机构")))
driver.find_element_by_link_text("组织机构").click()
time.sleep(3)
driver.quit()