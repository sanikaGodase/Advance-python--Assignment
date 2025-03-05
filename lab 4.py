Name: Godase Sanika

Lab 4


1. Suppose you are a teacher, and you want to analyze the exam scores of your students 
in a particular subject. You have recorded the scores of your students 
for a recent exam, and you want to represent this data using a Pandas Series

Input:
import pandas as pd
students = ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Hannah', 'Ivy', 'Jack']
exam_scores = [92, 88, 76, 94, 82, 90, 85, 89, 78, 91]
# Create a Pandas Series to represent the exam scores
exam_series = pd.Series(exam_scores, index=students, name="Exam Scores")
print(exam_series)

Output:
Alice      92
Bob        88
Charlie    76
David      94
Eve        82
Frank      90
Grace      85
Hannah     89
Ivy        78
Jack       91
Name: Exam Scores, dtype: int64

----------------------------------------------------------------------------------------------------------------------------------------------------------------------

2.Suppose you want to track and analyze the monthly energy consumption in your
home. You have recorded the monthly energy usage for electricity and gas over a year,
and you want to represent this data using Pandas Series.

Input:
import pandas as pd
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 
          'September', 'October', 'November', 'December']
electricity_usage = [350, 320, 310, 330, 340, 370, 380, 360, 350, 330, 320, 330]
gas_usage = [20, 18, 16, 15, 12, 10, 8, 9, 12, 15, 17, 19]
# Create Pandas Series for electricity and gas usage
electricity_series = pd.Series(electricity_usage, index=months, name="Electricity Usage (kWh)")
gas_series = pd.Series(gas_usage, index=months, name="Gas Usage (therms)")
print("Electricity Usage Data:")
print(electricity_series)
print("\nGas Usage Data:")
print(gas_series)

Output:
Electricity Usage Data:
January      350
February     320
March        310
April        330
May          340
June         370
July         380
August       360
September    350
October      330
November     320
December     330
Name: Electricity Usage (kWh), dtype: int64

Gas Usage Data:
January      20
February     18
March        16
April        15
May          12
June         10
July          8
August        9
September    12
October      15
November     17
December     19
Name: Gas Usage (therms), dtype: int64


