# Problem 2: Estimating π Using Monte Carlo Methods

---

## Part 1: Estimating π Using a Unit Circle

### Python Implementation

```python
import numpy as np
import matplotlib.pyplot as plt

# Generate random points in [-1,1] x [-1,1]
n_points = 10000
points = np.random.uniform(-1, 1, (n_points, 2))

# Calculate distances from origin
distances = np.sqrt(points[:, 0]**2 + points[:, 1]**2)

# Count points inside circle
inside = np.sum(distances <= 1)

# Estimate π
pi_estimate = 4 * inside / n_points
print(f"Estimated π: {pi_estimate}")
```

---

### Visualization

```python
import numpy as np
import matplotlib.pyplot as plt

# Generate random points in [-1,1] x [-1,1]
n_points = 10000
points = np.random.uniform(-1, 1, (n_points, 2))
distances = np.sqrt(points[:, 0]**2 + points[:, 1]**2)

# Separate points inside and outside the circle
inside = distances <= 1
outside = ~inside

# Plot points
plt.figure(figsize=(8, 8))
plt.scatter(points[inside, 0], points[inside, 1], color='blue', s=1, alpha=0.5)
plt.scatter(points[outside, 0], points[outside, 1], color='red', s=1, alpha=0.5)

# Draw circle
theta = np.linspace(0, 2 * np.pi, 100)
plt.plot(np.cos(theta), np.sin(theta), color='green', linewidth=2)

plt.axis('equal')
plt.title(f"Monte Carlo Estimation of π (n={n_points})")
plt.show()
```

---

### Analysis of Convergence

```python
import numpy as np
import matplotlib.pyplot as plt

# Convergence analysis
max_points = 10000
step = 100
point_counts = range(1, max_points + 1, step)
estimates = []

for n in point_counts:
    points = np.random.uniform(-1, 1, (n, 2))
    distances = np.sqrt(points[:, 0]**2 + points[:, 1]**2)
    inside = np.sum(distances <= 1)
    pi_estimate = 4 * inside / n
    estimates.append(pi_estimate)

# Plot convergence
plt.figure(figsize=(10, 6))
plt.plot(point_counts, estimates, label='Estimate')
plt.axhline(np.pi, color='r', linestyle='--', label='True π')
plt.xlabel('Number of points')
plt.ylabel('π Estimate')
plt.title('Convergence of π Estimation')
plt.legend()
plt.grid()
plt.show()
```

---

## Part 2: Estimating π Using Buffon's Needle

### Python Implementation

```python
import numpy as np

n_drops = 100000
needle_length = 1
line_distance = 1

# Random position of needle center (0 to D)
centers = np.random.uniform(0, line_distance, n_drops)

# Random angle (0 to π/2 is sufficient)
angles = np.random.uniform(0, np.pi / 2, n_drops)

# Calculate if needle crosses
crosses = (centers <= (needle_length / 2) * np.sin(angles)) | \
          (centers >= line_distance - (needle_length / 2) * np.sin(angles))

crossing_prob = np.mean(crosses)
pi_estimate = (2 * needle_length) / (crossing_prob * line_distance) if crossing_prob > 0 else 0
print(f"Estimated π: {pi_estimate}")
```

---

### Visualization

```python
import numpy as np
import matplotlib.pyplot as plt

n_drops = 50
needle_length = 1
line_distance = 1

# Generate needle positions
centers = np.random.uniform(0, line_distance, n_drops)
angles = np.random.uniform(0, np.pi, n_drops)

# Calculate endpoints
x1 = centers - (needle_length / 2) * np.cos(angles)
x2 = centers + (needle_length / 2) * np.cos(angles)
y1 = (needle_length / 2) * np.sin(angles)
y2 = -(needle_length / 2) * np.sin(angles)

# Plot needles
plt.figure(figsize=(10, 5))

# Draw lines
for i in range(0, int(line_distance) + 1):
    plt.axvline(i, color='black')

# Draw needles
for i in range(n_drops):
    crosses = (centers[i] <= (needle_length / 2) * np.sin(angles[i])) or \
              (centers[i] >= line_distance - (needle_length / 2) * np.sin(angles[i]))
    color = 'red' if crosses else 'blue'
    plt.plot([x1[i], x2[i]], [y1[i], y2[i]], color=color, alpha=0.7)

plt.title("Buffon's Needle Simulation")
plt.axis('equal')
plt.ylim(-1, 1)
plt.show()
```

---

### Analysis of Convergence

```python
import numpy as np
import matplotlib.pyplot as plt

# Convergence analysis for Buffon's Needle
max_drops = 10000
step = 100
drop_counts = range(1, max_drops + 1, step)
estimates = []

for n in drop_counts:
    centers = np.random.uniform(0, line_distance, n)
    angles = np.random.uniform(0, np.pi / 2, n)
    crosses = (centers <= (needle_length / 2) * np.sin(angles)) | \
              (centers >= line_distance - (needle_length / 2) * np.sin(angles))
    crossing_prob = np.mean(crosses)
    pi_estimate = (2 * needle_length) / (crossing_prob * line_distance) if crossing_prob > 0 else 0
    estimates.append(pi_estimate)

# Plot convergence
plt.figure(figsize=(10, 6))
plt.plot(drop_counts, estimates, label='Estimate')
plt.axhline(np.pi, color='r', linestyle='--', label='True π')
plt.xlabel('Number of needle drops')
plt.ylabel('π Estimate')
plt.title("Convergence of Buffon's Needle")
plt.legend()
plt.grid()
plt.show()
```

