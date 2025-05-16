# Problem 1

## **1. Introduction**

Kepler's Third Law is one of the most important principles in celestial mechanics. It describes the relationship between the orbital period of a planet (or satellite) and its orbital radius. This law is fundamental for understanding planetary motion, satellite dynamics, and even exoplanet detection.

### **What Does Kepler's Third Law State?**
Kepler's Third Law states:
> **"The square of the orbital period (T²) is proportional to the cube of the orbital radius (R³)."**

This means that if you know the distance of a planet or satellite from the central body (e.g., the Sun or Earth), you can calculate how long it takes to complete one orbit. Conversely, if you know the orbital period, you can determine the orbital radius.

---

## **2. Physical Derivation: Kepler's Third Law**

### **2.1 Basic Assumptions**
To derive Kepler's Third Law, we make the following assumptions:
1. **Circular Orbit**: The planet or satellite moves in a perfect circular orbit around the central body.
2. **Centripetal Force**: The gravitational force acts as the centripetal force that keeps the planet or satellite in orbit.

---

### **2.2 Mathematical Derivation**

#### **Step 1: Balance Gravitational and Centripetal Forces**
The gravitational force between two masses is given by Newton's Law of Gravitation:

$$
F_{\text{grav}} = G \frac{M m}{R^2}
$$

The centripetal force required to keep the planet in circular motion is:

$$
F_{\text{centripetal}} = m \frac{v^2}{R}
$$

For a stable circular orbit, these two forces must balance:

$$
F_{\text{grav}} = F_{\text{centripetal}}
$$

Substituting the expressions:

$$
G \frac{M m}{R^2} = m \frac{v^2}{R}
$$

#### **Step 2: Relate Orbital Velocity to Period**
The orbital velocity $$v$$ is related to the orbital period $$T$$ by the formula:

$$
v = \frac{\text{Circumference}}{\text{Period}} = \frac{2 \pi R}{T}
$$

Substitute this into the force balance equation:

$$
G \frac{M}{R^2} = \frac{\left( \frac{2 \pi R}{T} \right)^2}{R}
$$

#### **Step 3: Simplify the Expression**
Simplify the equation:

$$
G M = \frac{4 \pi^2 R^3}{T^2}
$$

Rearranging for $T^2$:

$$
T^2 = \frac{4 \pi^2}{G M} R^3
$$

This is the mathematical expression of **Kepler's Third Law**. The term $$\frac{4 \pi^2}{G M}$$ is a constant for a given central body (e.g., the Sun or Earth).

---

### **2.3 Key Insight**
Kepler's Third Law shows that:
- The orbital period $T$ increases with the orbital radius $R$.
- Larger orbits take longer to complete because the planet or satellite must travel a greater distance at a slower speed.

---

## **3. Astronomical Significance and Applications**

### **3.1 Calculating Planetary Masses**
Kepler's Third Law allows us to calculate the mass of a central body (e.g., the Sun or Earth) if we know the orbital period and radius of a planet or satellite.

#### **Example: Calculating the Sun's Mass**
Using Earth's orbital period (1 year) and radius (1 AU):

$$
M_{\text{Sun}} = \frac{4 \pi^2 (1 \, \text{AU})^3}{G (1 \, \text{year})^2}
$$

Substitute:
- $$1 \, \text{AU} = 1.496 \times 10^{11} \, \text{m}$$
- $$1 \, \text{year} = 3.154 \times 10^7 \, \text{s}$$
- $$G = 6.674 \times 10^{-11} \, \text{m}^3 \text{kg}^{-1} \text{s}^{-2}$$

The Sun's mass is approximately $1.989 \times 10^{30} \, \text{kg}$.

---

### **3.2 Satellite Orbits**
Kepler's Third Law is used to calculate the orbital period of satellites around Earth. For example:
- The Moon's orbital period (27.3 days) and radius (384,400 km) can be used to calculate Earth's mass.

---

### **3.3 Exoplanet Research**
Astronomers use Kepler's Third Law to detect and study exoplanets. By measuring the orbital period and velocity of a star (using Doppler spectroscopy), they can estimate the orbital radius and mass of the exoplanet.

---

## **4. Computational Modeling: Python Simulation**


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
```

---

## **5. Results and Observations**

### **5.1 Simulation Results**
- The plot of $T^2$ vs $R^3$ shows a straight line, confirming the proportionality predicted by Kepler's Third Law.
- This verifies that the square of the orbital period is directly proportional to the cube of the orbital radius.

### **5.2 Key Takeaways**
- Kepler's Third Law applies universally to any object in a circular orbit, whether it's a planet, satellite, or exoplanet.
- The relationship $T^2 \propto R^3$ allows us to calculate unknown masses or orbital parameters in astrophysical systems.

---


