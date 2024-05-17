import matplotlib.pyplot as plt
import numpy as np
def f(x):
  return (x+2)*(x+3)*(x-4)
x = np.linspace(-5, 5, 100)  
y = f(x)
plt.plot(x, y)
plt.grid(True, color='m')
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Graph of f(x)=(x+2)(x+3)(x-4)")
plt.axhline(y=0, color="k")
plt.axvline(x=0, color="k")
plt.show()