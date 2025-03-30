import numpy as np
import matplotlib.pyplot as plt

def r1(t):
    return np.array([t, -t**2 + t])

def r2(t):
    return np.array([2 * np.cos(t), 2 * np.sin(t)])

# Define the time ranges
t1 = np.linspace(0, 2, 100)
t2 = np.linspace(0, 2 * np.pi, 100)

# Create a side-by-side plot layout
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(12, 5))  # One row, two columns

# First plot
axes[0].plot(r1(t1)[0], r1(t1)[1])
axes[0].set_xlabel('x')
axes[0].set_ylabel('y')
axes[0].set_title('Plot 1: r1(t)')

# Second plot
axes[1].plot(r2(t2)[0], r2(t2)[1])
axes[1].set_xlabel('x')
axes[1].set_ylabel('y')
axes[1].set_title('Plot 2: r2(t)')

# Adjust aspect ratios if needed
axes[0].set_aspect('equal', 'box')
axes[1].set_aspect('equal', 'box')

# Optimize layout
plt.tight_layout()
plt.show()




def r(t):
    return np.array([t, -t**2 + t])

def v(t):
    return np.array([1, -2*t + 1])

t = np.linspace(0, 10, 100)

fig, axes = plt.subplots(figsize=(8, 6))

# whole curve
axes.plot(r(t)[0], r(t)[1], label='r(t)')

# velocity vector at t=3
axes.quiver(r(3)[0], r(3)[1], v(3)[0], v(3)[1], angles='xy', scale_units='xy', scale=1, color='red', label='v(3)')
axes.text(r(3)[0] + v(3)[0], r(3)[1] + v(3)[1], 'v(3)', color='red')
#velocity vector at t=6
axes.quiver(r(6)[0], r(6)[1], v(6)[0], v(6)[1], angles='xy', scale_units='xy', scale=1, color='blue', label='v(6)')
axes.text(r(6)[0] + v(6)[0], r(6)[1] + v(6)[1], 'v(6)', color='blue')

axes.set_xlabel('x')
axes.set_ylabel('y')
axes.legend()
plt.show()


def r(t):
    return np.array([t, -t**2 + t])

def v(t):
    return np.array([1, -2*t + 1])

def a(t):
    return np.array([0, -2])

t = np.linspace(0, 4, 100)

fig, axes = plt.subplots(figsize=(8, 6))

# whole curve
axes.plot(r(t)[0], r(t)[1], label='r(t)')
# velocity vector at t=3
axes.quiver(r(3)[0], r(3)[1], v(3)[0], v(3)[1], angles='xy', scale_units='xy', scale=1, color='red', label='v(3)')
axes.text(r(3)[0] + v(3)[0], r(3)[1] + v(3)[1], 'v(3)', color='red')
# acceleration vector at t=3
axes.quiver(r(3)[0], r(3)[1], a(3)[0], a(3)[1], angles='xy', scale_units='xy', scale=1, color='blue', label='a(3)')
axes.text(r(3)[0] + a(3)[0], r(3)[1] + a(3)[1], 'a(3)', color='blue')

axes.set_xlabel('x')
axes.set_ylabel('y')
axes.legend()
plt.show()