from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome()
driver.get('https://www.dramexchange.com')
html = driver.page_source
driver.close()
soup = BeautifulSoup(html, 'html.parser')


left_tab = soup.find('div', {'class':'left_tab'})

#print(left_tab)

contract_title = left_tab.find('td', {'class':'title_left2'})
contract_title_time = left_tab.find('td', {'class':'title_right2'})

#print(contract_title)
#print(contract_title_time)
title_row = []
row = []
row.append(contract_title.get_text(strip=True))
row.append(contract_title_time.get_text(strip=True))

title_row.append(row)
#print(title_row)

title = left_tab.find_all('td', {'class':'title_left'})
title_time = left_tab.find_all('td', {'class':'title_right'})

for i in range(len(title)):
    row = []
    row.append(title[i].get_text(strip=True))
    row.append(title_time[i].get_text(strip=True))
    title_row.append(row)

#print(title_row)

id = left_tab.find_all('tbody', id=True)

price_list = []

j = 0
for i in id:
    trs = i.find_all('tr')
    price_list.append(title_row[j])
    j = j + 1
    for index in trs:
        tds = index.find_all("td")
        row = []
        for index2 in tds:
            row.append(index2.get_text(strip=True))
        price_list.append(row)

for i in range(len(price_list)):
    for j in range(len(price_list[i])):
        print(price_list[i][j], end =' ')
    print()
