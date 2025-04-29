# Problem 1

## **Measurements and Uncertainties: Fundamental Physics and Mathematical Approaches**

## Introduction

In physics and other scientific disciplines, measurements are the building blocks of our understanding of nature. However, no measurement is perfect - every measurement contains some uncertainty. Understanding the sources of these uncertainties is vital for correctly interpreting measurements and reliably presenting results.

This document examines the fundamentals of measurement uncertainties, their types, mathematical models, and simulation methods.

---

## 1. What is Measurement Uncertainty?

Measurement uncertainty is a measure of how much a measurement might deviate from the true value. No measuring instrument is perfect, and every measurement process contains various sources of error.

**Example**: Let's imagine measuring the length of a pencil with a ruler. If the smallest division on the ruler is 1 mm, the uncertainty of our measurement will be approximately ±0.5 mm.

---

## 2. Types of Uncertainties

### 2.1 Systematic Errors

Systematic errors are consistent biases that affect measurements in the same direction:

- **Instrument error**: Comes from calibration issues
- **Method error**: Results from flaws in the measurement technique
- **Environmental factors**: Temperature, humidity, etc.

```python
import numpy as np
import matplotlib.pyplot as plt

# Systematic error simulation
true_value = 10.0
systematic_error = 0.5  # Constant +0.5 error

measurements = np.random.normal(0, 0.2, 100) + true_value + systematic_error

plt.figure(figsize=(8, 5))
plt.hist(measurements, bins=20)
plt.axvline(x=true_value, color='r', linestyle='--', label='True Value')
plt.axvline(x=np.mean(measurements), color='g', linestyle='--', label='Measurement Mean')
plt.xlabel('Measurement Value')
plt.ylabel('Frequency')
plt.legend()
plt.title('Effect of Systematic Error')
plt.show()
```

---

### 2.2 Random Errors

Random errors are unpredictable fluctuations that vary between measurements:

- **Observer error**: Small differences from the person taking measurements
- **Instrument precision**: Natural fluctuations of measuring devices
- **Environmental noise**: Uncontrollable external factors

```python
import numpy as np
import matplotlib.pyplot as plt

# Random error simulation
true_value = 10.0
random_errors = np.random.normal(0, 0.5, 100)  # Mean 0, std dev 0.5
random_measurements = true_value + random_errors

plt.figure(figsize=(8, 5))
plt.hist(random_measurements, bins=20)
plt.axvline(x=true_value, color='r', linestyle='--', label='True Value')
plt.axvline(x=np.mean(random_measurements), color='g', linestyle='--', label='Measurement Mean')
plt.xlabel('Measurement Value')
plt.ylabel('Frequency')
plt.legend()
plt.title('Effect of Random Error')
plt.show()
```

---

## 3. Mathematical Representation of Uncertainties

### 3.1 Absolute and Relative Uncertainty

- **Absolute uncertainty (Δx)**: Absolute value of potential deviation from true value  
  Example: 15.2 ± 0.3 cm → Δx = 0.3 cm

- **Relative uncertainty**: Ratio of absolute uncertainty to measured value  
  Relative uncertainty = Δx / x  
  Example: 0.3 / 15.2 ≈ 0.02 or 2%

```python
# Relative uncertainty calculation
import numpy as np

measurement = 15.2
absolute_uncertainty = 0.3
relative_uncertainty = absolute_uncertainty / measurement

print(f"Absolute uncertainty: {absolute_uncertainty}")
print(f"Relative uncertainty: {relative_uncertainty:.4f} or {relative_uncertainty*100:.2f}%")
```

---

### 3.2 Standard Deviation and Standard Error

- **Standard deviation (σ)**: Measure of how spread out data points are  
- **Standard error (SE)**: Uncertainty of the mean, SE = σ/√n

```python
import numpy as np

# Standard deviation and error calculation
data = np.array([9.8, 10.2, 10.0, 9.9, 10.1, 9.7, 10.3, 10.0, 9.8, 10.2])

mean = np.mean(data)
std_dev = np.std(data, ddof=1)  # ddof=1 for sample standard deviation
std_error = std_dev / np.sqrt(len(data))

print(f"Mean: {mean:.2f}")
print(f"Standard deviation: {std_dev:.4f}")
print(f"Standard error: {std_error:.4f}")
```

---

## 4. Propagation of Uncertainties

### 4.1 Addition/Subtraction Operations

Absolute uncertainties combine as root sum of squares:  
Δz = √(Δx² + Δy²)

### 4.2 Multiplication/Division Operations

Relative uncertainties combine as root sum of squares:  
Δz/z = √((Δx/x)² + (Δy/y)²)

```python
import numpy as np

# Uncertainty propagation calculation
x, dx = 10.0, 0.2
y, dy = 5.0, 0.1

# Addition
z_sum = x + y
dz_sum = np.sqrt(dx**2 + dy**2)

# Multiplication
z_prod = x * y
dz_prod = z_prod * np.sqrt((dx/x)**2 + (dy/y)**2)

print(f"Sum: {z_sum:.2f} ± {dz_sum:.2f}")
print(f"Product: {z_prod:.2f} ± {dz_prod:.2f}")
```

---

## 5. Graphical Representation of Uncertainties

### 5.1 Error Bars

```python
import numpy as np
import matplotlib.pyplot as plt

# Error bar example
x_data = np.array([1, 2, 3, 4, 5])
y_data = np.array([2.1, 3.9, 6.2, 8.1, 9.8])
y_error = np.array([0.3, 0.4, 0.2, 0.5, 0.3])

plt.figure(figsize=(8, 5))
plt.errorbar(x_data, y_data, yerr=y_error, fmt='o', capsize=5)
plt.xlabel('X Values')
plt.ylabel('Y Values')
plt.title('Measurement Graph with Error Bars')
plt.grid(True)
plt.show()
```


---

### 5.2 Confidence Intervals

```python
import numpy as np
import matplotlib.pyplot as plt

# Confidence interval simulation
np.random.seed(42)
data = np.random.normal(50, 5, 100)  # Mean 50, std dev 5

mean = np.mean(data)
std_error = np.std(data, ddof=1) / np.sqrt(len(data))
confidence_interval = 1.96 * std_error  # 95% confidence

print(f"Mean: {mean:.2f}")
print(f"95% Confidence Interval: {mean:.2f} ± {confidence_interval:.2f}")

plt.figure(figsize=(8, 5))
plt.hist(data, bins=20, alpha=0.7)
plt.axvline(x=mean, color='r', label='Mean')
plt.axvline(x=mean - confidence_interval, color='g', linestyle='--', label='Confidence Interval')
plt.axvline(x=mean + confidence_interval, color='g', linestyle='--')
plt.legend()
plt.title('Measurement Distribution and Confidence Interval')
plt.show()
```

---

## 6. Reporting Measurement Uncertainties

In scientific work, measurement results are typically reported as:

- **Significant figures rule**: Uncertainty given with at most 2 significant figures
- **Rounding**: Measurement value rounded to match uncertainty precision
- **Units**: Both measurement and uncertainty have same units

**Correct examples**:
- (15.24 ± 0.05) cm
- (1.057 ± 0.003) g

**Incorrect examples**:
- 15.235 ± 0.05 cm (measurement too precise)
- 15.2 ± 0.053 cm (uncertainty too precise)

---

## 7. Monte Carlo Simulation for Uncertainty Analysis

```python
import numpy as np
import matplotlib.pyplot as plt

# Monte Carlo simulation for uncertainty analysis
def model_calculation(a, b):
    return a * np.exp(-b)

# True parameters
a_true, b_true = 2.0, 0.5

# Measurement uncertainties
a_meas, a_unc = 2.1, 0.1
b_meas, b_unc = 0.52, 0.02

# Monte Carlo simulation
n_simulations = 10000
a_sim = np.random.normal(a_meas, a_unc, n_simulations)
b_sim = np.random.normal(b_meas, b_unc, n_simulations)
results = model_calculation(a_sim, b_sim)

# Analysis
mean_result = np.mean(results)
std_result = np.std(results)
conf_interval = np.percentile(results, [2.5, 97.5])  # 95% CI

print(f"Model output mean: {mean_result:.4f}")
print(f"Standard deviation: {std_result:.4f}")
print(f"95% confidence interval: [{conf_interval[0]:.4f}, {conf_interval[1]:.4f}]")

# Histogram
plt.figure(figsize=(8, 5))
plt.hist(results, bins=50, density=True, alpha=0.7)
plt.axvline(x=mean_result, color='r', label='Mean')
plt.axvline(x=conf_interval[0], color='g', linestyle='--', label='95% CI')
plt.axvline(x=conf_interval[1], color='g', linestyle='--')
plt.xlabel('Model Output')
plt.ylabel('Probability Density')
plt.title('Uncertainty Analysis with Monte Carlo Simulation')
plt.legend()
plt.show()
```

---

## 8. Practical Recommendations and Conclusion

### Before measurement:
- Calibrate instruments
- Understand the measurement method thoroughly
- Control or record environmental factors

### During measurement:
- Take multiple measurements
- Note potential systematic error sources
- Don't discard unexpected results without investigation

### Data analysis:
- Calculate uncertainties correctly
- Use appropriate statistical methods
- Report results clearly and transparently

Understanding and properly reporting measurement uncertainties is critical for the reliability of scientific work. By properly managing these uncertainties, we can obtain more reliable results and contribute to scientific progress.

