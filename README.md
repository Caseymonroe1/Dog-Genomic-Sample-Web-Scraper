# Dog-Genomic-Sample-Web-Scraper

In this project, I created a database of information on samples of dog genomic data from the National Center for Biotechnology Information website, and used this database to create multiple charts that visualized the data.  I used Python's Selenium, BeautifulSoup, and Excel Writer(xlwt) libraries for the web scraper, and R to create visualizations of the data.

  The web scraper takes in IDs of 3415 different samples from a csv file created by makeFile.py, and scrapes data from the links to these samples.  The scraper finds the breed, gender, date of last edit, and if the filetype of the sample is .IDAT or not.  This data is written to an excel sheet, which is used in an R script that formats the excel data and creates multiple visualizations, including bar charts and a pie chart.
