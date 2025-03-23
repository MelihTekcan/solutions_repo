<!DOCTYPE html>
<html lang="en">np
<head> matplotlib.pyplot as plt
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Projectile Motion Simulation</title>
    <link rel="stylesheet" href="css/styles.css">
</head>ian = np.radians(aci_degree)
<body>
    <header> np.sin(2* aci_radian)) / g
        <h1>Investigating the Range as a Function of the Angle of Projection</h1>
    </header>gsize=(10, 6))
    <main>ci_degree, R, label=f'v₀ = {v0} m/s, g = {g} m/s²')
        <section id="motivation">es)")
            <h2>Motivation</h2>
            <p>Projectile motion, while seemingly simple, offers a rich playground for exploring fundamental principles of physics. The problem is straightforward: analyze how the range of a projectile depends on its angle of projection. Yet, beneath this simplicity lies a complex and versatile framework. The equations governing projectile motion involve both linear and quadratic relationships, making them accessible yet deeply insightful.</p>
            <p>What makes this topic particularly compelling is the number of free parameters involved in these equations, such as initial velocity, gravitational acceleration, and launch height. These parameters give rise to a diverse set of solutions that can describe a wide array of real-world phenomena, from the arc of a soccer ball to the trajectory of a rocket.</p>
        </section>
        <section id="task">
            <h2>Task</h2>
            <ol>
                <li>ive the equations of the throwing motion of a body from the basic principles of physics. Shooting motion takes place in two dimensions: horizontal (x) and vertical (y). For now, we ignore air resistance (an ideal model) and assume that only the force of gravity acts downwards, which is the acceleration \( g \).
                    <h3>Theoretical Foundation</h3>
                    <p>Begin by deriving the governing equations of motion from fundamental principles. This involves solving a basic differential equation to establish the general form of the motion. Highlight how variations in initial conditions lead to a family of solutions.</p>
                </li>eleration affects only in the y direction:
                <li>no acceleration in the horizontal)
                    <h3>Analysis of the Range</h3>
                    <p>Investigate how the horizontal range depends on the angle of projection. Discuss how changes in other parameters, such as initial velocity and gravitational acceleration, influence the relationship.</p>
                </li>velocity \( v_0 \) and the throw angle \( \theta \):
                <li>ial velocity: \( v_{0x} = v_0 \cos\theta \)
                    <h3>Practical Applications</h3>n\theta \)
                    <p>Reflect on how this model can be adapted to describe various real-world situations, such as projectiles launched on uneven terrain or in the presence of air resistance.</p>
                </li>
                <li>cos\theta \cdot t \)
                    <h3>Implementation</h3>ac{1}{2} g t^2 \)
                    <p>Develop a computational tool or algorithm to simulate projectile motion. Visualize the range as a function of the angle of projection for different sets of initial conditions.</p>
                </li>
            </ol>
        </section>e horizontal distance when the object returns to the point \( y = 0 \). \( R \) range equation:
        <section id="deliverables">
            <h2>Deliverables</h2>}{g} \]
            <ul>
                <li>A Markdown document with Python script or notebook implementing the simulations.</li>
                <li>A detailed description of the family of solutions derived from the governing equations.</li>
                <li>Graphical representations of the range versus angle of projection, highlighting how different parameters influence the curve.</li>
                <li>A discussion on the limitations of the idealized model and suggestions for incorporating more realistic factors, such as drag or wind.</li>
            </ul>
        </section>be used in the following areas:
        <section id="hints-resources"> archery, etc.
            <h2>Hints and Resources</h2>rockets
            <ul>ics**: Movement in low gravity environments
                <li>Start from the fundamental laws of motion and gradually build the general solution.</li>
                <li>Use numerical methods or simulation tools to explore scenarios that go beyond simple analytical solutions.</li>
                <li>Consider how this model connects to real-world systems, such as sports, engineering, and astrophysics.</li>
            </ul>
            <p>This task encourages a deep understanding of projectile motion while showcasing its versatility and applicability across various domains.</p>
        </section>which the maximisation is 45°
        <section id="explanation">sistance not taken into account, range may be shorter in the real world**
            <h2>Explanation</h2>ncreases if initial speed increases
            <p>This study will explore the relationship between the projection angle of a projectile and its corresponding range. This situation exemplifies a fundamental case of projectile motion, which is particularly intriguing as it integrates elementary mathematical principles with practical insights. To maintain clarity and precision in our analysis, certain assumptions will be made: the projectile is considered to be launched from the ground level (initial height = 0), air resistance is disregarded, and the gravitational force is treated as constant. These are the default initial parameters unless you would prefer that I modify them.</p>
            <p>The range of a projectile is the horizontal distance it travels before it strikes the ground. To see how this depends on the angle of projection, we need the range formula. The horizontal range \( R \) depends on the initial velocity \( v_0 \), the angle of projection \( \theta \), and the acceleration due to gravity \( g \). The time of flight comes from the vertical motion, but the range is all about horizontal distance traveled.</p>ill explore the relationship between the projection angle of a projectile and its corresponding range. This situation exemplifies a fundamental case of projectile motion, which is particularly intriguing as it integrates elementary mathematical principles with practical insights. To maintain clarity and precision in our analysis, certain assumptions will be made: the projectile is considered to be launched from the ground level (initial height = 0), air resistance is disregarded, and the gravitational force is treated as constant. These are the default initial parameters unless you would prefer that I modify them.
            <p>Returning to first principles: the initial velocity has horizontal and vertical components. Horizontally, it is \( v_{0x} = v_0 \cos\theta \), and vertically, it is \( v_{0y} = v_0 \sin\theta \). Horizontally, there is no acceleration, so range is just \( R = v_{0x} \times t \), where \( t \) is the total flight time.</p>
            <p>The duration of the flight relies on the vertical movement. The projectile rises, reaching a peak (vertical velocity = 0), then falls. Applying the kinematic equation \( v_y = v_{0y} - gt \), at the peak, \( 0 = v_0 \sin\theta - gt_{\text{peak}} \), so \( t_{\text{peak}} = \frac{v_0 \sin\theta}{g} \).</p>nge of a projectile is the horizontal distance it travels before it strikes the ground. To see how this depends on the angle of projection, we need the range formula. The horizontal range \( R \) depends on the initial velocity \( v_0 \), the angle of projection \( \theta \), and the acceleration due to gravity \( g \). The time of flight comes from the vertical motion, but the range is all about horizontal distance traveled.
            <p>Since the rise time equals the fall time (symmetrical parabola), the total flight time is \( t = 2 \times t_{\text{peak}} = \frac{2 v_0 \sin\theta}{g} \).</p>


















</html></body>    <script src="js/scripts.js"></script>    </footer>        <p>&copy; 2025 Projectile Motion Simulation</p>    <footer>    </main>        </section>            </ul>                <li><strong>Extremes:</strong> If \( \theta = 0^{\circ} \) (straight ahead), \( \sin 0^{\circ} = 0 \), so \( R = 0 \)—it never goes horizontally. If \( \theta = 90^{\circ} \) (straight up), \( \sin 180^{\circ} = 0 \), and again \( R = 0 \)—it simply falls back to the start. The range is at its greatest in between. Therefore, the curve is not a straight line—it is sinusoidal! As \( \theta \) goes from 0° to 90°, the range goes up to a maximum at 45° and then decreases symmetrically. The values of \( v_0 \) and \( g \) scale the range but do not change the angle dependence—higher velocity stretches it, higher gravity compresses it. We can try particular angles with numerical values (e.g., \( v_0 = 10 \, \text{m/s} \) and \( g = 9.8 \, \text{m/s}^2 \)), or investigate the effect of launching from an initial height.</li>                <li><strong>Symmetry:</strong> Observe that \( \sin 2\theta \) yields the same result for complementary angles. For instance, when \( \theta \) is set to \( 30^{\circ} \) and \( 60^{\circ} \), both are equal to \( 2\theta = 60^{\circ} \) or \( 120^{\circ} \), where \( \sin 60^{\circ} = \sin 120^{\circ} = \frac{\sqrt{3}}{2} \). The value of \( R \) is thus equal for \( 30^{\circ} \) and \( 60^{\circ} \). This symmetry is cool—it shows multiple angles can achieve the same range, just with different heights and times.</li>                <li><strong>Maximum Range:</strong> The range \( \sin 2\theta \) takes values from -1 to 1, with the highest value being 1 when \( 2\theta = 90^{\circ} \), or \( \theta = 45^{\circ} \). At this angle, \( R = \frac{v_0^2}{g} \) is the maximum range the projectile can reach. This is understandable, as an angle of 45° optimally balances the horizontal and vertical components on level ground.</li>            <ul>            <p>The key equation is highlighted here. The range depends on \( \sin 2\theta \), so the angle \( \theta \) is crucial. Let's look at the implications of this observation:</p>            \[ R = \frac{v_0^2 \sin 2\theta}{g} \]</p>            There's a handy trig identity here: \( \sin 2\theta = 2 \sin\theta \cos\theta \), so the range simplifies to:            \( R = v_0 \cos\theta \times \frac{2 v_0 \sin\theta}{g} = \frac{2 v_0^2 \sin\theta \cos\theta}{g} \).            <p>Now plug that into the range:#Returning to first principles: the initial velocity has horizontal and vertical components. Horizontally, it is \( v_{0x} = v_0 \cos\theta \), and vertically, it is \( v_{0y} = v_0 \sin\theta \). Horizontally, there is no acceleration, so range is just \( R = v_{0x} \times t \), where \( t \) is the total flight time.

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