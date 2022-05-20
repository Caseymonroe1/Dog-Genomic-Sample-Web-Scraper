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
worksheet.write(0,0,"Name")
worksheet.write(0,1,"Breed")
worksheet.write(0,2,"Gender")
worksheet.write(0,3,"Link")
worksheet.write(0,4,"Date of Last Edit")
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
    print(line)
    html=soup
    worksheet.write(rows,0,line)
    worksheet.write(rows,3,link)
    statusString=""
    i=""
    if "Status" in str(html): 
        status=re.search("Status",str(html))
        statusend=status.end()+20
        
        while i!='<':
            i=str(html)[statusend]
            statusString+=i
            statusend+=1
        statusString = statusString.rstrip(statusString[-1])
        worksheet.write(rows,4,statusString)
        print(statusString)
    i=""
    if "breed: " in str(html):
        breed=re.search("breed: ",str(html))
        breedString=""
        breednum=breed.start()+7
        while i!='<':
            i=str(html)[breednum]
            breednum=breednum+1
            breedString=breedString+i
        breedString = breedString.rstrip(breedString[-1])
        print(breedString)
        worksheet.write(rows,1,breedString)
    i=""
    #both gender and sex were used in the pages, so the two if statements for those
    if ("gender: " or "Gender: ")  in str(html):
        gender=re.search("gender: ",str(html))
        genderString=""
        gendernum=gender.start()+8
        while i!='<':
            i=str(html)[gendernum]
            gendernum=gendernum+1
            genderString=genderString+i
        genderString=genderString.rstrip(genderString[-1])
        print(genderString)
        worksheet.write(rows,2,genderString)
    i=""
    if ("Sex: " or "sex: ") in str(html):
        gender=re.search("Sex: ",str(html))
        genderString=""
        gendernum=gender.start()+5
        while i!='<':
            i=str(html)[gendernum]
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



