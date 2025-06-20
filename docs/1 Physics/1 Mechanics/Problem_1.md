# Problem 1

Projectile motion is a fundamental concept in physics that describes the motion of an object launched into the air under the influence of gravity. This motion is characterized by a **parabolic trajectory**, and it is widely applicable in sports, engineering, and astrophysics.

---

## 1. Theoretical Foundation

### What is Projectile Motion?

Projectile motion occurs when an object is launched with an initial velocity $v_0$ at an angle $\theta$ to the horizontal. The motion is influenced only by gravity $g$, assuming no air resistance. The motion can be broken into two independent components:

1. **Horizontal Motion**:
   - The horizontal velocity remains constant because there is no horizontal acceleration.
   - The horizontal position at time $t$ is given by:
     $$
     x(t) = v_0 \cos(\theta) \cdot t
     $$

2. **Vertical Motion**:
   - The vertical velocity decreases due to the acceleration caused by gravity.
   - The vertical position at time $t$ is given by:
     $$
     y(t) = v_0 \sin(\theta) \cdot t - \frac{1}{2} g t^2
     $$

### Key Equations

1. **Time of Flight**:
   - The total time the projectile spends in the air is:
     $$
     T = \frac{2 v_0 \sin(\theta)}{g}
     $$

2. **Range**:
   - The horizontal distance traveled by the projectile is:
     $$
     R = \frac{v_0^2 \sin(2\theta)}{g}
     $$

3. **Maximum Height**:
   - The highest point reached by the projectile is:
     $$
     H = \frac{v_0^2 \sin^2(\theta)}{2g}
     $$

---

## 2. Analysis of the Range

### How Does the Range Depend on the Angle of Projection?

TThe range $R$ depends on:

1. **Initial velocity ($v_0$)**  
   - Quadratic dependence:  
     $$
     R \propto v_0^2
     $$

2. **Projection angle ($\theta$)**  
   - Maximum at $45^\circ$:  
     $$
     R = \frac{v_0^2 \sin(2\theta)}{g}
     $$

3. **Gravity ($g$)**  
   - Inversely proportional:  
     $$
     R \propto \frac{1}{g}
     $$

### Key Observations
1. The range is symmetric:  
   $$
   R(\theta) = R(90^\circ - \theta)
   $$
   For example, the range at $\theta = 30^\circ$ is the same as at $\theta = 60^\circ$.

2. The maximum range occurs at $\theta = 45^\circ$ for flat terrain.

---

## 3. Practical Applications

### Real-World Scenarios

Projectile motion has numerous real-world applications across various fields:

- **Sports**:  
  In sports like soccer and golf, players adjust the angle of projection ($\theta$) and the initial velocity ($v_0$) to achieve optimal range or height. For example:
  - A soccer player might aim for a higher angle to clear a wall of defenders.
  - A golfer adjusts the angle and velocity to maximize the distance of a drive.

- **Engineering**:  
  Engineers use projectile motion principles to design artillery and rockets. They account for factors like terrain, wind effects, and the desired range to ensure accuracy. For example:
  - Artillery shells are launched at specific angles to hit targets at known distances.
  - Rockets are launched with precise trajectories to reach their destinations.

- **Astrophysics**:  
  In space exploration, spacecraft trajectories are calculated using projectile motion principles. However, these calculations also account for variable gravitational forces and drag. For example:
  - A Mars rover's landing trajectory is carefully planned to ensure a safe descent.
  - Satellites are launched into orbit using similar principles, with adjustments for Earth's curvature and atmosphere.

### Trajectory Example

The trajectory for an object launched with an initial velocity of $v_0 = 20\,\text{m/s}$ at an angle of $\theta = 45^\circ$



The parabolic path demonstrates the interplay between horizontal and vertical motion:
- The horizontal motion is uniform, with a constant velocity.
- The vertical motion is accelerated due to gravity, resulting in a curved path.

---

## 4. Implementation

```python
import numpy as np
import matplotlib.pyplot as plt

def plot_projectile_motion():
    # Parameters
    v0 = 20  # Initial velocity (m/s)
    theta = 45  # Angle (degrees)
    g = 9.8  # Gravity (m/s²)
    
    # Time of flight
    t_max = 2 * v0 * np.sin(np.deg2rad(theta)) / g
    t = np.linspace(0, t_max, 100)
    
    # Calculate x and y positions
    x = v0 * np.cos(np.deg2rad(theta)) * t
    y = v0 * np.sin(np.deg2rad(theta)) * t - 0.5 * g * t**2
    
    # Create plot
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, 'b-', label='Trajectory')
    plt.title(f'Projectile Motion (v₀={v0} m/s, θ={theta}°)')
    plt.xlabel('Distance (m)')
    plt.ylabel('Height (m)')
    plt.grid(True)
    plt.legend()
    
    # Save plot
    plt.savefig('projectile_motion.png')
    plt.close()

# Generate the plot
plot_projectile_motion()
```

**Output:**

[](projectile_motion.png)

