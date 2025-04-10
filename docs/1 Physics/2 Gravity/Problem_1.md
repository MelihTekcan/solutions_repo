# Problem 1

## 1. Introduction

Kepler's Third Law is fundamental to planetary motion and crucial for understanding gravitational theory in practice. This document presents the derivation of the relationship **"The square of the orbital period (T²) is proportional to the cube of the orbital radius (R³)"** for circular orbits, its astronomical significance, and verification through computational simulation.

---

## 2. Physical Derivation: Kepler's Third Law

### 2.1 Basic Assumptions
- **Circular Orbit**: For simplicity, we assume a planet/satellite moves in a perfect circular orbit.
- **Centripetal Force**: The gravitational force provides the necessary centripetal force for circular motion.

### 2.2 Mathematical Steps

**Step 1: Newton's Law of Gravitation and Centripetal Force Balance**  
For a planet (m) orbiting a star (M):

$$
F_{\text{grav}} = F_{\text{centripetal}}
$$

$$
G \frac{M m}{R^2} = m \left( \frac{v^2}{R} \right)
$$

Where:
- $G$: Gravitational constant ($6.674 \times 10^{-11} \ \text{m}^3 \ \text{kg}^{-1} \ \text{s}^{-2}$)
- $v$: Orbital velocity
- $R$: Orbital radius

**Step 2: Velocity-Period Relationship**  
For a circular orbit, the period (T) is the time for one complete revolution:

$$
v = \frac{\text{Circumference}}{\text{Period}} = \frac{2 \pi R}{T}
$$

**Step 3: Substitution and Simplification**  
Substituting Step 2 into Step 1:

$$
G \frac{M}{R^2} = \frac{(2 \pi R / T)^2}{R}
$$

Simplifying:

$$
G M = \frac{4 \pi^2 R^3}{T^2}
$$

Finally:

$$
T^2 = \frac{4 \pi^2}{G M} R^3
$$

This is the mathematical expression of **Kepler's Third Law**. Combining constants:

$$
T^2 \propto R^3
$$

---

## 3. Astronomical Significance and Applications

### 3.1 Calculating Planetary Masses
- **Example**: The Sun's mass can be calculated using Earth's orbital period (1 year) and radius (1 AU):

$$
M_{\text{Sun}} = \frac{4 \pi^2 (1 \, \text{AU})^3}{G (1 \, \text{year})^2}
$$

### 3.2 Satellite Orbits
- **Moon's Orbit**: The Earth's mass can be derived from the Moon's period (27.3 days) and orbital radius (384,400 km).

### 3.3 Exoplanet Research
- **Doppler Spectroscopy**: A star's oscillation period and velocity reveal an exoplanet's orbital radius.

---

## 4. Computational Modeling: Python Simulation

The Python code below calculates orbital periods for different radii and verifies the $$ T^2 $$ vs $$ R^3 $$ relationship.

```python
import numpy as np
import matplotlib.pyplot as plt

# Constants
G = 6.67430e-11  # Gravitational constant (m^3 kg^-1 s^-2)
M = 5.972e24     # Earth's mass (kg)

# Orbital radii (from 1e6 m to 1e7 m)
R = np.linspace(1e6, 1e7, 100)

# Calculate orbital period (T) using Kepler's Third Law
T = np.sqrt((4 * np.pi**2 * R**3) / (G * M))

# Plot T^2 vs R^3
plt.figure(figsize=(10, 6))
plt.plot(R**3, T**2, 'b-', label='Simulation Data')
plt.xlabel('Orbital Radius Cubed (R³) [m³]')
plt.ylabel('Orbital Period Squared (T²) [s²]')
plt.title('Verification of Kepler\'s Third Law')
plt.grid(True)
plt.legend()
plt.show()