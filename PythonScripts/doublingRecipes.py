# A31
# Doubling Recipes

import pandas as pd

recipe = input("Enter recipe name:")
dbl = pd.read_csv(recipe)

dbl['Amount'] *= 2

print("Double your recipe is:", dbl)