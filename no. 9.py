import matplotlib.pyplot as plt
import numpy as np

# Generate x values
x = np.linspace(-10, 10, 1000)
x = x[x !=0]

# Calculate y values using the equation 
y = (x**3 / (2*x)) - 10 * x

# Create the plot
plt.figure(figsize=(8, 6))
plt.plot(x, y, label='$y = \\frac{{x^3}}{{2x}} - 10x$', color='b', linewidth=2)
plt.title('Plot of $y = \\frac{{x^3}}{{2x}} - 10x$')
plt.xlabel('x', color='y')
plt.ylabel('y', color='g')
plt.grid(True)
plt.legend()
plt.show()