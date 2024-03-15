# A24
# Topo Map: generates a topographic map visualization based on elevation data loaded from file elevationsNYC.txt

import numpy as np
import matplotlib.pyplot as plt

bclr = float(input('How blue is the ocean: '))  # 0.5
floodMap = input('Enter a saving location: ')   # topoMedBlue.png


elevations = np.loadtxt('elevationsNYC.txt')

mapShape = elevations.shape + (3,)
floodMap = np.zeros(mapShape)

for row in range(mapShape[0]):
    for col in range(mapShape[1]):
        if elevations[row, col] <= 0:
            floodMap[row, col, 2] = bclr

        elif elevations[row, col] % 10 == 0:
            floodMap[row, col, :] = 0

        else:
            floodMap[row, col, :] = 1

plt.imsave("topoMedBlue.png", floodMap)