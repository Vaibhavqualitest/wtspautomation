from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("C:\\Users\\Vaibhav\\Downloads\\chromedriver_win32\\chromedriver.exe")
driver.get("https://web.whatsapp.com/")

input("Please scan QR code--")
driver.find_element_by_css_selector('span[title="Vishnu Mishra"]').click()

message=driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div[2]/div/div[1]/div/div[2]")
for i in range(20):
    message.send_keys("message is only for automation of whatsapp")
    message.send_keys(Keys.RETURN)

