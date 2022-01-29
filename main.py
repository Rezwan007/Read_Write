import csv
import time
from selenium import webdriver

#mobileNumber="1741532908"
emailAddress="utsha1234@gmail.com"
passWordV="amijaninaa"

with open('sample.csv', 'r') as data_csv:
    csv_reader = csv.reader(data_csv)

    for line in csv_reader:
        browser = webdriver.Chrome("C:/Users/Rezwan/Documents/Python Scripts/chromedriver.exe")
        browser.get("https://www.rtvonline.com/youngstaraward/")

        time.sleep(2)
        clickButton = browser.find_element_by_xpath('/html/body/div[6]/form/fieldset/div/div[9]/div/div/section/label/img')
        clickButton.click()

        time.sleep(1)
        emailId = browser.find_element_by_xpath('/html/body/div[6]/form/div[2]/input[1]')
        emailId.send_keys(emailAddress)

        time.sleep(1)
        passWord = browser.find_element_by_xpath('/html/body/div[6]/form/div[2]/input[2]')
        passWord.send_keys(passWordV)

        time.sleep(1)
        mobileNumber = browser.find_element_by_xpath('/html/body/div[6]/form/div[2]/input[3]')
        mobileNumber.send_keys("01741532908")

        time.sleep(1)
        submiButton = browser.find_element_by_xpath('/html/body/div[6]/form/div[2]/h6[2]/button')
        submiButton.submit()

        time.sleep(1)
        succesConfirmation = browser.find_element_by_xpath('/html/body/div[6]/form/div[2]/h6[1]')
        print(succesConfirmation.text)
        print("*"*100)


        #browser.quit()
