import numpy as np
import matplotlib.pyplot as plt

# Physical constants
g = 9.81  # Gravity (m/s^2)
v0_values = [10, 20, 30]  # Initial velocities (m/s)
angles = np.linspace(0, 90, 100)  # Angles from 0° to 90°
time_steps = np.linspace(0, 5, 500)  # Time intervals

# Function to calculate range
def calculate_range(v0, theta, g):
    theta_rad = np.radians(theta)
    return (v0**2 * np.sin(2*theta_rad)) / g

# Create a figure for multiple plots
plt.figure(figsize=(12, 8))

#Range vs. Launch Angle**
plt.subplot(2, 2, 1)
for v0 in v0_values:
    ranges = [calculate_range(v0, theta, g) for theta in angles]
    plt.plot(angles, ranges, label=f"v0 = {v0} m/s")
plt.xlabel("Launch Angle (°)")
plt.ylabel("Range (m)")
plt.title("Range vs. Launch Angle")
plt.legend()
plt.grid(True)

#Height vs. Time**
plt.subplot(2, 2, 2)
for v0 in v0_values:
    t_max = (2 * v0 * np.sin(np.radians(45))) / g  # Total flight time at 45°
    t_vals = np.linspace(0, t_max, 100)
    y_vals = v0 * np.sin(np.radians(45)) * t_vals - 0.5 * g * t_vals**2
    plt.plot(t_vals, y_vals, label=f"v0 = {v0} m/s")
plt.xlabel("Time (s)")
plt.ylabel("Height (m)")
plt.title("Height vs. Time")
plt.legend()
plt.grid(True)

#Effect of Air Resistance on Range**
plt.subplot(2, 2, 3)
def range_with_air_resistance(v0, theta, g, k=0.1, m=1):
    theta_rad = np.radians(theta)
    vx = v0 * np.cos(theta_rad)
    vy = v0 * np.sin(theta_rad)
    dt = 0.01  # Small time step
    x, y = 0, 0
    while y >= 0:
        ax = -k/m * vx  # Air resistance (x direction)
        ay = -g - (k/m) * vy  # Air resistance (y direction)
        vx += ax * dt
        vy += ay * dt
        x += vx * dt
        y += vy * dt
    return x

ranges_no_air = [calculate_range(20, theta, g) for theta in angles]
ranges_air = [range_with_air_resistance(20, theta, g) for theta in angles]

plt.plot(angles, ranges_no_air, label="No Air Resistance", linestyle="dashed")
plt.plot(angles, ranges_air, label="With Air Resistance (k=0.1)", color="red")
plt.xlabel("Launch Angle (°)")
plt.ylabel("Range (m)")
plt.title("Effect of Air Resistance on Range")
plt.legend()
plt.grid(True)

#Range on Different Planets**
plt.subplot(2, 2, 4)
planets = {"Earth": 9.81, "Moon": 1.62, "Mars": 3.71}
for planet, g_planet in planets.items():
    ranges = [calculate_range(20, theta, g_planet) for theta in angles]
    plt.plot(angles, ranges, label=f"{planet}")
plt.xlabel("Launch Angle (°)")
plt.ylabel("Range (m)")
plt.title("Range on Different Planets")
plt.legend()
plt.grid(True)

#Show all plots
plt.tight_layout()
plt.show()
















