import requests
from bs4 import BeautifulSoup

website_url = requests.get('https://en.wikipedia.org/wiki/List_of_file_signatures').text

soup = BeautifulSoup(website_url, 'lxml')
# print(soup.prettify())

my_table = soup.find('table',{'class':'wikitable sortable'})
#print(my_table)

for row in my_table.findAll('tr'):
    print(row)

#print(cells)