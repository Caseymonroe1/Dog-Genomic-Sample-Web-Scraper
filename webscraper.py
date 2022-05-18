from selenium import webdriver 
import re
import bs4
import xlwt
from xlwt import Workbook
from xlwt import Workbook
PATH = "C:\\Program Files (x86)\chromedriver.exe"
driver=webdriver.Chrome(PATH)

#setting up the excel file
workbook = Workbook()
worksheet = workbook.add_sheet('Sheet 1')
worksheet.write(0,0,"Sample Name")
worksheet.write(0,1,"Sample Breed")
worksheet.write(0,2,"Sample Gender")
#opening sample names file
with open('cleanedsamplenames.txt') as f:
    lines = f.readlines()


html=""
rows=1
for line in lines:
    link="https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc="+line
    driver.get(link)
    soup = bs4.BeautifulSoup(driver.page_source, 'html.parser')
    count=0
    html=soup
    
    for thelines in html:
        worksheet.write(rows,0,line)
        i=""
        if "breed: " in str(thelines):
            breed=re.search("breed: ",str(thelines))
            breedString=""
            breednum=breed.start()+7
            while i!='<':
                i=str(thelines)[breednum]
                breednum=breednum+1
                breedString=breedString+i
            breedString = breedString.rstrip(breedString[-1])
            print(breedString)
            worksheet.write(rows,1,breedString)
        i=""
        if "gender: " in str(thelines):
            gender=re.search("gender: ",str(thelines))
            genderString=""
            gendernum=gender.start()+8
            while i!='<':
                i=str(thelines)[gendernum]
                gendernum=gendernum+1
                genderString=genderString+i
            genderString=genderString.rstrip(genderString[-1])
            print(genderString)
            worksheet.write(rows,2,genderString)
        if "Sex: " in str(thelines):
            gender=re.search("Sex: ",str(thelines))
            genderString=""
            gendernum=gender.start()+5
            while i!='<':
                i=str(thelines)[gendernum]
                gendernum=gendernum+1
                genderString=genderString+i
            genderString=genderString.rstrip(genderString[-1])
            print(genderString)
            worksheet.write(rows,2,genderString)
        
        rows+=1
        workbook.save('samples.xls')
workbook.save('samples.xls')
#workbook.save()
driver.quit()
#iterate through each sample by changing the url and scrape the data, adding to excel spreadsheet

# driver.find_element_by_name("q").send_keys("Selenium")
# driver.find_element_by_name("btnK").click()