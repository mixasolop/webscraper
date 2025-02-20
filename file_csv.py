import pandas as pd
import csv 
from scrap import scan

filepath = 'C:/code/.vscode/webscraper/scrap.csv'
collums = ["from/to", "ask"]
data = [
    ['from/to', 'bid', 'ask', 'max_bid', 'min_bid'],
    ["EUR/USD", "1,04", "1,05", "1,1", "1,03"]
]
print("enter command")
command = "scan"

if(command == "scan"):
    scan()