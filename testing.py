# try:
#     a = float(input("Enter first number: "))
#     b = float(input("Enter second number: "))
#     op = input("Enter operation (+, -, *, /): ")

#     if op == '+':
#         print(f"Result: {a + b}")
#     elif op == '-':
#         print(f"Result: {a - b}")
#     elif op == '*':
#         print(f"Result: {a * b}")
#     elif op == '/':
#         if b != 0:
#             print(f"Result: {a / b}")
#         else:
#             print("Error: Division by zero!")
#     else:
#         print("Invalid operation.")
# except ValueError:
#     print("Invalid input! Please enter numbers.")
from matplotlib import pyplot as plt
import numpy as np

# Generate 100 random data points along 3 dimensions
x, y, scale = np.random.randn(3, 100)
fig, ax = plt.subplots()

# Map each onto a scatterplot we'll create with Matplotlib
ax.scatter(x=x, y=y, c=scale, s=np.abs(scale)*500)
ax.set(title="Some random data, created with JupyterLab!")
plt.show()

