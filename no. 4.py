import matplotlib.pyplot as plt
import numpy as np

# Generate x values
x = np.linspace(-5, 5, 100)

# Calculate y values using the equation \(y = x^4 +x^3 + x^2 + x + 1\)
y = x**4 + x**3 + x**2 + x + 1

# Create the plot
plt.figure(figsize=(8, 6))
plt.plot(x, y, label='$y = x^4 +x^3 + x^2 + x + 1$', color='b', linewidth=2)
plt.title('Plot of $y = x^4 +x^3 + x^2 + x + 1$')
plt.xlabel('x', color='y')
plt.ylabel('y', color='g')
plt.grid(True)
plt.legend()
plt.show()