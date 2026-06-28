


import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# 1. Basic Python test
# -----------------------------
print("Python is working ✔")

# -----------------------------
# 2. NumPy test
# -----------------------------
x = np.random.randint(1, 7, 10000)
print("NumPy mean (should be ~3.5):", np.mean(x))

# -----------------------------
# 3. Simple physics-style simulation
# Random walk (1D)
# -----------------------------
steps = 1000
position = 0
positions = []

for _ in range(steps):
    step = np.random.choice([-1, 1])
    position += step
    positions.append(position)

# -----------------------------
# 4. Plot result
# -----------------------------
plt.plot(positions)
plt.title("1D Random Walk Simulation")
plt.xlabel("Step")
plt.ylabel("Position")
plt.show()