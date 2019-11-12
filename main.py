import requests

indeed_result = requests.get('https://kr.indeed.com/jobs?q=%EB%8C%80%EA%B8%B0%EC%97%85&limit=50&radius=25&start=950')

print(indeed_result.json())