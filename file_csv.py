import pandas as pd
import csv 
import scrap

filepath = 'scrap.csv'
data = pd.read_csv(filepath)
print("enter what do you want to do: \nscan - scrap current exchanging rates\nmin - find minimum value at the specific currency")
command = input()



if(command == "scan"):
    scrap.scan_check()
    
elif(command == "min"):
    print("please provide what currency minimum you want to know?")
    currency = input()
    values = data.loc[data["from/to"] == currency, "bid"]
    min = values.values[0]
    min_idx = 0
    for i in range(len(values.values)):
        if(values.values[i] <= min):
            min = values.values[i]
            min_idx = values.index[i]
    print(f"the least value of {currency} was {min} at {data.loc[min_idx, 'time']}")