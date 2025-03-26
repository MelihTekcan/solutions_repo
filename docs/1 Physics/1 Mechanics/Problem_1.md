import numpy as np
import matplotlib.pyplot as plt
import base64
from io import BytesIO

# Range calculation function
def projectile_range(v0, theta_deg, g=9.81, h=0):
    theta = np.radians(theta_deg)
    if h == 0:
        return (v0**2 * np.sin(2 * theta)) / g
    else:
        t_flight = (v0 * np.sin(theta) + np.sqrt((v0 * np.sin(theta))**2 + 2 * g * h)) / g
        return v0 * np.cos(theta) * t_flight

# Trajectory calculation for plotting
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

# Generate HTML content
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Projectile Motion Analysis</title>
    <style>
        body {font-family: Arial, sans-serif; margin: 20px;}
        h1, h2 {color: #2c3e50;}
        img {max-width: 100%; height: auto;}
        p {line-height: 1.6;}
    </style>
</head>
<body>
    <h1>Investigating the Range as a Function of the Angle of Projection</h1>
    <h2>1. Theoretical Foundation</h2>
    <p>The governing equations are derived from Newton's laws:</p>
    <ul>
        <li>Horizontal: x(t) = v₀ cos(θ) t</li>
        <li>Vertical: y(t) = h + v₀ sin(θ) t - (1/2) g t²</li>
        <li>Range (h=0): R = (v₀² sin(2θ)) / g</li>
    </ul>
"""

# Plot 1: Range vs. Angle for different v0, g, h
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
buf1 = BytesIO()
fig1.savefig(buf1, format="png")
img1_str = base64.b64encode(buf1.getvalue()).decode("utf-8")
buf1.close()
plt.close(fig1)

html_content += f"""
    <h2>2. Analysis of the Range</h2>
    <p>The plot below shows how range varies with angle for different initial velocities (v₀), gravitational accelerations (g), and heights (h):</p>
    <img src="data:image/png;base64,{img1_str}" alt="Range vs Angle">
    <p><b>Observations:</b></p>
    <ul>
        <li>Maximum range at 45° for h = 0.</li>
        <li>Higher v₀ quadratically increases range.</li>
        <li>Lower g (e.g., Moon) extends range significantly.</li>
        <li>Non-zero h shifts the optimal angle slightly below 45°.</li>
    </ul>
"""

# Plot 2: Trajectories for selected angles
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
buf2 = BytesIO()
fig2.savefig(buf2, format="png")
img2_str = base64.b64encode(buf2.getvalue()).decode("utf-8")
buf2.close()
plt.close(fig2)

html_content += f"""
    <h2>3. Practical Applications</h2>
    <p>Trajectories for v₀ = 20 m/s on Earth (g = 9.81 m/s²):</p>
    <img src="data:image/png;base64,{img2_str}" alt="Trajectories">
    <p><b>Applications:</b></p>
    <ul>
        <li><b>Sports</b>: Golf shots optimize low angles with spin.</li>
        <li><b>Engineering</b>: Artillery adjusts for elevation.</li>
        <li><b>Astrophysics</b>: Mars rovers consider g = 3.72 m/s².</li>
    </ul>
    <h2>4. Limitations and Extensions</h2>
    <p>This model assumes no air resistance or wind. To include drag:</p>
    <ul>
        <li>Add F_d = -k v² and solve numerically.</li>
        <li>Use Runge-Kutta methods for accuracy.</li>
    </ul>
</body>
</html>
"""

# Save HTML
with open("projectile_analysis_detailed.html", "w") as f:
    f.write(html_content)

print("Detailed HTML file 'projectile_analysis_detailed.html' has been generated.")














