import requests
from bs4 import BeautifulSoup
import pandas as pd

URL = "https://www.investing.com/currencies/streaming-forex-rates-majors"


page = requests.get(URL)

if(page.status_code == 200):
    soup = BeautifulSoup(page.text, "html.parser")
    result = soup.find("tbody", class_="datatable-v2_body__8TXQk")
    if(result):
        print("NICE!")
        rows = result.find_all("tr")
        names = []
        prices = {}
        if(rows):
            for row in rows:
                title = row.find("span", {"dir":"ltr"})
                names.append(title.text)
                nums = row.find_all("td", class_="rtl:text-right")
                sell = nums[0]
                buy = nums[1]
                prices[title.text] = [buy.text, sell.text]
    else:
        print(":((")
else:
    print(page.status_code)

print(names)
print("what currency do you want to exchange?")
input_curr = input()
print("Here are currencies that you can exchange yours:")
for cur in names:
    if(input_curr in cur[0:3]):
        print(f"{cur[-3]}{cur[-2]}{cur[-1]}")
print("please pick one:")
output_curr = input()
full = input_curr+"/"+output_curr
print(full)
print(f"the exchange is {prices[full][0]}")