from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

chromedriver_location = "C:\\chromedriver.exe"
refund_amount = "1000"
ssn1 = "123"
ssn2 = "45"
ssn3 = "6789"

# the 2nd item on the list is for a joint return
filing_input = '//*[@id="filingStatus2"]'

driver = webdriver.Chrome(chromedriver_location)
driver.get('https://sa.www4.irs.gov/irfof/lang/en/irfofgetstatus.jsp')

driver.switch_to.alert.accept();

ssn1_input = '//*[@id="TIN3"]'
ssn2_input = '//*[@id="TIN2"]'
ssn3_input = '//*[@id="TIN5"]'
refund_input = '//*[@id="refundAmount"]'

driver.find_element_by_xpath(ssn1_input).send_keys(ssn1)
driver.find_element_by_xpath(ssn2_input).send_keys(ssn2)
driver.find_element_by_xpath(ssn3_input).send_keys(ssn3)
driver.find_element_by_xpath(filing_input).click()
driver.find_element_by_xpath(refund_input).send_keys(refund_amount)


