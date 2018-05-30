import requests
from bs4 import BeautifulSoup as soup

my_url = 'https://scrapethissite.com/pages/simple/'
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
headers = {'User-Agent': user_agent}
response = requests.get(my_url,headers=headers)
html = response.content
page = soup(html, "html.parser")

f = open("scrapedData.csv", "w")
headers = "Country,Capital,Population,Area \n"

f.write(headers)
countries = page.find_all('div', {'class': 'country'})

for country in countries:
    capital = country.find('span', {'class': 'country-capital'}).text
    print(capital)
    population = country.find('span', {'class': 'country-population'}).text
    #print(population)
    area = country.find('span', {'class': 'country-area'}).text
    #print(country.h3.text.strip() + "," + capital + "," + population + "," + area + "\n")
    f.write(country.h3.text.strip() + "," + capital.replace('\u015f', 's').replace('\u0103', 'a') + "," + population + "," + area + "\n")

f.close()
print("done!")

