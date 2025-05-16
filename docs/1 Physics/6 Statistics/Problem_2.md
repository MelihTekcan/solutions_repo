# Problem 2

## **Estimating π Using Monte Carlo Methods**

## Introduction

Monte Carlo methods are a class of computational algorithms that rely on repeated random sampling to obtain numerical results. In this article, we'll explore two fascinating ways to estimate the value of π using these methods: the circle-based approach and Buffon's Needle experiment.

---

##  Estimating π Using a Unit Circle

### Theoretical Foundation

Imagine a unit circle (radius = 1) inscribed inside a square with side length 2. The area of the circle is:

$$
\text{Area of Circle} = \pi r^2 = \pi (1)^2 = \pi
$$

The area of the square is:

$$
\text{Area of Square} = (\text{side length})^2 = 2^2 = 4
$$

If we randomly scatter points inside the square, the probability that a point falls inside the circle is the ratio of their areas:

$$
P(\text{point inside circle}) = \frac{\text{Area of Circle}}{\text{Area of Square}} = \frac{\pi}{4}
$$

Rearranging this gives us our estimation formula:

$$
\pi \approx 4 \times \frac{\text{Number of points inside circle}}{\text{Total number of points}}
$$

---

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

### Theoretical Foundation

Buffon's Needle is one of the oldest problems in geometric probability. Imagine a needle of length \( L \) dropped onto a floor with parallel lines distance \( D \) apart (where $L \leq D$).

The probability that the needle crosses a line is:

$$
P(\text{cross}) = \frac{2L}{\pi D}
$$

Rearranging gives us:

$$
\pi = \frac{2L}{P(\text{cross}) \cdot D}
$$

For simplicity, we'll use \( L = D = 1 \), giving:

$$
\pi \approx \frac{2}{\text{Observed crossing probability}}
$$

---

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
# Plot Buffon's Needle simulation
n_drops = 50
centers = np.random.uniform(0, line_distance, n_drops)
angles = np.random.uniform(0, np.pi, n_drops)

# Calculate endpoints
x1 = centers - (needle_length / 2) * np.cos(angles)
x2 = centers + (needle_length / 2) * np.cos(angles)
y1 = (needle_length / 2) * np.sin(angles)
y2 = -(needle_length / 2) * np.sin(angles)

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

---

## Method Comparison

| Aspect              | Circle Method       | Buffon's Needle       |
|---------------------|---------------------|-----------------------|
| **Convergence Rate** | ~1/√n              | ~1/√n (but slower)    |
| **Computational Cost** | Low (simple math) | Higher (trig functions) |
| **Implementation**   | Simple             | More complex          |
| **Historical Context** | Modern Monte Carlo | 18th century problem  |
| **Visual Appeal**    | High               | Moderate              |

---


