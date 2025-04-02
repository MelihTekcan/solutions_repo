import numpy as np
import matplotlib.pyplot as plt

# Parameters
g = 9.8  # Acceleration due to gravity (m/s^2)
v0_values = [10, 20, 30]  # Initial velocities (m/s)
theta_deg = np.linspace(0, 90, 91)  # Angles from 0° to 90°
theta_rad = np.deg2rad(theta_deg)

# Range function
def range_projectile(v0, theta, g):
    return (v0**2 * np.sin(2 * theta)) / g

# Compute ranges for different velocities
ranges = {v0: range_projectile(v0, theta_rad, g) for v0 in v0_values}

# Plot Range vs Angle
plt.figure(figsize=(10, 6))
for v0, R in ranges.items():
    plt.plot(theta_deg, R, label=f'v0 = {v0} m/s')
plt.xlabel('Angle of Projection (degrees)')
plt.ylabel('Range (meters)')
plt.title('Range vs. Angle of Projection')
plt.legend()
plt.grid(True)
plt.show()
