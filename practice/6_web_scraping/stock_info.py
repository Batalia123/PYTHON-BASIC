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
from datetime import datetime
from bs4 import BeautifulSoup
import re


class HolderScraper:
    def __init__(self, url):
        self.url = url
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (X11; OpenBSD i386) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36'
        }
        self.response = None
        self.soup = None
        self.symbols = None
        self.institutional_ranking = None
        self.mutual_rating = None
        self.all_holders = None
        self.sorted_all_holders = None
        self.yearly_52_week_change = None
        self.youngest_CEOs = None

    def fetch_data(self):
        self.response = requests.get(self.url, headers=self.headers)
        self.soup = BeautifulSoup(self.response.content, "lxml")
        # print(self.soup)

    def scrape_symbols(self):
        links = self.soup.find_all('a', attrs={'data-test': True})
        self.symbols = [link['href'] for link in links]
        self.symbols = [re.findall(r'(p=\D*)', symbol)[0][2:] for symbol in self.symbols]
        # print(symbols)

    def scrape_52_week_change(self):
        self.yearly_52_week_change = {symbol: None for symbol in self.symbols}
        for company_symbol in self.symbols:
            company_url = f'https://finance.yahoo.com/quote/{company_symbol}/key-statistics?p={company_symbol}'
            content = requests.get(company_url, headers=self.headers).content
            new_soup = BeautifulSoup(content, 'lxml')

            company_name = new_soup.find('h1').get_text()
            index = company_name.find('(')
            company_name = company_name[:index - 1]

            main_id = "Col1-0-KeyStatistics-Proxy"
            metric_value = new_soup.find(id=main_id).find_all('td')[21].get_text()[:-1]

            #metric_value = new_soup.find(id=main_id)
            #print(company_symbol)
            #print(metric_value)
            # //*[@id="Col1-0-KeyStatistics-Proxy"]/section/div[2]/div[2]/div/div[1]/div/div/table/tbody/tr[2]/td[2]
            total_cash = new_soup.find(id=main_id).find_all('td')[105].get_text()
            list = [company_name, metric_value, total_cash]
            self.yearly_52_week_change[company_symbol] = list


    def sort_52_week_change(self):
        self.yearly_52_week_change = sorted(self.yearly_52_week_change.items(), key=lambda kv: kv[1][1], reverse=True)[:10]
        print(self.yearly_52_week_change)

    def scrape_youngest_CEOs(self):
        self.youngest_CEOs = {symbol: None for symbol in self.symbols}
        for symbol in self.symbols:
            profile_url = f'https://finance.yahoo.com/quote/{symbol}/profile?p={symbol}'
            content = requests.get(profile_url, headers=self.headers).content
            new_soup = BeautifulSoup(content, 'lxml')
            main_id = "Col1-0-Profile-Proxy"
            year = new_soup.find(id=main_id).find_all('td')[4].get_text()[:]
            # print(new_soup.find(id=main_id).find_all('td')[9].get_text()[:])
            company_name = new_soup.find('h1').get_text()
            index = company_name.find('(')
            company_name = company_name[:index - 1]
            spans = new_soup.find(id=main_id).find('section').find('section').find('table')
            ceo_name = spans.find_all('span', {'class': ''})[5].text
            lines = str(new_soup.find('div', id='Col1-0-Profile-Proxy').find('section').find('div').find('div').find(
                'div').find('p'))
            country = str(re.sub(r'<a class.*', '', lines)).split('<br/>')[-2]

            employee_number = new_soup.find('div', id='Col1-0-Profile-Proxy').find('section').find('div').find('div').find('div').find_all('p')[1].find_all('span')[-1].text
            list = [company_name, country, employee_number, ceo_name, year]
            self.youngest_CEOs[symbol] = list

    def sort_CEOs(self):
        self.youngest_CEOs = sorted(self.youngest_CEOs.items(), key=lambda kv: kv[1][-1], reverse=True)[:10]
        print(self.youngest_CEOs)

    def scrape_institutional_holders(self):
        institutional_holders = self.soup.find_all(['tbody'])[2]
        rows = [
            [
                td.get_text() for td in institutional_holders.find_all('td')[i * 5:(i + 1) * 5]
            ] for i in range(10)
        ]
        #keys = [institutional_holders.find_all('td')[i*5].get_text() for i in range(10)] #MOD
        #values = [institutional_holders.find_all('td')[i*5+3].get_text()[:-1] for i in range(10)]
        result = {row[0]: row[1:] for row in rows}

        for key in result:
            result[key][0] = result[key][0].replace(",", "")
            result[key][1] = datetime.strptime(result[key][1], '%b %d, %Y').date().isoformat()
            result[key][2] = result[key][2][:-1]
            result[key][3] = result[key][3].replace(",", "")
            result[key].insert(0, "TODO Company Code")
        self.institutional_ranking = result

    def scrape_mutual_holders(self):
        mutual_holders = self.soup.find_all(['tbody'])[2]
        rows = [
            [
                td.get_text() for td in mutual_holders.find_all('td')[i*5:(i+1)*5]
            ] for i in range(10)
        ]
        #keys = [mutual_holders.find_all('td')[i*5].get_text() for i in range(10)] #MOD
        #values = [mutual_holders.find_all('td')[i*5+3].get_text()[:-1] for i in range(10)]
        result = {row[0]: row[1:] for row in rows}
        for key in result:
            result[key][0] = result[key][0].replace(",", "")
            result[key][1] = datetime.strptime(result[key][1], '%b %d, %Y').date().isoformat()
            result[key][2] = result[key][2][:-1]
            result[key][3] = result[key][3].replace(",", "")
            result[key].insert(0, "TODO Company Code")
        self.mutual_rating = result

    def sort_combine_holders(self):
        self.all_holders = {**self.institutional_ranking, **self.mutual_rating}
        self.sorted_all_holders = sorted(self.all_holders.items(), key=lambda kv: kv[1][2], reverse=True)[:10]

    def print_top_holders(self):
        print("10 largest holds of Blackrock Inc:")
        for item in self.sorted_all_holders[:10]:
            print(type(item))


url = 'https://finance.yahoo.com/most-active'
scraper = HolderScraper(url)
scraper.fetch_data()
scraper.scrape_symbols()
scraper.scrape_52_week_change()
scraper.sort_52_week_change()
