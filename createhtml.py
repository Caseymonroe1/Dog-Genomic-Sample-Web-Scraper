from selenium import webdriver 
import re
import bs4
import xlwt
from xlwt import Workbook
from xlwt import Worksheet
PATH = "C:\\Program Files (x86)\chromedriver.exe"
driver=webdriver.Chrome(PATH)

f=open("htmlex.txt","w+")
link = 'https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM5799392'
driver.get(link)
soup=bs4.BeautifulSoup(driver.page_source, 'html.parser')


for line in str(soup):
    f.write(str(line))

html=""
driver.quit()

