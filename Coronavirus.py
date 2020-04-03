import requests
from bs4 import BeautifulSoup
import smtplib
import time
import operator


def coronavirus():
    url = "https://www.worldometers.info/coronavirus/"

    headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/79.0.3945.88 Safari/537.36'}

    page = requests.get(url, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    lines = soup.find(id='main_table_countries_today').get_text()
    # print(lines)

    Data = lines.split("\n")
    del Data[:17]
    # print(Data)

    table = dict()
    x = 0
    for _ in range(206):
        table[Data[x]] = [Data[x+1], Data[x+3]]
        x += 12
    # print(table)

    for key in table.keys():
        table[key][0] = int(table[key][0].replace(",", ""))
        table[key][1] = table[key][1].strip().replace(",", "")
        if table[key][1] == '':
            table[key][1] = "0"
        table[key][1] = int(table[key][1])
        # print(table[key])
    # print(table)
    sorted_table = sorted(table.items(), key=operator.itemgetter(1), reverse=True)
    # print(sorted_table)

    print("{:<7} {:<25} {:<15} {:<10} {:<10}".format("Rank", "Country, Other",
          "Infections", "Deaths", "Mortality"))
    rank = 1
    for key, value in sorted_table:
        z = key
        a, b = value
        print("# {:<5} {:<25} {:<15} {:<10} {:5.2f} %".format(rank, z, a, b,
             (b / a * 100)))
        rank += 1


while True:
    coronavirus()
    time.sleep(60*60)
