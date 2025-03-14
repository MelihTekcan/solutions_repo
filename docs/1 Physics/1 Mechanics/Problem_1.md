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

#This study will explore the relationship between the projection angle of a projectile and its corresponding range. This situation exemplifies a fundamental case of projectile motion, which is particularly intriguing as it integrates elementary mathematical principles with practical insights. To maintain clarity and precision in our analysis, certain assumptions will be made: the projectile is considered to be launched from the ground level (initial height = 0), air resistance is disregarded, and the gravitational force is treated as constant. These are the default initial parameters unless you would prefer that I modify them.

#The range of a projectile is the horizontal distance it travels before it strikes the ground. To see how this depends on the angle of projection, we need the range formula. The horizontal range \( R \) depends on the initial velocity \( v_0 \), the angle of projection \( \theta \), and the acceleration due to gravity \( g \). The time of flight comes from the vertical motion, but the range is all about horizontal distance traveled.

#Returning to first principles: the initial velocity has horizontal and vertical components. Horizontally, it is \( v_{0x} = v_0 \cos\theta \), and vertically, it is \( v_{0y} = v_0 \sin\theta \). Horizontally, there is no acceleration, so range is just \( R = v_{0x} \times t \), where \( t \) is the total flight time.

#The duration of the flight relies on the vertical movement. The projectile rises, reaching a peak (vertical velocity = 0), then falls. Applying the kinematic equation \( v_y = v_{0y} - gt \), at the peak, \( 0 = v_0 \sin\theta - gt_{\text{peak}} \), so \( t_{\text{peak}} = \frac{v_0 \sin\theta}{g} \).

#Since the rise time equals the fall time (symmetrical parabola), the total flight time is \( t = 2 \times t_{\text{peak}} = \frac{2 v_0 \sin\theta}{g} \).

#Now plug that into the range:
#\( R = v_0 \cos\theta \times \frac{2 v_0 \sin\theta}{g} = \frac{2 v_0^2 \sin\theta \cos\theta}{g} \).
#There's a handy trig identity here: \( \sin 2\theta = 2 \sin\theta \cos\theta \), so the range simplifies to:

#\[ R = \frac{v_0^2 \sin 2\theta}{g} \]

#The key equation is highlighted here. The range depends on \( \sin 2\theta \), so the angle \( \theta \) is crucial. Let's look at the implications of this observation: - **Maximum Range**: The range \( \sin 2\theta \) takes values from -1 to 1, with the highest value being 1 when \( 2\theta = 90^{\circ} \), or \( \theta = 45^{\circ} \). At this angle, \( R = \frac{v_0^2}{g} \) is the maximum range the projectile can reach. This is understandable, as an angle of 45° optimally balances the horizontal and vertical components on level ground.

#- **Symmetry**: Observe that \( \sin 2\theta \) yields the same result for complementary angles. For instance, when \( \theta \) is set to \( 30^{\circ} \) and \( 60^{\circ} \), both are equal to \( 2\theta = 60^{\circ} \) or \( 120^{\circ} \), where \( \sin 60^{\circ} = \sin 120^{\circ} = \frac{\sqrt{3}}{2} \). The value of \( R \) is thus equal for \( 30^{\circ} \) and \( 60^{\circ} \).

#This symmetry is cool—it shows multiple angles can achieve the same range, just with different heights and times.

#- **Extremes**: If \( \theta = 0^{\circ} \) (straight ahead), \( \sin 0^{\circ} = 0 \), so \( R = 0 \)—it never goes horizontally. If \( \theta = 90^{\circ} \) (straight up), \( \sin 180^{\circ} = 0 \), and again \( R = 0 \)—it simply falls back to the start. The range is at its greatest in between. Therefore, the curve is not a straight line—it is sinusoidal! As \( \theta \) goes from 0° to 90°, the range goes up to a maximum at 45° and then decreases symmetrically. The values of \( v_0 \) and \( g \) scale the range but do not change the angle dependence—higher velocity stretches it, higher gravity compresses it. We can try particular angles with numerical values (e.g., \( v_0 = 10 \, \text{m/s} \) and \( g = 9.8 \, \text{m/s}^2 \)), or investigate the effect of launching from an initial height.