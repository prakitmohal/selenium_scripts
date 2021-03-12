from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

chromedriver_location = "C:\\chromedriver.exe"
refund_amount = "100"
ssn = "123456789"

driver = webdriver.Chrome(chromedriver_location)
driver.get('https://mypath.pa.gov')

time.sleep(2)

refund_link = '//*[@id="Dg-b"]/tbody[4]/tr[2]'

driver.find_element_by_xpath(refund_link).click()

time.sleep(2)

refund_input = '//*[@id="Dd-a"]'
ssn_input = '//*[@id="Dd-b"]'

driver.find_element_by_xpath(refund_input).send_keys(refund_amount)
driver.find_element_by_xpath(ssn_input).send_keys(ssn)

time.sleep(2)

driver.find_element_by_xpath(ssn_input).send_keys(Keys.TAB)
driver.find_element_by_xpath(ssn_input).send_keys(Keys.ENTER)


