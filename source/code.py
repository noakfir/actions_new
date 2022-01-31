import pandas as pd
import math
df = pd.read_csv("example.csv")
df["a/b"] = df["a"]/df["b"]

if math.isinf(df["a/b"][2]):
    raise ValueError


    

      


      