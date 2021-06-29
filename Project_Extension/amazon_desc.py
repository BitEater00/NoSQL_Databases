from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup
import time
import os
import pandas as pd
import xlwt
from xlwt import Workbook

book_ASIN_list = []
options = Options()
options.headless = True
base_path = os.path.realpath('.')
geckodriver_path = base_path + r'\geckodriver.exe'
options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
driver = webdriver.Firefox(options=options, executable_path = geckodriver_path)
print("Web Driver Identified")

read_asin = pd.read_csv("numbers.csv")
print("CSV data read")

wb = Workbook()
print("WorkBook Added")
sheet1 = wb.add_sheet('DESC')
print("Sheet Added")

print("Starting reading of desc")
for index, row in read_asin.iterrows():
    print("[x] Index : " + str(index))
    ASIN = str(row["ASIN"])
    print("[x]Getting data for ASIN number" + ASIN)
    if len(ASIN) == 9:
        ASIN = "0" + ASIN
    URL = 'https://www.amazon.in/dp/' + ASIN
    start = time.time()
    try:
        print("[x]Visiting url for " + ASIN)
        driver.get(URL)
        driver.switch_to.frame("bookDesc_iframe")
        source_code = driver.page_source
        inspect_code = driver.execute_script("return document.documentElement.innerHTML;")
        soup = BeautifulSoup(inspect_code, "html.parser")
        description_received = soup.find("div" , {"id":"iframeContent"}).text
        sheet1.write(index,0,ASIN)
        sheet1.write(index,1,description_received)
        print("[x]Description Writing done for " + ASIN)
    except:
        book_ASIN_list.append(ASIN)
        print("[E]ERROR RECEIVED FOR " + ASIN)


    end = time.time()
    print(f"Runtime of the program is {end - start}")

driver.quit()
print("Driver Closed")
print("Saving file")
wb.save('desc_data.xls')
print("File Saved")
print("Saving ASIN to delete")
dict = {"ASIN" : book_ASIN_list}
df = pd.DataFrame(dict) 
df.to_csv('amz_todel2.csv') 
print("Saved file")
print("Closing Program")