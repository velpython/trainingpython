import pandas as pd

df = pd.read_excel("D:\\python training\\bq7971xQ1-A0-Electrical Characteristics_example.xlsx")
vel = df[df['SPEC ID'] == '6EZTK3_1' ] [['TEST CONDITIONS','TYP']]
print(vel)