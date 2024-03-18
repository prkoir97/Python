# A15
# Flood Map: creates flood map for NYC

import numpy as np
import matplotlib.pyplot as plt

elevations = np.loadtxt('elevationsNYC.txt')

# Create an empty flood map with the same shape as the elevation data
mapShape = elevations.shape + (3,)            # Add additional dimension for color channels (RGB)
floodMap = np.zeros(mapShape)

for row in range(mapShape[0]):
    for col in range(mapShape[1]):               # Check elevation levels and assign colors accordingly
        if elevations[row, col] <= 0:            # Below sea level, set to blue for water
            floodMap[row, col, 2] = 1.0

        elif elevations[row, col] <= 6:          # Between 0 and 6 feet, set to red for potential flood risk
            floodMap[row, col, 0] = 1.0

        elif elevations[row, col] <= 20:         # Between 6 and 20 feet, set to gray at 50% for lower risk areas
            floodMap[row, col, :] = 0.5

        else:                                    # Above 20 feet, set to green for higher ground
            floodMap[row, col, 1] = 1.0

plt.imsave('floodMap.png', floodMap)
