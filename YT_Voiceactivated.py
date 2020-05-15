import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sample

sp= sample.VCtitle
driver = webdriver.Chrome ('C:/Users/Shubh/Downloads/chromedriver_win32/chromedriver')
driver.get('https://www.youtube.com/')
#driver.find_element_by_xpath("/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/div[2]/ytd-button-renderer/a/paper-button").click()
wait = WebDriverWait(driver, 3)
#driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input").send_keys("shubh1896@gmail.com")
#driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div").click()

#title = input('Enter title:')
title = str(sp)
driver.find_element_by_xpath("/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div/div[1]/input").send_keys(title)
driver.find_element_by_xpath("/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/button").click()
driver.get("https://www.youtube.com/results?search_query=" + str(title))
presence = EC.presence_of_element_located
visible = EC.visibility_of_element_located


wait.until(visible((By.ID, "video-title")))
driver.find_element_by_id("video-title").click()

#skipAd = driver.find_element_by_xpath(" /html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[4]/div[1]/div/div[1]/div/div/div/ytd-player/div/div/div[4]/div/div[3]/div/div[2]/span/button").click()

#def skipAdFunction():
    #threading.Timer(3,skipAdFunction).start()
    #if(skipAd.is_enabled() or skipAd.is_displayed()):
    #    skipAd.click()

#skipAdFunction()
