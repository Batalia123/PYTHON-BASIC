"""
There is a list of most active Stocks on Yahoo Finance https://finance.yahoo.com/most-active.
You need to compose several sheets based on data about companies from this list.
To fetch data from webpage you can use requests lib. To parse html you can use beautiful soup lib or lxml.
Sheets which are needed:
1. 5 stocks with most youngest CEOs and print sheet to output. You can find CEO info in Profile tab of concrete stock.
    Sheet's fields: Name, Code, Country, Employees, CEO Name, CEO Year Born.
2. 10 stocks with best 52-Week Change. 52-Week Change placed on Statistics tab.
    Sheet's fields: Name, Code, 52-Week Change, Total Cash
3. 10 largest holds of Blackrock Inc. You can find related info on the Holders tab.
    Blackrock Inc is an investment management corporation.
    Sheet's fields: Name, Code, Shares, Date Reported, % Out, Value.
    All fields except first two should be taken from Holders tab.


Example for the first sheet (you need to use same sheet format):
==================================== 5 stocks with most youngest CEOs ===================================
| Name        | Code | Country       | Employees | CEO Name                             | CEO Year Born |
---------------------------------------------------------------------------------------------------------
| Pfizer Inc. | PFE  | United States | 78500     | Dr. Albert Bourla D.V.M., DVM, Ph.D. | 1962          |
...

About sheet format:
- sheet title should be aligned to center
- all columns should be aligned to the left
- empty line after sheet

Write at least 2 tests on your choose.
Links:
    - requests docs: https://docs.python-requests.org/en/latest/
    - beautiful soup docs: https://www.crummy.com/software/BeautifulSoup/bs4/doc/
    - lxml docs: https://lxml.de/
"""
import requests
import ssl
from urllib.request import urlopen
from bs4 import BeautifulSoup
from math import ceil

ssl._create_default_https_context = ssl._create_unverified_context
#url = "http://finance.yahoo.com/most-active"
url = "https://finance.yahoo.com/quote/BLK/holders?p=BLK"
#response = requests.get(url)
#page = urlopen(url)
#print(page)
response = requests.get(url)
soup = BeautifulSoup(response.content, "lxml")


sheet_attributes ={"5 stocks with most youngest CEOs":["Name       ", "Code","Country      ","Employees" ,"CEO Name                            ","CEO Year Born"], "10 stocks with best 52-Week Change":["Name       ", "Code","52-Week Change", "Total Cash"], "10 largest holds of Blackrock Inc":["Name       ", "Code","Shares", "Date Reported", "% Out", "Value  "]}

#print(len("==================================== 5 stocks with most youngest CEOs ==================================="))

with open("sheets.txt", "w") as sheets:
    for sh in ["5 stocks with most youngest CEOs", "10 stocks with best 52-Week Change", "10 largest holds of Blackrock Inc"]:
        sheet_width = sum(len(i)+3 for i in sheet_attributes[sh]) + 1
        #print(sheet_width)
        sheets.write( "="*int( (sheet_width-2-len(sh))/2 ) + " " + sh + " " + "="*ceil( ( (sheet_width-2-len(sh))/2 ) ) + "\n")
        sheets.write("-"*sheet_width + "\n")

        for att in sheet_attributes[sh]:
            sheets.write("| " + att + " ")

        sheets.write("|\n")
        sheets.write("\n")

with open("active_stocks.html", "w") as f:
    f.write(response.text)
with open("active_stocks.html", "r") as f:
    print(f.read())

with open("active_stocks.html") as html_file:
    soup = BeautifulSoup(html_file, 'lxml')
    match = soup.find(string='yahoo')
    print(match)

with open("sheets.txt", "r") as sh:
    #print(sh.read())
    pass




