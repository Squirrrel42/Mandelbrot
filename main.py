import numpy as np
import matplotlib.pyplot as plt

length = 200

re = np.linspace(-2, 2, length)
im = np.linspace(-2, 2, length)

img = np.zeros((length, length))

for i in range(length):
    for j in range(length):
        c = re[i] + im[j] * 1j

        z = 0
        for k in range(300):
            z = z ** 2 + c

            if(np.abs(z) > 2):
                img[j, i] = k
                break

plt.imshow(-img, cmap='flag')
plt.show()