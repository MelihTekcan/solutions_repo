# Problem 2
# Escape Velocities and Cosmic Velocities:

Imagine you're trying to throw a ball so hard that it leaves Earth and never comes back. Or picture a rocket zooming into space to orbit the planet or travel to Mars. To make these things happen, we need to understand **escape velocity** and **cosmic velocities**. These are special speeds that objects need to reach to overcome gravity and move through space.

---

## What Are Escape and Cosmic Velocities?

Gravity is like an invisible force that pulls things toward the ground. If you want to escape gravity, you need to move really, really fast. The speeds required for different space tasks are called **escape velocity** and **cosmic velocities**. Let’s break them down:

1. **First Cosmic Velocity (Orbital Velocity)**: This is the speed needed to orbit a planet, like a satellite circling Earth. The object stays close to the planet, moving fast enough so gravity doesn’t pull it back down, but not so fast that it escapes into space.

2. **Second Cosmic Velocity (Escape Velocity)**: This is the speed needed to completely break free from a planet’s gravity. If a rocket reaches this speed, it can leave Earth and travel into deep space without falling back.

3. **Third Cosmic Velocity**: This is the speed needed to escape the gravitational pull of a star, like our Sun, and leave the star system. For example, a spacecraft leaving Earth to travel beyond our Solar System needs this speed.

Think of it like this:
- **First**: Stay in a circle around the planet (like a hula hoop).
- **Second**: Fly away from the planet forever.
- **Third**: Leave the whole star system and go to another one.

---

## The Math Behind These Velocities

Don’t worry if math sounds scary! We’ll explain it step-by-step, like following a recipe. These velocities depend on two main things:
- **Mass** of the planet or star (how heavy it is).
- **Radius** (how big it is, measured from the center to the surface).

We also use a special number called the **gravitational constant ($G$)**, which is like a rule that applies everywhere in the universe. Its value is:

$$
G = 6.674 \times 10^{-11} \, \text{m}^3 \text{kg}^{-1} \text{s}^{-2}
$$

### First Cosmic Velocity (Orbital Velocity)

To orbit a planet, an object needs to move fast enough so that the pull of gravity keeps it in a circular path, like swinging a ball on a string. The formula is:

$$
v_1 = \sqrt{\frac{G \cdot M}{r}}
$$

- **$M$**: Mass of the planet (in kilograms).
- **$r$**: Radius of the planet (in meters).
- **$G$**: Gravitational constant.

This speed ensures the object stays in orbit without falling back or flying away.

### Second Cosmic Velocity (Escape Velocity)

To escape a planet’s gravity entirely, an object needs enough energy to overcome the gravitational pull. The formula is:

$$
v_2 = \sqrt{\frac{2 \cdot G \cdot M}{r}}
$$

Notice that this is just the first cosmic velocity multiplied by $\sqrt{2}$:

$$
v_2 = v_1 \cdot \sqrt{2}
$$

This makes sense because escaping requires more energy than just orbiting.

### Third Cosmic Velocity

This one is trickier. It’s the speed needed to escape a star’s gravity (like the Sun) from the orbit of a planet (like Earth). The formula depends on the planet’s orbit around the star and the star’s mass. For a spacecraft leaving Earth to escape the Sun’s gravity, the formula is complex, but a simplified version gives:

$$
v_3 = \sqrt{\frac{2 \cdot G \cdot M_{\text{sun}}}{R_{\text{orbit}}}} + v_{\text{planet}}
$$

- **$M_{\text{sun}}$**: Mass of the Sun.
- **$R_{\text{orbit}}$**: Distance from the Sun to the planet (e.g., Earth’s orbit radius).
- **$v_{\text{planet}}$**: The planet’s orbital speed around the Sun.

This speed is much higher because the Sun is way bigger and heavier than Earth.

---

## Calculating Velocities for Earth, Mars, and Jupiter

Let’s calculate these velocities for three celestial bodies: **Earth**, **Mars**, and **Jupiter**. We’ll use the following data:

| Celestial Body | Mass ($M$, kg)         | Radius ($r$, m) | Distance from Sun ($R_{\text{orbit}}$, m) |
|----------------|--------------------------|-------------------|--------------------------------------------|
| Earth         | $5.972 \times 10^{24}$ | $6.371 \times 10^6$ | $1.496 \times 10^{11}$                  |
| Mars          | $6.417 \times 10^{23}$ | $3.390 \times 10^6$ | $2.279 \times 10^{11}$                  |
| Jupiter       | $1.899 \times 10^{27}$ | $6.991 \times 10^7$ | $7.785 \times 10^{11}$                  |
| Sun           | $1.989 \times 10^{30}$ | -                 | -                                          |

We’ll write a Python script to calculate:
- **First cosmic velocity** (orbital velocity).
- **Second cosmic velocity** (escape velocity).
- **Third cosmic velocity** (to escape the Sun, starting from each planet’s orbit).

The script will also create bar charts to compare these velocities.

### Python Script

```python
import numpy as np
import matplotlib.pyplot as plt

# Constants
G = 6.674e-11  # Gravitational constant (m^3 kg^-1 s^-2)

# Data for celestial bodies
bodies = {
    'Earth': {
        'mass': 5.972e24,  # kg
        'radius': 6.371e6,  # m
        'orbit_radius': 1.496e11,  # m (distance from Sun)
        'orbital_velocity_sun': 29.78e3  # m/s (Earth's speed around Sun)
    },
    'Mars': {
        'mass': 6.417e23,
        'radius': 3.390e6,
        'orbit_radius': 2.279e11,
        'orbital_velocity_sun': 24.13e3
    },
    'Jupiter': {
        'mass': 1.899e27,
        'radius': 6.991e7,
        'orbit_radius': 7.785e11,
        'orbital_velocity_sun': 13.07e3
    }
}
sun_mass = 1.989e30  # Mass of the Sun (kg)

# Calculate velocities
v1_list = []  # First cosmic velocity (orbital)
v2_list = []  # Second cosmic velocity (escape)
v3_list = []  # Third cosmic velocity (escape Sun)
names = []

for body, data in bodies.items():
    # First cosmic velocity: v1 = sqrt(G * M / r)
    v1 = np.sqrt(G * data['mass'] / data['radius']) / 1000  # Convert to km/s
    # Second cosmic velocity: v2 = sqrt(2 * G * M / r)
    v2 = np.sqrt(2 * G * data['mass'] / data['radius']) / 1000  # Convert to km/s
    # Third cosmic velocity: Approximate as escape velocity from Sun at planet's orbit
    v_sun_escape = np.sqrt(2 * G * sun_mass / data['orbit_radius']) / 1000  # km/s
    v3 = v_sun_escape + (data['orbital_velocity_sun'] / 1000)  # Add planet's orbital velocity

    v1_list.append(v1)
    v2_list.append(v2)
    v3_list.append(v3)
    names.append(body)

# Plotting
plt.figure(figsize=(10, 6))
bar_width = 0.25
index = np.arange(len(names))

plt.bar(index, v1_list, bar_width, label='First Cosmic Velocity (Orbital)', color='blue')
plt.bar(index + bar_width, v2_list, bar_width, label='Second Cosmic Velocity (Escape)', color='green')
plt.bar(index + 2 * bar_width, v3_list, bar_width, label='Third Cosmic Velocity (Sun Escape)', color='red')

plt.xlabel('Celestial Body')
plt.ylabel('Velocity (km/s)')
plt.title('Cosmic Velocities for Earth, Mars, and Jupiter')
plt.xticks(index + bar_width, names)
plt.legend()
plt.grid(True, axis='y')
plt.tight_layout()

plt.savefig('cosmic_velocities.png')
plt.show()

```