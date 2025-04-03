#---
title: "Problem 2:"
format: html
---

# Problem 2

## Investigating the Dynamics of a Forced Damped Pendulum

## 1. Introduction

A **forced damped pendulum** is a fascinating physical system that reveals how simple components—like a swinging weight—can produce complex behaviors. Imagine a playground swing: left alone, it slows down due to air resistance (damping); push it rhythmically, and it keeps going (forcing). This interplay creates a rich mix of motion, from smooth swings to wild, unpredictable chaos.

---

## 2. Theoretical Foundation

The motion of a forced damped pendulum is governed by the following differential equation:

$$ \frac{d^2\theta}{dt^2} + \frac{b}{m} \frac{d\theta}{dt} + \frac{g}{L} \sin(\theta) = A \cos(\omega t) $$

Where:
- $$ \theta $$: Angle from vertical (in radians).
- $$ \frac{d^2\theta}{dt^2} $$: Angular acceleration.
- $$ \frac{b}{m} \frac{d\theta}{dt} $$: Damping force proportional to angular velocity.
- $$ \frac{g}{L} \sin(\theta) $$: Restoring force due to gravity.
- $$ A \cos(\omega t) $$: External forcing term.

---

## 3. Python Simulation

Below is the Python code to simulate the motion of the forced damped pendulum. The simulation includes:
1. A time series plot showing the angle of the pendulum over time.
2. A phase diagram showing the relationship between angle and angular velocity.

### Regular Motion Simulation
This simulation uses a moderate forcing amplitude (A = 1.2):

```{python}
# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Define the forced damped pendulum equation
def forced_damped_pendulum(t, y, b, m, g, L, A, omega):
    theta, omega_dot = y
    dtheta_dt = omega_dot
    domega_dt = -(b/m) * omega_dot - (g/L) * np.sin(theta) + A * np.cos(omega * t)
    return [dtheta_dt, domega_dt]

# Parameters
m = 1.0  # Mass (kg)
b = 0.5  # Damping coefficient
g = 9.81  # Gravity (m/s²)
L = 1.0  # Length of pendulum (m)
A = 1.2  # Forcing amplitude
omega = 1.5  # Forcing frequency
y0 = [np.pi / 4, 0]  # Initial angle = 45°, velocity = 0

# Time setup
t_span = (0, 20)  # Simulate for 20 seconds
t_eval = np.linspace(*t_span, 1000)  # Time points for evaluation

# Solve the differential equation
sol = solve_ivp(forced_damped_pendulum, t_span, y0, t_eval=t_eval, args=(b, m, g, L, A, omega))

# Plotting the results
plt.figure(figsize=(12, 8))

# Time series plot (angle vs. time)
plt.subplot(2, 1, 1)
plt.plot(sol.t, sol.y[0], label="Angle (θ)")
plt.xlabel("Time (s)")
plt.ylabel("Angle (rad)")
plt.title("Motion of a Forced Damped Pendulum")
plt.legend()
plt.grid(True)

# Phase diagram (angle vs. angular velocity)
plt.subplot(2, 1, 2)
plt.plot(sol.y[0], sol.y[1], label="Phase Space")
plt.xlabel("Angle (θ)")
plt.ylabel("Angular Velocity (ω)")
plt.title("Phase Diagram")
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()