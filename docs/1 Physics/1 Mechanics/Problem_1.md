<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Projectile Motion: Range Analysis</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 20px;
            max-width: 900px;
            margin-left: auto;
            margin-right: auto;
        }
        h1, h2, h3 {
            color: #2c3e50;
        }
        h2 {
            border-bottom: 2px solid #3498db;
            padding-bottom: 5px;
        }
        pre {
            background-color: #f4f4f4;
            padding: 10px;
            border-radius: 5px;
            overflow-x: auto;
        }
        code {
            font-family: Consolas, monospace;
        }
        ul, ol {
            margin-left: 20px;
        }
        .section {
            margin-bottom: 20px;
        }
    </style>
</head>
<body>
    <h1>Investigating the Range as a Function of the Angle of Projection</h1>

    <div class="section">
        <h2>1. Theoretical Foundation</h2>
        <h3>Deriving the Governing Equations</h3>
        <p>Projectile motion involves an object launched with initial velocity v0 at angle θ under gravity g, with no air resistance. Motion is split into:</p>
        <ul>
            <li>Horizontal: ax = 0</li>
            <li>Vertical: ay = -g</li>
        </ul>
        <p>Initial velocity components:</p>
        <ul>
            <li>v0x = v0 cos(θ)</li>
            <li>v0y = v0 sin(θ)</li>
        </ul>
        <p>Position equations:</p>
        <ul>
            <li>x(t) = (v0 cos(θ)) t</li>
            <li>y(t) = (v0 sin(θ)) t - (1/2) g t^2</li>
        </ul>
        <p>Time of flight (y = 0):</p>
        <p>0 = (v0 sin(θ)) t - (1/2) g t^2</p>
        <p>Solutions: t = 0 or t = (2 v0 sin(θ)) / g (time of flight, T)</p>

        <h3>Range Equation</h3>
        <p>Range R = x(T):</p>
        <p>R = (v0 cos(θ)) * (2 v0 sin(θ)) / g = (2 v0^2 cos(θ) sin(θ)) / g</p>
        <p>Using 2 cos(θ) sin(θ) = sin(2θ):</p>
        <p>R = (v0^2 sin(2θ)) / g</p>

        <h3>Family of Solutions</h3>
        <p>R depends on v0, θ, and g, creating a family of solutions where:</p>
        <ul>
            <li>R ∝ v0^2</li>
            <li>θ affects R via sin(2θ)</li>
            <li>R ∝ 1/g</li>
        </ul>
    </div>

    <div class="section">
        <h2>2. Analysis of the Range</h2>
        <h3>Dependence on Angle of Projection</h3>
        <p>R = (v0^2 sin(2θ)) / g:</p>
        <ul>
            <li>R = 0 at θ = 0° and 90° (sin(0) = 0, sin(180°) = 0)</li>
            <li>Max R at θ = 45° (sin(90°) = 1): R_max = v0^2 / g</li>
            <li>Symmetry: R(θ) = R(90° - θ)</li>
        </ul>

        <h3>Influence of Other Parameters</h3>
        <ul>
            <li><strong>v0</strong>: R ∝ v0^2 (doubling v0 quadruples R)</li>
            <li><strong>g</strong>: R ∝ 1/g (e.g., Moon’s g ≈ 1.62 m/s^2 vs Earth’s 9.8 m/s^2 increases R ~6x)</li>
        </ul>
    </div>

    <div class="section">
        <h2>3. Practical Applications</h2>
        <h3>Real-World Scenarios</h3>
        <ul>
            <li><strong>Sports</strong>: Soccer/golf adjust θ and v0; 45° optimal without drag.</li>
            <li><strong>Engineering</strong>: Artillery/rockets consider terrain, wind.</li>
            <li><strong>Astrophysics</strong>: Spacecraft trajectories with variable g, drag.</li>
        </ul>

        <h3>Adaptations</h3>
        <ul>
            <li><strong>Uneven Terrain</strong>: Solve y(t) = h for t, adjust R.</li>
            <li><strong>Air Resistance</strong>: Use numerical methods (e.g., Runge-Kutta).</li>
        </ul>
    </div>

    <div class="section">
        <h2>4. Implementation</h2>
        <p>Python script to simulate and visualize range:</p>
        <pre><code>import numpy as np
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
x = v0 * np.cos(theta) * t
y = v0 * np.sin(theta) * t - 0.5 * g * t**2

plt.figure(figsize=(10, 6))
plt.plot(x, y, label='Trajectory (v0 = 20 m/s, θ = 45°)')
plt.xlabel('Horizontal Distance (m)')
plt.ylabel('Height (m)')
plt.title('Projectile Trajectory')
plt.legend()
plt.grid(True)
plt.show()
        </code></pre>
        <p><strong>Outputs:</strong></p>
        <ul>
            <li>Range vs. Angle: Peaks at 45°, scales with v0.</li>
            <li>Trajectory: Parabolic path for specific case.</li>
        </ul>
    </div>

    <div class="section">
        <h2>Deliverables</h2>
        <h3>Description of Solutions</h3>
        <p>R = (v0^2 sin(2θ)) / g defines the family of solutions. Trajectory: y(x) = x tan(θ) - (g x^2) / (2 v0^2 cos^2(θ)).</p>

        <h3>Graphical Representations</h3>
        <p>Plots confirm max at 45° and v0^2 scaling.</p>

        <h3>Limitations and Extensions</h3>
        <ul>
            <li><strong>Idealizations</strong>: No drag, flat terrain, constant g.</li>
            <li><strong>Improvements</strong>: Add drag (F_d ∝ -v^2), wind effects via numerical solvers.</li>
        </ul>
    </div>

    <p><em>Note: For proper math rendering (e.g., superscripts), include MathJax in the head section.</em></p>
</body>
</html>


