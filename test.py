#Author: Imad Kalboneh
#Date created: June 25, 2017
#Last updated; January 10, 2019

import os
import time
import subprocess
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

site = 'textfree.us'

#make sure site can load
response = subprocess.Popen(["ping", site, "-n", '1'], stdout=subprocess.PIPE).stdout.read()

if response != -1: 
	#open up chrome window and load the site
	driver = webdriver.Chrome()
	driver.maximize_window()
	driver.get('https://www.' + site)
	delay = 3
	
	try:
		WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, 'username')))
	except TimeoutException:
		print('')

	#find parameter names and fill them
	username = driver.find_element_by_name('username')
	username.send_keys('wetextyou')
	
	password = driver.find_element_by_name('password')
	password.send_keys('cHSkM2iD1')

	driver.find_element_by_xpath("//*[@id='loginForm']/div[4]/button").click()
	time.sleep(3);
	
	#remove google prompt
	try:
		WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div/pmk-add-google-contacts-modal/div[1]/div")))
	except TimeoutException:
		print('')
	driver.find_element_by_xpath("/html/body/div[1]/div/div/pmk-add-google-contacts-modal/div[1]/div").click()
	
	#create new text
	driver.find_element_by_xpath("//*[@id='startNewConversationButton']").click()
	
	driver.find_element_by_id('contactInput').send_keys('6472428770\t\t')
	
	#read text file with 2 lines
	#line 1: user name
	#line 2: user phone number
	driver.find_element_by_xpath("//*[@id='messageForm']/div/div[2]/div[1]").send_keys('Thanks for registering at Demo1.com, ' + 'username!' + Keys.RETURN)
	
	time.sleep(5);
	
	driver.close()		
else:
	print('site not found')