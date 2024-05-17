import matplotlib.pyplot as plt
import numpy as np

# Generate x values
x = np.linspace(-10, 10, 1000)
x = x[x !=0]

# Calculate y values using the equation 
y = np.cos(x) / (5*x)

# Create the plot
plt.figure(figsize=(8, 6))
plt.plot(x, y, label='$y =\\frac{{\\cos(x)}}{{5x}}$', color='b', linewidth=2)
plt.axhline(y=0, color='y')
plt.axvline(x=0, color='y')
plt.title('Plot of $y =\\frac{{\\cos(x)}}{{5x}}$')
plt.xlabel('x', color='y')
plt.ylabel('y', color='g')
plt.grid(True)
plt.legend()
plt.show()