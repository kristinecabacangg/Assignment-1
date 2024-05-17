import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10, 10, 1000)

y = x**2 - 10

plt.figure(figsize=(8, 6))
plt.plot(x, y, label='$y = x^2 - 10$', color='b', linewidth=2)
plt.axhline(y=0, color='y')
plt.axvline(x=0, color='y')
plt.title('Plot of $y = x^2 - 10$')
plt.xlabel('x', color='y')
plt.ylabel('y', color='g')
plt.grid(True)
plt.legend()
plt.show()