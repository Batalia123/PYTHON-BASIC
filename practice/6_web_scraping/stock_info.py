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
from bs4 import BeautifulSoup
import re
#SQLite

#ssl._create_default_https_context = ssl._create_unverified_context




class HolderScraper:
    def __init__(self, url):
        self.url = url
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (X11; OpenBSD i386) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36'
        }
        self.response = None
        self.soup = None
        self.institutional_ranking = None
        self.mutual_rating = None
        self.all_holders = None
        self.sorted_all_holders = None
        self.yearly_52_week_change = None

    def fetch_data(self):
        self.response = requests.get(self.url, headers=self.headers)
        self.soup = BeautifulSoup(self.response.content, "lxml")
        #print(self.soup)

    def scrape_symbols(self):
        links = self.soup.find_all('a', attrs={'data-test': True})
        symbols = [link['href'] for link in links]
        symbols = [ re.findall(r'(p=\D*)', symbol)[0][2:] for symbol in symbols ]
        values = []

        for company_symbol in symbols:
            print(company_url := f'https://finance.yahoo.com/quote/{company_symbol}/key-statistics?p={company_symbol}')
            content = requests.get(company_url, headers=self.headers).content
            new_soup = BeautifulSoup(content, 'lxml')

            company_name = new_soup.find('h1').get_text()

            main_id = "Col1-0-KeyStatistics-Proxy"
            metric_value = new_soup.find(id=main_id).find_all('td')[21].get_text()[:-1]

            total_cash = new_soup.find(id=main_id).find_all('td')[105].get_text()

            values.append(
                (company_name, company_symbol, float(metric_value), total_cash)
            )

        self.yearly_52_week_change = sorted(values, key=lambda x: x[2], reverse=True)

        # Top 10 companies by this metric
        for item in self.yearly_52_week_change[:10]:
            print(item)

    def scrape_institutional_holders(self):
        institutional_holders = self.soup.find_all(['tbody'])[1]
        keys = [institutional_holders.find_all('td')[i*5].get_text()[:-1] for i in range(10)]
        values = [institutional_holders.find_all('td')[i*5+3].get_text()[:-1] for i in range(10)]
        self.institutional_ranking = dict(zip(keys, values))

    def scrape_mutual_holders(self):
        mutual_holders = self.soup.find_all(['tbody'])[2]
        keys = [mutual_holders.find_all('td')[i*5].get_text()[:-1] for i in range(10)]
        values = [mutual_holders.find_all('td')[i*5+3].get_text()[:-1] for i in range(10)]
        self.mutual_rating = dict(zip(keys, values))

    def combine_holders(self):
        self.all_holders = {**self.institutional_ranking, **self.mutual_rating}
        self.sorted_all_holders = sorted(self.all_holders.items(), key=lambda kv: kv[1], reverse=True)

    def print_top_holders(self):
        print("10 largest holds of Blackrock Inc:")
        for holder, rating in self.sorted_all_holders[:10]:
            print(f"{holder}: {rating}")


'''url = 'https://finance.yahoo.com/quote/BLK/holders?p=BLK'
scraper = HolderScraper(url)
scraper.fetch_data()
scraper.scrape_institutional_holders()
scraper.scrape_mutual_holders()
scraper.combine_holders()
scraper.print_top_holders()'''

url = "https://finance.yahoo.com/most-active"
scraper = HolderScraper(url)
scraper.fetch_data()
scraper.scrape_symbols()
