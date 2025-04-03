---
title: "Problem 2"
format: html
---

# Investigating the Dynamics of a Forced Damped Pendulum

## 1. Introduction
A **forced damped pendulum** is a fascinating physical system that reveals how simple components—like a swinging weight—can produce complex behaviors. Imagine a playground swing: left alone, it slows down due to air resistance (damping); push it rhythmically, and it keeps going (forcing). This interplay creates a rich mix of motion, from smooth swings to wild, unpredictable chaos. In this document, we’ll:

- Break down the physics step-by-step.
- Simulate the motion with Python.
- Explore real-world applications.

This system is key in fields like engineering (e.g., designing stable bridges) and science (e.g., modeling climate oscillations). Let’s dive in!

### Why Study This?
- **Damping**: Friction or air resistance reduces energy, mimicking real-world energy loss.
- **Forcing**: An external push adds energy, introducing new patterns like resonance or chaos.
- **Complexity**: Small tweaks can shift the pendulum from predictable to erratic motion.

## 2. Theoretical Foundation
The heart of this system is its equation of motion, which describes how the pendulum’s angle changes over time.

### 2.1. The Differential Equation
The motion is governed by:

$$ \frac{d^2\theta}{dt^2} + \frac{b}{m} \frac{d\theta}{dt} + \frac{g}{L} \sin(\theta) = A \cos(\omega t) $$

Here’s what each term means:
- $$ \theta $$ : Angle from vertical (in radians—e.g., 0 is straight down, $$ \pi/2 $$ is horizontal).
- $$ \frac{d^2\theta}{dt^2} $$ : Angular acceleration—how fast the swinging speeds up or slows down.
- $$ \frac{b}{m} \frac{d\theta}{dt} $$ : Damping force—friction proportional to speed ($$ \frac{d\theta}{dt} $$ is angular velocity).
- $$ \frac{g}{L} \sin(\theta) $$ : Restoring force—gravity pulling the pendulum back (g = 9.81 m/s², L = length).
- $$ A \cos(\omega t) $$ : External forcing—A is the push strength, $$ \omega $$ is the push frequency.

This equation is **nonlinear** because of $$ \sin(\theta) $$, meaning exact solutions are tough. It’s like a recipe with a tricky ingredient!

### 2.2. Small-Angle Approximation
For small swings (e.g., $$ \theta < 0.1 $$ radians, about 6°), $$ \sin(\theta) \approx \theta $$. This simplifies the equation to:

$$ \frac{d^2\theta}{dt^2} + \frac{b}{m} \frac{d\theta}{dt} + \frac{g}{L} \theta = A \cos(\omega t) $$

This is a **linear** equation, like a spring’s motion, and we can solve it. The solution has two parts:
1. **Transient**: Natural oscillations (frequency $$ \sqrt{\frac{g}{L}} $$) that fade due to damping.
2. **Steady-State**: Oscillations matching the forcing frequency ($$ \omega $$).

**Example**: If $$ L = 1 $$ m, the natural frequency is $$ \sqrt{9.81} \approx 3.13 $$ rad/s. Push at this rate, and you get **resonance**—big swings!

### 2.3. Resonance
Resonance occurs when $$ \omega \approx \sqrt{\frac{g}{L}} $$. The forcing adds energy perfectly in sync with the pendulum’s natural rhythm, amplifying swings. Think of pushing a child on a swing: time it right, and they soar; time it wrong, and they barely move.

## 3. Analysis of Dynamics
Let’s explore how parameters shape the pendulum’s dance.

### 3.1. Damping Coefficient (b/m)
- **Low Damping (e.g., b/m = 0.1)**: Swings last longer, fading slowly.
- **High Damping (e.g., b/m = 2.0)**: Motion stops quickly unless forcing is strong.

**Analogy**: Swing in air (low damping) vs. mud (high damping).

### 3.2. Forcing Amplitude (A)
- **Small A (e.g., 0.5)**: Gentle pushes—small, steady swings.
- **Large A (e.g., 5.0)**: Big pushes—wild swings or chaos if damping can’t balance it.

**Example**: A light tap vs. a hard shove on a swing.

### 3.3. Forcing Frequency ($$ \omega $$)
- **Low $$ \omega $$ (e.g., 0.5)**: Slow pushes—pendulum struggles to follow.
- **Near $$ \sqrt{\frac{g}{L}} $$**: Resonance—huge swings.
- **High $$ \omega $$ (e.g., 10)**: Fast jiggles—small, erratic motion.

### 3.4. Regular vs. Chaotic Motion
- **Regular**: Predictable swings (e.g., small A, $$ \omega $$ near natural frequency).
- **Chaotic**: Unpredictable wiggles (e.g., large A, mismatched $$ \omega $$). Chaos means tiny changes (like a 0.01 radian nudge) lead to totally different paths.

**Test**: With $$ A = 5 $$, $$ \omega = 1.5 $$, chaos emerges—see it below!

## 4. Practical Applications
This model isn’t just theoretical—it’s everywhere:
1. **Energy Harvesting**: Tiny pendulums in watches or sensors convert motion (e.g., walking) into power.
2. **Seismic Isolation**: Buildings use damped oscillators to absorb earthquake shakes.
3. **Mechanical Resonance**: Engineers avoid resonance in bridges (e.g., Tacoma Narrows collapse) or exploit it in musical instruments.

**Real Example**: The Millennium Bridge in London swayed due to crowd footsteps—a forced oscillation problem!

## 5. Implementation (Python Simulation)
Let’s simulate this with Python using **SciPy’s solve_ivp**. Below, we’ll plot the angle over time and a phase diagram for both regular and chaotic cases.

### Regular Motion Simulation
Here’s the simulation with moderate forcing (A = 1.2):

```{python}
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

def forced_damped_pendulum(t, y, b, m, g, L, A, omega):
    theta, omega_dot = y
    dtheta_dt = omega_dot
    domega_dt = -(b/m) * omega_dot - (g/L) * np.sin(theta) + A * np.cos(omega * t)
    return [dtheta_dt, domega_dt]

# Parameters
m = 1.0  # Mass (kg)
b = 0.5  # Damping coefficient
g = 9.81 # Gravity (m/s²)
L = 1.0  # Length (m)
A = 1.2  # Forcing amplitude
omega = 1.5  # Forcing frequency
y0 = [np.pi / 4, 0]  # Initial angle = 45°, velocity = 0

# Time setup
t_span = (0, 20)
t_eval = np.linspace(*t_span, 1000)

# Solve
sol = solve_ivp(forced_damped_pendulum, t_span, y0, t_eval=t_eval, args=(b, m, g, L, A, omega))

# Plotting
plt.figure(figsize=(12, 8))

# Time series
plt.subplot(2, 1, 1)
plt.plot(sol.t, sol.y[0], label="Angle (θ)")
plt.xlabel("Time (s)")
plt.ylabel("Angle (rad)")
plt.title("Regular Motion of a Forced Damped Pendulum (A = 1.2)")
plt.legend()

# Phase diagram
plt.subplot(2, 1, 2)
plt.plot(sol.y[0], sol.y[1], label="Phase Space")
plt.xlabel("Angle (θ)")
plt.ylabel("Angular Velocity (ω)")
plt.title("Phase Diagram")
plt.legend()

plt.tight_layout()
plt.show()