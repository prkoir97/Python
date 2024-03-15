# A26
# Borough Graph

import matplotlib.pyplot as plt
import pandas as pd

# Prompting the user to input the borough name and the output file name
brgh = input('Enter borough name: ')
brgh2 = input('Enter output file name: ')

# Loading historical population data from a CSV file using Pandas
pop = pd.read_csv('nycHistPop.csv', skiprows=5, encoding='ISO-8859-1')

# Calculating the fraction of the population of the specified borough compared to the total population for each year
pop['Fraction'] = pop[brgh] / pop['Total']

# Plotting the calculated fraction over the years
pop.plot(x='Year', y='Fraction')

# Saving the generated plot as an image file with the specified output file name
fig = plt.gcf()  # Get current figure
fig.savefig(brgh2)  # Save the figure as the specified file

# Displaying the plot on the screen
fig.savefig(brgh2)  # Save the figure as a PNG file


