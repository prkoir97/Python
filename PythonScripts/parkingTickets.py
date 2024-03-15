# A35
# Parking Tickets

import pandas as pd

# Prompt the user to enter the name of the CSV file
csvFile = input('Enter file name: ')

# Prompt the user to enter the name of the attribute/column
attr = input('Enter attribute: ')

# Read the CSV file into a DataFrame
tickets = pd.read_csv(csvFile)

print("The 10 worst offenders are: ")

# Calculate the count of occurrences for each unique value in the specified attribute/column
# Then, print the 10 most common values
print(tickets[attr].value_counts()[:10])