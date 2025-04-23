# Problem 3

## Trajectories of a Payload Released Near Earth


Analysis of Trajectories for a Payload Released Near Earth
This report investigates the trajectories of a payload released from a rocket near Earth, a fundamental problem in orbital mechanics with significant implications for space exploration. The objective was to analyze the possible paths—elliptical, parabolic, or hyperbolic—based on initial conditions, simulate these trajectories using Python, and relate the findings to practical applications such as satellite deployment and interplanetary missions. The study combines theoretical principles, numerical methods, and graphical visualization to provide a comprehensive understanding of the payload’s motion under Earth’s gravitational influence.
Introduction
When a payload is released from a rocket near Earth, its trajectory depends on its initial position, velocity, and the gravitational force exerted by Earth. This scenario is critical for designing space missions, including satellite launches, atmospheric reentry, and deep-space exploration. My goal was to explore how different initial velocities lead to distinct trajectories and to develop a computational model to visualize these paths. By integrating theoretical concepts with numerical simulations, this report aims to clarify the physics governing the payload’s motion and its relevance to real-world applications.
Theoretical Background
Gravitational Force
The motion of the payload is governed by Newton’s Law of Universal Gravitation, which describes the force between two masses as: $$ F = \frac{G M m}{r^2} $$

Where: 
- Gravitational constant: $$ G = 6.674 \times 10^{-11} \, \text{m}^3 \text{kg}^{-1} \text{s}^{-2} $$
- Earth’s mass: $$ M = 5.972 \times 10^{24} \, \text{kg} $$
- Payload’s mass: $$ m $$
- Distance from Earth’s center to the payload: $$ r $$

The resulting acceleration, independent of the payload’s mass, is: $$ a = \frac{G M}{r^2} $$ This acceleration, directed toward Earth’s center, determines the payload’s trajectory.
Equations of Motion
To model the payload’s motion, I adopted a two-dimensional Cartesian coordinate system with Earth at the origin. The payload’s position is denoted by $$ (x, y) $$, and its distance from Earth’s center is $$ r = \sqrt{x^2 + y^2} $$. The gravitational acceleration affects both coordinates, yielding the differential equations: $$ \ddot{x} = -\frac{G M x}{r^3}, \quad \ddot{y} = -\frac{G M y}{r^3} $$ These equations, which describe the payload’s position and velocity over time, were solved numerically due to their complexity.
Trajectory Types
The payload’s trajectory is determined by its specific mechanical energy, defined as: $$ \epsilon = \frac{v^2}{2} - \frac{G M}{r} $$ Where $$ v $$ is the payload’s speed. The energy classifies the trajectory as follows:

Elliptical ($$ \epsilon < 0 $$): A closed orbit around Earth, typical for satellites.
Parabolic ($$ \epsilon = 0 $$): An open path with zero velocity at infinity, representing the threshold for escape.
Hyperbolic ($$ \epsilon > 0 $$): An open path with positive velocity at infinity, indicating escape.

Escape Velocity
The escape velocity, the minimum speed required for the payload to escape Earth’s gravity, is: $$ v_{\text{esc}} = \sqrt{\frac{2 G M}{r}} $$ At an altitude of 200 km ($$ r \approx 6.571 \times 10^6 , \text{m} $$), the escape velocity is approximately 11.2 km/s, a key reference for analyzing the payload’s behavior.
Numerical Simulation
To study the payload’s motion, I developed a Python program using NumPy for numerical computations, SciPy for solving differential equations, and Matplotlib for visualization. The simulation models the payload’s trajectory starting at an altitude of 200 km with varying initial velocities to produce elliptical, parabolic, and hyperbolic paths.
Python Implementation
The following code simulates the payload’s motion and generates graphical outputs:

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
    r = np.sqrt(x**2 + y**2)  # Fixed typo: y^2 -> y**2
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

# Execute the simulation
simulate_trajectories()
```
# Execute simulation

Constants: The gravitational parameter ($$ \mu = G M $$) simplifies the equations by combining the gravitational constant and Earth's mass.
Equations: The equations function calculates the derivatives of position and velocity based on gravitational acceleration.
Energy: The specific_energy function determines the mechanical energy to classify the trajectory (elliptical, parabolic, or hyperbolic).
Simulation: The payload starts at 200 km altitude with initial velocities of 7.8 km/s (elliptical), 11.2 km/s (parabolic), and 15.0 km/s (hyperbolic). The simulation runs for 1 day (86,400 seconds).
Visualization: The plot shows Earth’s surface and the three trajectories, ensuring accurate representation with an equal aspect ratio.
Results and Discussion
Trajectories:

Elliptical (7.8 km/s): A closed orbit with negative specific energy, representing a bound state.
Parabolic (11.2 km/s): An open escape path with near-zero specific energy.
Hyperbolic (15.0 km/s): An open escape path with positive specific energy.
Applications:

Orbital Insertion: Elliptical trajectories are used for deploying satellites into Low Earth Orbit (e.g., Starlink).
Atmospheric Reentry: Steep elliptical paths lead to reentry, relevant for spacecraft like Apollo capsules.
Escape Trajectories: Hyperbolic paths enable interplanetary missions (e.g., Voyager).
Limitations and Future Work
Limitations:

Assumes 2D motion, neglecting Earth's rotation and 3D effects.
Ignores atmospheric drag and Earth’s oblateness.
Future Improvements:

Add 3D modeling, atmospheric drag, and external gravitational influences (e.g., Moon, Sun).
Develop interactive tools for dynamic trajectory exploration.
Conclusion
This study modeled elliptical, parabolic, and hyperbolic trajectories for a payload near Earth using Newton’s laws and numerical methods. The Python simulation demonstrated how initial velocity determines the trajectory, providing insights critical for satellite deployment, reentry, and interplanetary missions.
