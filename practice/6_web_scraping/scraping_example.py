import requests
from bs4 import BeautifulSoup

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

results = soup.find(id="ResultsContainer")

job_elements = results.find_all("div", class_="card-content")

for job_element in job_elements:
    title_element = job_element.find("h2", class_="title")
    company_element = job_element.find("h3", class_="company")
    location_element = job_element.find("p", class_="location")
    '''print(title_element.text.strip())
    print(company_element.text.strip())
    print(location_element.text.strip())
    print()'''

print(type(results))
print("##########")
print(str(results)[:50])
print("###################")
python_jobs = results.find_all(
    "h2", string=lambda tag: print(type(tag), dir(tag)[:5]) or "python" in tag.lower()
)
print("###################")
print(len(python_jobs))
print(type(python_jobs[0]))
import json
print(json.dumps(python_jobs, indent=4, default=str))

'''
l = [lambda x: x*x for x in range(10)]

result = [f(x) for f, x in zip(l, range(10))]
print(result)
'''