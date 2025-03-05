# Problem 1
import numpy as np
import matplotlib.pyplot as plt

g = 9.8 # m/s^2
v0 = 20 # m/s
aci_degree = np.linspace(0, 90, 91)
aci_radian = np.radians(aci_degree)

R = (v0**2 * np.sin(2* aci_radian)) / g

plt.figure(figsize=(10, 6))
plt.plot(aci_degree, R, label=f'v₀ = {v0} m/s, g = {g} m/s²')
plt.xlabel("Shooting Angle (degrees)")
plt.ylabel("Range (metres)")
plt.title("Range vs. Angle of Fire")
plt.grid(True)
plt.legend()
plt.show()


###First, let us derive the equations of the throwing motion of a body from the basic principles of physics. Shooting motion takes place in two dimensions: horizontal (x) and vertical (y). For now, we ignore air resistance (an ideal model) and assume that only the force of gravity acts downwards, which is the acceleration \( g \).

### Derivation of Equations
### Gravitational acceleration affects only in the y direction:
###- \( a_x = 0 \) (no acceleration in the horizontal)
###- \( a_y = -g \) (downward acceleration)

###Given the initial velocity \( v_0 \) and the throw angle \( \theta \):
###- Horizontal initial velocity: \( v_{0x} = v_0 \cos\theta \)
###- Vertical initial velocity: \( v_{0y} = v_0 \sin\theta \)

###Equations:
###- \( x(t) = v_0 \cos\theta \cdot t \)
###- \( y(t) = v_0 \sin\theta \cdot t - \frac{1}{2} g t^2 \)

## Analysing Range 2

###The range is the horizontal distance when the object returns to the point \( y = 0 \). \( R \) range equation:

###[ R = \frac{v_0^2 \sin 2\theta}{g} \]

###- Maximum range: \( \( \theta = 45^\\circ \), \( R_{max} = \frac{v_0^2}{g} \)
###- As \( v_0 \) increases, the range increases, as \( g \) increases, the range decreases.

## 3. Practical Applications

###This model can be used in the following areas:
###- **Sports**: Football, basketball, archery, etc.
###- **Engineering**: Artillery shells, rockets
###- **Astrophysics**: Movement in low gravity environments




#### Results
###- The angle at which the maximisation is 45°
###- Air resistance not taken into account, range may be shorter in the real world**
###- Range increases if initial speed increases

