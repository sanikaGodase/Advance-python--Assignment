Name : Godase Sanika

Lab 3

1. Analyze the relationship between the size of houses (measured in square
footage) and their selling prices in a particular neighborhood. You have collected
data on various houses in that neighborhood.Create a scatter plot using the
below data and share your conclusion/analysis.
Input:
import numpy as np
import matplotlib.pyplot as plt
square_footage = np.array([1200, 1400, 1600, 1800, 2000, 2200, 2400, 2600, 2800, 3000])
selling_prices = np.array([250, 290, 315, 380, 410, 450, 500, 525, 570, 610])
# Create a scatter plot
plt.scatter(square_footage, selling_prices, color='green')
plt.title("Housing Prices vs. Square Footage")
plt.xlabel("Square Footage (sq. ft.)")
plt.ylabel("Selling Price (1000$)")
plt.grid(True)
plt.show()

Output:




2. Create a pie chart to visualize the distribution of your monthly income by source. 
You have collected data on the various sources of your income, such as salary, 
freelance work, investments, and rental income. Share your conclusion/analysis
Input:
import matplotlib.pyplot as plt
income_sources = ['Salary', 'Freelance', 'Investments', 'Rental', 'Other']
monthly_income = [5000, 1500, 1000, 600, 400]
# Create a pie chart
plt.figure(figsize=(6,6))
plt.pie(monthly_income, labels=income_sources, autopct='%1.1f%%', colors=['lightcoral', 'lightskyblue', 'lightgreen', 'gold', 'violet'])
plt.title("Distribution of Monthly Income by Source")
plt.show()

Output:



