# A14
# CUNY Logo

import matplotlib.pyplot as plt
import numpy as np

logoImg = np.ones((30,30,3))

logoImg[:10,:,0:2] = 0
logoImg[10:20,0:10,0:2] = 0
logoImg[20:,:,0:2] = 0
plt.imshow(logoImg)
plt.show()
plt.imsave("logo.png", logoImg)