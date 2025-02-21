import pandas as pd
import csv 
import scrap

filepath = 'scrap.csv'
data = pd.read_csv(filepath, usecols=["bid"])
print("enter what do you want to do: \nscan - scrap current exchanging rates\nmin - find minimum value at the specific currency")
command = input()



if(command == "scan"):
    scrap.scan_check()
