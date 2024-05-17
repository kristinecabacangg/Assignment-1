import matplotlib.pyplot as plt
import numpy as np

# Generate x values
x = np.linspace(-5, 5, 100)

# Calculate y values using the equation \(x^10 - x^8 + x^2 - 8\)
y = x**10 - x**8 + x**2 - 8

# Create the plot
plt.figure(figsize=(8, 6))
plt.plot(x, y, label='$y = x^10 - x^8 + x^2 - 8$', color='b', linewidth=2)
plt.title('Plot of $y = x^10 - x^8 + x^2 - 8$')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.legend()
plt.show()