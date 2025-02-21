import pandas as pd
import csv 
import scrap

filepath = 'scrap.csv'

data = pd.read_csv(filepath)
command = input()

print("enter what do you want to do:\nscan - scrap current exchanging rates\nmin - find minimum of some currency exchange")

if(command == "scan"):
    scrap.scan_check()
