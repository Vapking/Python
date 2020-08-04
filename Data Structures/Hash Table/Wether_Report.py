import pandas as pd
import numpy as np

def main():
    data = pd.read_csv("nyc_weather.csv")
    arr = np.array(data)
    lst = []
    for elements in arr:
        lst.append(elements[1])
    print("Average tempeature first week was : ",((sum(lst[0:7]))/len(lst[0:7])))
    print("Maximum tempeature of 10 Days : ",max(lst[0:10]))
    print("In Wether Report Program.")

if __name__ == "__main__":
    main()