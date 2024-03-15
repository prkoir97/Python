# A32
# Shelter Census

import pandas as pd
import matplotlib.pyplot as plt

census = input('Enter name of input file: ')        # shelter.DHS_Daily_Report.csv
output = input('Enter name of output file: ')       # shelter.dhsPlot.png

# Read the census data from the input file into a DataFrame using Pandas
homeless = pd.read_csv(census)

# Calculate the fraction of children in shelters and add it as a new column in the DataFrame
homeless['Fraction Children'] = homeless['Total Children in Shelter'] / homeless['Total Individuals in Shelter']

# Plot the fraction of children in shelters over time
homeless.plot(x = "Date of Census", y = "Fraction Children")

# Get the current figure (plot) and save it to the specified output file
fig = plt.gcf()
fig.savefig(output)
