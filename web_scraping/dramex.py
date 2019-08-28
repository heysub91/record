from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome()
driver.get('https://www.dramexchange.com')
html = driver.page_source
driver.close()
soup = BeautifulSoup(html, 'html.parser')


id = soup.find(id = 'tb_NationalDramSpotPrice')


trs = id.find_all('tr')

price_list = []

for index in trs:
    tds = index.find_all("td")
    row = []
    for index2 in tds:
        row.append(index2.get_text(strip=True))
    price_list.append(row)

print(price_list[0])
print('--------------')
print(price_list[1])
print('--------------')
print(price_list[2])
print('--------------')
print(price_list[3])
print('--------------')
print(price_list[4])
print('--------------')
print(price_list[5])
print('--------------')
print(price_list[6])
