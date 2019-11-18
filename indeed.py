import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = f'https://kr.indeed.com/jobs?q=%EB%8C%80%EA%B8%B0%EC%97%85&limit={LIMIT}'

def get_last_page() :
  # Request를 통해 html을 가져올수 있게 해준다.
  indeed_result = requests.get(URL)

# Beautifulsoup를 통해 방대한 데이터에서 오브젝트를 뽑아낸다.
  indeed_soup = BeautifulSoup(indeed_result.text, "html.parser")

  pagination = indeed_soup.find("div", {"class": "pagination"})

  links=pagination.find_all('a')
  pages = []

  # a태그를 돌면서 span 내의 숫자값을 str 형태로 읽어온다. int로 형변환가능
  # for link in links:
  #   print(link.find("span").string)

  for link in links[:-1] :
    pages.append(int(link.string))

#max_page의 값은 pages배열의 맨 마지막값 : 19
  max_page = pages[-1]
  return max_page

def extract_job(html):
    title= (html.find("div", {"class" :  "title"})).find("a")["title"]
    company=(html.find("span", {"class":"company"}))
    company_anchor = company.find("a")
    if company_anchor is not None :
      company = (str(company_anchor.string))
    else :
      company = (str(company.string))
    location = html.find("span", {"class": "location"}).string
    if location is None :
      location = "none"
    else :
      location = location 
    #여백을 지워주는 함수 strip이다 strip(F) 하면 F를 전부 삭제
    company=company.strip()
    return {'title': title, 'company': company, 'location' : location}

def extract_jobs(last_page):
  jobs = []
  print("number 1")
  for page in range(last_page):
    print("number 2")
    result = requests.get(f"{URL}&start={last_page*LIMIT}")
    soup = BeautifulSoup(result.text, "html.parser")
    results = soup.find_all("div", {"class": "jobsearch-SerpJobCard"})
    for result in results :
      job =extract_job(result)
      jobs.append(job)
  return jobs

def get_jobs() :
  last_page = get_last_page()
  jobs = extract_jobs(last_page)
  return jobs