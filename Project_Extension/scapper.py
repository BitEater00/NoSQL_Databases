from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup
import time

options = Options()
options.headless = True
options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
driver = webdriver.Firefox(options=options, executable_path=r'C:\Users\Ak\Desktop\SEM6\Theory\NoSQL\Project\Project_Extension\geckodriver.exe')
start = time.time()
driver.get('https://www.amazon.in/dp/0761183272/')
driver.switch_to.frame("bookDesc_iframe")
source_code = driver.page_source
inspect_code = driver.execute_script("return document.documentElement.innerHTML;")
soup = BeautifulSoup(inspect_code, "html.parser")
print(soup.find("div" , {"id":"iframeContent"}).text)
end = time.time()
driver.quit()
print(f"Runtime of the program is {end - start}")