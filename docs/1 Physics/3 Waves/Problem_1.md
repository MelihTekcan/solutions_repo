# Problem 1

## **Introduction**

Wave motion is a fundamental concept in physics that describes how energy is transferred through a medium without the transport of matter. Waves are all around us whether it’s the sound we hear, the light we see, or the ripples on a pond. This problem focuses on understanding the basic principles of wave motion, including the mathematical description of waves, their properties, and their behavior in different scenarios.

---

## **What is a Wave?**

A wave is a disturbance that travels through a medium, transferring energy from one point to another. Waves can be classified into two main types:

1. **Mechanical Waves**: Require a medium to propagate (e.g., sound waves, water waves).
2. **Electromagnetic Waves**: Do not require a medium and can travel through a vacuum (e.g., light, radio waves).

---

## **Key Properties of Waves**

To understand wave motion, we need to define some key properties:

1. **Wavelength ($\lambda$)**: The distance between two consecutive points in phase on a wave (e.g., crest to crest or trough to trough). Measured in meters (m).

2. **Frequency ($f$)**: The number of wave cycles that pass a given point per second. Measured in hertz (Hz).

3. **Period ($T$)**: The time it takes for one complete wave cycle to pass a point. Related to frequency by:
   $$
   T = \frac{1}{f}
   $$

4. **Wave Speed ($v$$)**: The speed at which the wave propagates through the medium. Related to wavelength and frequency by:
   $$
   v = f \lambda
   $$

5. **Amplitude ($A$)**: The maximum displacement of the wave from its equilibrium position. Determines the wave’s energy.

---

## **Mathematical Description of a Wave**

The general equation for a traveling wave is:

$$
y(x, t) = A \sin(kx - \omega t + \phi)
$$

Where:
- $y(x, t)$: Displacement of the wave at position $x$ and time $t$.
- $A$: Amplitude of the wave.
- $k = \frac{2\pi}{\lambda}$: Wave number (spatial frequency).
- $\omega = 2\pi f$: Angular frequency (temporal frequency).
- $\phi$: Phase constant, which determines the wave’s initial position.

---

## **Practical Applications of Wave Motion**

1. **Communication**: Radio and television signals use electromagnetic waves to transmit information.
2. **Seismology**: Understanding wave motion helps scientists study earthquakes and the Earth’s interior.
3. **Medical Imaging**: Ultrasound waves are used to create images of internal body structures.
4. **Music**: Sound waves are the basis of musical instruments and acoustics.

---

## **Wave Simulation Using Python**


```python
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Wave parameters
A = 0.05  # Amplitude (m)
k = 4 * np.pi  # Wave number (rad/m)
omega = 20 * np.pi  # Angular frequency (rad/s)
lambda_ = 2 * np.pi / k  # Wavelength (m)
f = omega / (2 * np.pi)  # Frequency (Hz)
v = f * lambda_  # Wave speed (m/s)

# Spatial and temporal domains
x = np.linspace(0, 2, 500)  # Position (m)
t = np.linspace(0, 1, 100)  # Time (s)

# Wave function
def wave(x, t):
    return A * np.sin(k * x - omega * t)

# Create a figure for the animation
fig, ax = plt.subplots(figsize=(8, 4))
ax.set_xlim(0, 2)
ax.set_ylim(-A * 1.5, A * 1.5)
ax.set_xlabel("Position (m)")
ax.set_ylabel("Displacement (m)")
ax.set_title("Wave Propagation")
line, = ax.plot([], [], lw=2)

# Animation function
def update(frame):
    y = wave(x, t[frame])
    line.set_data(x, y)
    return line,

# Create the animation
ani = FuncAnimation(fig, update, frames=len(t), interval=50, blit=True)

# Show the animation
plt.show()
```

---

