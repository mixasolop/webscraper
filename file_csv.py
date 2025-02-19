import pandas as pd
import csv 

filepath = 'D:/code/projects/webscraper/scrap.csv'
collums = ["from/to", "ask"]
data = [
    ['from/to', 'bid', 'ask', 'max_bid', 'min_bid'],
    ["EUR/USD", "1,04", "1,05", "1,1", "1,03"]
]

with open(filepath,"w", newline="") as wfile:
    writer  = csv.writer(wfile)
    writer.writerows(data)

dt = pd.read_csv(filepath)



print(dt)