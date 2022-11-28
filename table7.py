from bs4 import BeautifulSoup
import requests
import pandas as pd


url = "http://www.nfl.com/standings"
url = "https://fastestlaps.com/tracks/adm-miachkovo"
url = "https://www.nfl.com/standings/"
url = "https://www.nfl.com/standings/division/1999/REG"
url = " https://fastestlaps.com/tracks/adm-miachkovo"



url = "https://en.wikipedia.org/wiki/Ali_Gatie"
url = "https://github.com/fivethirtyeight/negro-leagues-player-ratings"
url = " https://en.wikipedia.org/wiki/List_of_European_Cup_and_UEFA_Champions_League_finals"
url = "https://en.wikipedia.org/wiki/List_of_NBA_champions"
url = " https://en.wikipedia.org/wiki/List_of_24_Hours_of_Le_Mans_winners"

page = requests.get(url)
# print(page.text)
soup = BeautifulSoup(page.text, 'lxml')
# print(soup)


title = soup.find_all('title')
# print(title)


for title in title:
    headering=title.find_all('h1')
    for header in title:
        print(header.text, end='')
    print()

tables = soup.find_all('table')
# print(tables)



for table in tables:
    heading=table.find_all('th')
    for header in heading:
        print(header.text, end='')
    # print()
    for row in table.find_all('tr'):
        for col in row.find_all('td'):
            print(col.text, end='|')
        print('\n')


        