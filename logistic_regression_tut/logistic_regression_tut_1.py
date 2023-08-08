import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

with open("logistic_regression_tut\\titanic_train.csv") as data:
    data_pd = pd.read_csv(data)

print(data_pd)