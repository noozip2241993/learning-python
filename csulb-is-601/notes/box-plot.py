import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_excel("example.xlsx", usecols=[0,1], sheet_name="Sheet1")

print(df)