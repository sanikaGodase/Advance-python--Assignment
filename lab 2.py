Name: Godase Sanika 

Lab 2

1. Suppose you have a dataset containing daily temperature readings for a city, and you want to identify days with extreme temperature conditions. Find days where the temperature either exceeded 35 degrees Celsius (hot day) or dropped below 5 degrees Celsius (cold day)
Input:
import numpy as np
temperatures = np.array([32.5, 34.2, 36.8, 29.3, 31.0, 38.7, 23.1, 18.5, 22.8, 37.2, 4.0, -4.0, -12.0])
# Find hot days (temperature > 35°C)
hot_days = np.where(temperatures > 35)[0]
hot_temperatures = temperatures[temperatures > 35]
# Find cold days (temperature < 5°C)
cold_days = np.where(temperatures < 5)[0]
cold_temperatures = temperatures[temperatures < 5]
print("Hot Days:")
print("Day  Temperature (°C)")
for day, temp in zip(hot_days, hot_temperatures):
    print(f"{day+1}    {temp}")
print("\nCold ys:")
print("Day  Temperature (°C)")
for day, temp in zip(cold_dDays, cold_temperatures):
    print(f"{day+1}    {temp}")

Output:
Hot Days:
Day  Temperature (°C)
3    36.8
6    38.7
10    37.2

Cold Days:
Day  Temperature (°C)
11    4.0
12    -4.0
13    -12.0

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

2. Suppose you have a dataset containing monthly sales data for a company, and you
want to split this data into quarterly reports for analysis and reporting purposes
Input:
import numpy as np
monthly_sales = np.array([120, 135, 148, 165, 180, 155, 168, 190, 205, 198, 210, 225])
# Split the monthly sales data into 4 quarters
quarter1_sales = monthly_sales[0:3]
quarter2_sales = monthly_sales[3:6]
quarter3_sales = monthly_sales[6:9]
quarter4_sales = monthly_sales[9:12]
print("Quarter 1 Sales (in thousands of dollars):")
print(quarter1_sales)
print("\nQuarter 2 Sales (in thousands of dollars):")
print(quarter2_sales)
print("\nQuarter 3 Sales (in thousands of dollars):")
print(quarter3_sales)
print("\nQuarter 4 Sales (in thousands of dollars):")
print(quarter4_sales)

Output:
Quarter 1 Sales (in thousands of dollars):
[120 135 148]

Quarter 2 Sales (in thousands of dollars):
[165 180 155]

Quarter 3 Sales (in thousands of dollars):
[168 190 205]

Quarter 4 Sales (in thousands of dollars):
[198 210 225]