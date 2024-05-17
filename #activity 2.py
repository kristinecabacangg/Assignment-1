import matplotlib.pyplot as plt
import numpy as np

# Generate x values
x = np.linspace(-5, 5, 100)

# Calculate y values using the equation \(y = x^3 + x - 100\)
y = x**3 + x - 100

# Create the plot
plt.figure(figsize=(8, 6))
plt.plot(x, y, label='$y = x^3 + x - 100$', color='b', linewidth=2)
plt.title('Plot of $y = x^3 + x - 100$')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.legend()
plt.show()