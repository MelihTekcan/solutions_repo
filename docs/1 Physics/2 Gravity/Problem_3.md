# Problem 3 
## Payload Trajectories Near Earth

This report analyzes the trajectories of a payload released from a rocket near Earth. It explores elliptical, parabolic, and hyperbolic paths based on initial conditions. Python simulations visualize these trajectories, relating them to applications like satellite deployment and interplanetary missions.

**Theoretical Background:**

- **Gravitational Force:**  The motion is governed by Newton's Law of Universal Gravitation: $F = \frac{G M m}{r^2}$, where:
    -  \(G\) is the gravitational constant.
    -  \(M\) is Earth's mass.
    -  \(m\) is the payload's mass.
    -  \(r\) is the distance between Earth and the payload.
- **Equations of Motion:** To model the motion, we use a 2D Cartesian coordinate system, resulting in:
    $\ddot{x} = -\frac{G M x}{r^3}, \quad \ddot{y} = -\frac{G M y}{r^3}$
- **Trajectory Types:** Determined by the specific mechanical energy: $\epsilon = \frac{v^2}{2} - \frac{G M}{r}$
    - Elliptical ($\epsilon < 0$): Closed orbit.
    - Parabolic ($\epsilon = 0$): Escape threshold.
    - Hyperbolic ($\epsilon > 0$): Escape trajectory.
- **Escape Velocity:** The minimum speed to escape Earth's gravity: $v_{\text{esc}} = \sqrt{\frac{2 G M}{r}}$ (approximately 11.2 km/s at 200 km altitude).

**Python Implementation:**

```python

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Physical constants
G = 6.67430e-11  # Gravitational constant (m^3 kg^-1 s^-2)
M = 5.972e24     # Earth’s mass (kg)
R_E = 6.371e6    # Earth’s radius (m)
mu = G * M       # Gravitational parameter (m^3 s^-2)

# Equations of motion
def equations(t, state):
    x, y, vx, vy = state
    r = np.sqrt(x**2 + y**2)
    ax = -mu * x / r**3
    ay = -mu * y / r**3
    return [vx, vy, ax, ay]

# Specific mechanical energy
def specific_energy(x, y, vx, vy):
    r = np.sqrt(x**2 + y**2)
    v = np.sqrt(vx**2 + vy**2)
    return 0.5 * v**2 - mu / r

# Simulate trajectories
def simulate_trajectories():
    # Initial conditions: 200 km altitude
    altitude = 200e3
    r0 = R_E + altitude
    x0, y0 = 0, r0
    
    # Time span: 1 day (86,400 seconds)
    t_span = (0, 86400)
    t_eval = np.linspace(0, 86400, 1000)
    
    # Initial velocities for different trajectories
    velocities = [
        (0, 7.8e3, "Elliptical"),  # Sub-escape velocity
        (0, 11.2e3, "Parabolic"),  # Escape velocity
        (0, 15.0e3, "Hyperbolic")  # Above escape velocity
    ]
    
    plt.figure(figsize=(10, 8))
    
    # Plot Earth’s surface
    theta = np.linspace(0, 2 * np.pi, 100)
    x_earth = R_E * np.cos(theta)
    y_earth = R_E * np.sin(theta)
    plt.plot(x_earth, y_earth, 'b-', label="Earth")
    
    # Simulate and plot each trajectory
    for vx0, vy0, label in velocities:
        state0 = [x0, y0, vx0, vy0]
        sol = solve_ivp(equations, t_span, state0, t_eval=t_eval, method='RK45')
        
        plt.plot(sol.y[0], sol.y[1], label=f"{label} (v = {np.sqrt(vx0**2 + vy0**2)/1e3:.1f} km/s)")
        
        # Compute and display energy
        energy = specific_energy(x0, y0, vx0, vy0)
        print(f"{label} trajectory: Specific energy = {energy:.2e} J/kg")
    
    plt.xlabel("X (m)")
    plt.ylabel("Y (m)")
    plt.title("Trajectories of a Payload Near Earth")
    plt.legend()
    plt.grid(True)
    plt.axis("equal")
    plt.savefig("trajectories.png")
    plt.show()

simulate_trajectories()

```