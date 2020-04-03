import requests
from bs4 import BeautifulSoup
import smtplib
import time


def corona():
    url = "https://www.worldometers.info/coronavirus/"

    headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/79.0.3945.88 Safari/537.36'}

    page = requests.get(url, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    Data = soup.find(id='main_table_countries_today').get_text().strip().split()
    # print(Data)

    table = dict()
    x = 13
    for _ in range(10):
        table[Data[x]] = [Data[x+1], Data[x+3]]
        x += 10
    # print(table)

    print("{:<15} {:<10} {:<10} {:<10}".format("Country", "Cases", "Deaths", "DeathRate"))
    for key, value in table.items():
        z = key
        a, b = value
        print("{:<15} {:<10} {:<10} {:5.2f} %".format(z, a, b,
             (int(b.replace(",", "")) / int(a.replace(",",  "")) * 100)))


if __name__ == "__main__":
    corona()
    # time.sleep(60*24)
