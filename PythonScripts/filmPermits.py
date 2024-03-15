# A36
# Film Permits

import pandas as pd

# Prompt the user to enter the name of the CSV file containing permit data
file = input('Enter file name: ')       # filmPermitsJune2019.csv

# Read the CSV file into a DataFrame
permit = pd.read_csv(file)

# Calculate the total number of permits
amount = permit['EventID'].size

# Print the total number of permits
print(f"\nThere were {amount} film permits.\n")

# Print the count of permits by borough
print(permit["Borough"].value_counts().to_string(), end="\n")

# Print the header for the five most popular filming locations
print("\nThe five most popular filming locations were: ")

# Iterate over the top five most common values in 'ParkingHeld' column and print them
for location, count in permit['ParkingHeld'].value_counts().head(5).items():
    print(f"{location:<120}{count}")
