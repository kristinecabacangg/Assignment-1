import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-5, 5, 100)

y = x**2 + x + 10 / 2*x

plt.figure(figsize=(8, 6))
plt.plot(x, y, label='$y = \\frac{{x^2 + x + 10 }}{{2x}}$', color='b', linewidth=2)
plt.axhline(y=0, color='y')
plt.axvline(x=0, color='y')
plt.title('Plot of $y = \\frac{{x^2 + x + 10 }}{{2x}}$')
plt.xlabel('x', color='y')
plt.ylabel('y', color='g')
plt.grid(True)
plt.legend()
plt.show()