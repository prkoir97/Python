# A27
# Borough Stats

import matplotlib.pyplot as plt
import pandas as pd

# Prompting the user to input the borough name
borough = input('Enter Borough: ')

# Loading historical population data from a CSV file using Pandas
pop = pd.read_csv('nycHistPop.csv', skiprows=5, encoding='latin1')

# Filter the population data for the specified borough
borough_data = pop[['Year', borough]]

# Plotting the population data for the specified borough over the years
borough_data.plot(x="Year", y=borough)

# Adding labels and a title to the plot
plt.xlabel("Year")
plt.ylabel("Population")
plt.title(f"Population Trend for {borough}")

# Displaying the plot on the screen
plt.show()

# Calculating and printing the minimum, average, and maximum population for the specified borough
print("Minimum population:", borough_data[borough].min())
print("Average population:", borough_data[borough].mean())
print("Maximum population:", borough_data[borough].max())