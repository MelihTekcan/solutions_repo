<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Projectile Motion Analysis</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
            line-height: 1.6;
        }
        h1, h2 {
            color: #2c3e50;
        }
        img {
            max-width: 100%;
            height: auto;
            display: block;
            margin: 20px auto;
        }
        ul {
            margin: 10px 0;
            padding-left: 20px;
        }
        p {
            margin: 10px 0;
        }
    </style>
</head>
<body>
    <h1>Investigating the Range as a Function of the Angle of Projection</h1>

    <h2>1. Theoretical Foundation</h2>
    <p>Projectile motion is governed by Newton’s laws under constant gravitational acceleration. The key equations are derived as follows:</p>
    <ul>
        <li><b>Horizontal Motion</b>: \( x(t) = v_0 \cos\theta \cdot t \)</li>
        <li><b>Vertical Motion</b>: \( y(t) = h + v_0 \sin\theta \cdot t - \frac{1}{2} g t^2 \)</li>
        <li><b>Range</b>: \( R = \frac{v_0^2 \sin 2\theta}{g} \) for \( h = 0 \)</li>
    </ul>

    <h2>2. Analysis of the Range</h2>
    <p>The range depends heavily on the angle of projection, as shown below:</p>
    <img src="range_vs_angle.png" alt="Range vs Angle Plot">
    <p><b>Key Observations:</b></p>
    <ul>
        <li>Maximum range occurs at 45° for \( h = 0 \).</li>
        <li>Higher initial velocity increases the range quadratically.</li>
        <li>Lower gravity (e.g., on the Moon) significantly extends the range.</li>
    </ul>

    <h2>3. Practical Applications</h2>
    <p>Trajectories for \( v_0 = 20 \, \text{m/s} \), \( g = 9.81 \, \text{m/s}^2 \), and \( h = 0 \):</p>
    <img src="trajectories.png" alt="Trajectories Plot">
    <p><b>Real-World Examples:</b></p>
    <ul>
        <li><b>Sports</b>: Basketball players use angles around 50° for optimal shots.</li>
        <li><b>Engineering</b>: Artillery adjusts for elevation and terrain.</li>
        <li><b>Astrophysics</b>: On Mars, ranges are longer due to lower gravity.</li>
    </ul>

    <h2>4. Limitations and Extensions</h2>
    <p>This idealized model assumes:</p>
    <ul>
        <li>No air resistance: Real projectiles experience drag.</li>
        <li>Flat terrain: Uneven surfaces require adjustments.</li>
        <li>No wind: Wind alters the horizontal motion.</li>
    </ul>
    <p><b>Extensions:</b></p>
    <ul>
        <li>Include air resistance using numerical methods.</li>
        <li>Simulate variable gravity for high-altitude trajectories.</li>
    </ul>
</body>
</html>




