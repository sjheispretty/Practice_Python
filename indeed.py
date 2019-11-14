import requests
from bs4 import BeautifulSoup

INDEED_URL = 'https://kr.indeed.com/jobs? q=%EB%8C%80%EA%B8%B0%EC%97%85&limit=50'

def extract_indeed_pages() :
  # Request를 통해 html을 가져올수 있게 해준다.
  indeed_result = requests.get(INDEED_URL)

# Beautifulsoup를 통해 방대한 데이터에서 오브젝트를 뽑아낸다.
  indeed_soup = BeautifulSoup(indeed_result.text, "html.parser")

  pagination = indeed_soup.find("div", {"class": "pagination"})

  links=pagination.find_all('a')
  pages = []


# a태그를 돌면서 span 내의 숫자값을 str 형태로 읽어온다. int로 형변환가능
# for link in links :
#   print(link.find("span").string)
  for link in links[1:] :
   pages.append(int(link.string))

#max_page의 값은 pages배열의 맨 마지막값 : 19
  max_page = pages[-1]

  for n in range(max_page) :
    print(f"start={n*50}")