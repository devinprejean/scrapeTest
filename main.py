import requests
from bs4 import BeautifulSoup as soup

my_url = 'https://scrapethissite.com/pages/simple/'
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
headers = {'User-Agent': user_agent}
response = requests.get(my_url,headers=headers)
html = response.content
page = soup(html, "html.parser")
countries = page.find_all('div', {'class': 'country'})
print(countries)

