# Projectile Motion: Range Analysis

## 1. Theoretical Foundation

### Deriving the Governing Equations

Projectile motion involves an object launched with initial velocity \( v_0 \) at angle \( \theta \) under gravity \( g \), with no air resistance. Motion is split into:

- **Horizontal Motion**: \( x(t) = v_0 \cos(\theta) \cdot t \)
- **Vertical Motion**: \( y(t) = v_0 \sin(\theta) \cdot t - \frac{1}{2} g t^2 \)

The time of flight is given by:

\[
T = \frac{2 v_0 \sin(\theta)}{g}
\]

The range is calculated as:

\[
R = \frac{v_0^2 \sin(2\theta)}{g}
\]

---

## 2. Analysis of the Range

### Dependence on Angle of Projection

The range depends on the angle of projection \( \theta \), initial velocity \( v_0 \), and gravitational acceleration \( g \):

- Maximum range occurs at \( \theta = 45^\circ \).
- Range is symmetric: \( R(\theta) = R(90^\circ - \theta) \).
- Higher \( v_0 \) increases the range quadratically (\( R \propto v_0^2 \)).
- Lower \( g \) (e.g., on the Moon) significantly increases the range (\( R \propto 1/g \)).

![Range vs Angle Plot](range_vs_angle.png)

**Key Observations**: The plot confirms that the range peaks at \( \theta = 45^\circ \) and scales with \( v_0^2 \).

---

## 3. Practical Applications

### Real-World Scenarios

- **Sports**: Soccer and golf adjust \( \theta \) and \( v_0 \) for optimal range.
- **Engineering**: Artillery and rockets consider terrain and wind effects.
- **Astrophysics**: Spacecraft trajectories account for variable \( g \) and drag.

### Trajectory Example

The trajectory for \( v_0 = 20 \, \text{m/s} \) and \( \theta = 45^\circ \) is shown below:

![Projectile Trajectory](trajectory.png)

The parabolic path demonstrates the interplay between horizontal and vertical motion.

---

## 4. Implementation

The following Python script simulates and visualizes the range and trajectory of a projectile:

```python
import numpy as np
import matplotlib.pyplot as plt

# Parameters
g = 9.8  # m/s^2
v0_values = [10, 20, 30]  # m/s
theta_deg = np.linspace(0, 90, 91)  # 0° to 90°
theta_rad = np.deg2rad(theta_deg)

# Range function
def range_projectile(v0, theta, g):
    return (v0**2 * np.sin(2 * theta)) / g

# Compute ranges
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

# Trajectory (v0 = 20 m/s, θ = 45°)
v0 = 20
theta = np.deg2rad(45)
t_flight = (2 * v0 * np.sin(theta)) / g
t = np.linspace(0, t_flight, 100)
x = v0 * np.cos(theta) * ts
y = v0 * np.sin(theta) * t - 0.5 * g * t**2

plt.figure(figsize=(10, 6))
plt.plot(x, y, label='Trajectory (v0 = 20 m/s, θ = 45°)')
plt.xlabel('Horizontal Distance (m)')
plt.ylabel('Height (m)')
plt.title('Projectile Trajectory')
plt.legend()
plt.grid(True)
plt.show()