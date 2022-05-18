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
    #for each sample in the sample names file, get the link and html of the page
    link="https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc="+line
    driver.get(link)
    soup = bs4.BeautifulSoup(driver.page_source, 'html.parser')
    count=0
    html=soup
    
    for thelines in html:
        #for each line in the html, check if it contains breed and gender
        #then add each to the spreadsheet if they are present in the page
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
        #both gender and sex were used in the pages, so the two if statements for those
        if ("gender: " or "Gender: ")  in str(thelines):
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
        if ("Sex: " or "sex: ") in str(thelines):
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
        #saving the spreadsheet every iteration isn't necessary but useful for testing
        workbook.save('samples.xls')
workbook.save('samples.xls')
driver.quit()
