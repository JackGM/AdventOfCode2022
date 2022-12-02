import numpy as np
import pandas as pd
import math as math

df = pd.read_csv('input.txt', skip_blank_lines=False)
#print(df)

i = 0
Value = 0
results = []

for row in df:
    print(df[row])
    if math.isnan(df[row]) == False:
        Value = Value + row
        print("Added Value")
    else:
        i = i + 1
        print(Value)
        Value = 0
        print("NaN")







   

