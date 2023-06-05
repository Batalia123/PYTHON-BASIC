from urllib.request import urlopen
url = "http://olympus.realpython.org/profiles/dionysus"
page = urlopen(url)
html = page.read().decode("utf-8")

start_index = html.find("<title>") + len("<title>")
end_index = html.find("</title>")
#print(html)


import re

'''
pattern1 = re.findall('< *title.*?>', html, re.IGNORECASE)[0]
pattern2 = re.findall('< */ *title.*?>', html, re.IGNORECASE)[0]

start = html.find(pattern1) + len(pattern1)
end = html.find(pattern2)
#print(html[start:end])
'''

'''
pattern = "<title.*?>.*?</title.*?>"
match_results = re.search(pattern, html, re.IGNORECASE)
print(match_results.group())
title = match_results.group()
title = re.sub("<.*?>", "", title) # Remove HTML tags

print(title)
'''

'''
start = html.find("Favorite Color") + len("Favorite Color: ")
end = start + html[start:].find("<")

print(html[start:end].strip("\n\t\r"))
'''

# beauty_soup.py

from bs4 import BeautifulSoup

'''
url = "http://olympus.realpython.org"
page = urlopen(url + "/profiles")
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")
profiles = soup.find_all("a")
for p in profiles:
    print(url + p["href"])
'''
import mechanicalsoup
browser = mechanicalsoup.Browser()
'''
url = "http://olympus.realpython.org/login"
login_page = browser.get(url)
login_html = login_page.soup

# 2
form = login_html.select("form")[0]
form.select("input")[0]["value"] = "zeus"
form.select("input")[1]["value"] = "ThunderDude"

# 3
profiles_page = browser.submit(form, login_page.url)

base_url = "http://olympus.realpython.org"

links = profiles_page.soup.select("a")
for link in links:
    address = base_url + link["href"]
    print(link)
    #print(link.text)
    #print(f"{link.text}: {address}")

tag = profiles_page.soup.select("title")
for t in tag:
    print(t)
'''

import time
for i in range(4):
    browser = mechanicalsoup.Browser()
    page = browser.get("http://olympus.realpython.org/dice")
    tag = page.soup.select("#result")[0]
    result = tag.text
    print(page.soup.select("#result"))
    print(f"The result of your dice roll is: {result}")

    if(i<3): time.sleep(10)