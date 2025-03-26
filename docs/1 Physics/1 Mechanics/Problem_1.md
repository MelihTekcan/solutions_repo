import numpy as np
import matplotlib.pyplot as plt

# Range calculation function
def projectile_range(v0, theta_deg, g=9.81, h=0):
    theta = np.radians(theta_deg)
    if h == 0:
        return (v0**2 * np.sin(2 * theta)) / g
    else:
        t_flight = (v0 * np.sin(theta) + np.sqrt((v0 * np.sin(theta))**2 + 2 * g * h)) / g
        return v0 * np.cos(theta) * t_flight

# Trajectory calculation function
def trajectory(v0, theta_deg, g=9.81, h=0):
    theta = np.radians(theta_deg)
    t_flight = (v0 * np.sin(theta) + np.sqrt((v0 * np.sin(theta))**2 + 2 * g * h)) / g
    t = np.linspace(0, t_flight, 100)
    x = v0 * np.cos(theta) * t
    y = h + v0 * np.sin(theta) * t - 0.5 * g * t**2
    return x, y

# Parameters
v0_values = [10, 20, 30]  # m/s
g_values = [9.81, 1.62]   # Earth, Moon
h_values = [0, 10]        # m
theta_deg = np.linspace(0, 90, 91)

# Plot 1: Range vs. Angle
fig1, ax1 = plt.subplots(figsize=(12, 8))
for v0 in v0_values:
    for g in g_values:
        for h in h_values:
            R = [projectile_range(v0, t, g, h) for t in theta_deg]
            label = f"v₀={v0} m/s, g={g} m/s², h={h} m"
            ax1.plot(theta_deg, R, label=label)
ax1.set_xlabel("Angle of Projection (degrees)")
ax1.set_ylabel("Range (m)")
ax1.set_title("Range vs. Angle for Various Parameters")
ax1.legend()
ax1.grid(True)
fig1.savefig("range_vs_angle.png", dpi=300, bbox_inches="tight")
plt.close(fig1)

# Plot 2: Trajectories
fig2, ax2 = plt.subplots(figsize=(12, 8))
v0, g, h = 20, 9.81, 0
angles = [15, 30, 45, 60, 75]
for theta in angles:
    x, y = trajectory(v0, theta, g, h)
    ax2.plot(x, y, label=f"θ={theta}°")
ax2.set_xlabel("Horizontal Distance (m)")
ax2.set_ylabel("Height (m)")
ax2.set_title(f"Trajectories (v₀={v0} m/s, g={g} m/s², h={h} m)")
ax2.legend()
ax2.grid(True)
ax2.set_ylim(bottom_ylim)
fig2.savefig("trajectories.png", dpi=300, bbox_inches="tight")
plt.close(fig2)

print("Plots saved as 'range_vs_angle.png' and 'trajectories.png'.")













