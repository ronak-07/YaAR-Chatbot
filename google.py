from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys
from time import sleep
if sys.argv[-1] == "1":
	url = "https://google.com/search?q="
	for i in range(1,len(sys.argv)-1):
		url+=sys.argv[i]+" "
elif sys.argv[-1] == "2":
	print("Here are the pictures")
	url = "https://www.google.com/search?tbm=isch&q="
	for i in range(1,len(sys.argv)-1):
		url+=sys.argv[i]+" "
driver = webdriver.Chrome()
driver.get(url)
sleep(10)
driver.quit()