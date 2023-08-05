import pandas as pd
from sqlalchemy import create_engine

with open("pandas_tut\\example.csv") as data:
    data_pd = pd.read_csv(data)

print(data_pd)

data_pd.to_csv("pandas_tut\\example_output.csv", index= False)

file_pd = pd.read_excel("pandas_tut\\Excel_Sample.xlsx", sheet_name = "Sheet1")

print(file_pd)

data_html = pd.read_html('https://www.fdic.gov/resources/resolutions/bank-failures/failed-bank-list/')

print(data_html)
print(type(data_html))

engine = create_engine("sqlite:///:memory:")

data_pd.to_sql("my_table", engine)

data_sql = pd.read_sql("my_table", con= engine)
print(data_sql)