# Problem 1

### **Central Limit Theorem: Theoretical Foundations and Empirical Verification**

## 1. Introduction and Fundamental Concepts

### 1.1 Core Principle
The Central Limit Theorem (CLT) establishes that the sampling distribution of the mean will approximate a normal distribution as sample size increases, regardless of the population's original distribution shape.

### 1.2 Mathematical Formulation
$$
\frac{\overline{X}_n - \mu}{\sigma/\sqrt{n}} \xrightarrow{d} N(0,1) \quad \text{as} \quad n \to \infty
$$

### 1.3 Key Implications
- Applies to both normal and non-normal populations
- Enables reliable statistical inference
- Forms foundation for confidence intervals and hypothesis tests
- Standard error decreases as SE = σ/√n

## 2. Theoretical Foundations

### 2.1 Historical Development
- 1733: Initial concepts by Abraham de Moivre
- 1812: Formalization by Pierre-Simon Laplace
- 1901: Rigorous proof by Aleksandr Lyapunov

### 2.2 Critical Assumptions
1. **Independence**: Random sampling
2. **Identical Distribution**: i.i.d. variables
3. **Finite Variance**: σ² < ∞

### 2.3 Convergence Properties
Berry-Esseen Theorem quantifies convergence rate:
$$
\sup_x |F_n(x) - Φ(x)| ≤ \frac{Cρ}{σ^3\sqrt{n}}
$$
where ρ = E[|X-μ|³]

## 3. Simulation Methodology

### 3.1 Python Implementation
```python
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import norm

def clt_demo(population, dist_name, sizes=[5, 10, 30, 50, 100], n_sim=10000):
    
    # Determine the number of rows and columns for subplots dynamically
    num_plots = len(sizes)
    rows = (num_plots + 2) // 3
    fig, axs = plt.subplots(rows, 3, figsize=(15, 5 * rows))
    axs = axs.flatten()

    for i, n in enumerate(sizes):
        # Generate sampling distribution of the mean
        means = [np.mean(np.random.choice(population, n, replace=True)) for _ in range(n_sim)]
        
        # Plot histogram of sample means
        sns.histplot(means, kde=True, ax=axs[i], stat='density', color='blue', label='Sample Means')
        
        # Overlay the theoretical normal distribution
        mu, se = np.mean(means), np.std(means)
        x = np.linspace(min(means), max(means), 100)
        axs[i].plot(x, norm.pdf(x, mu, se), 'r-', lw=2, label='Normal Approximation')
        
        # Add title and labels
        axs[i].set_title(f'Sample Size: n={n}\nSE={se:.4f}')
        axs[i].legend()

    # Hide unused subplots
    for j in range(len(sizes), len(axs)):
        axs[j].axis('off')

    # Add a main title and adjust layout
    fig.suptitle(f'Central Limit Theorem Demonstration: {dist_name} Distribution', fontsize=16, y=0.95)
    plt.tight_layout(rect=[0, 0, 1, 0.95])
    plt.show()
```

### 3.2 Test Distributions
```python
# Configuration
np.random.seed(42)

# Uniform Distribution U(0,1)
uniform_pop = np.random.uniform(0, 1, 100000)
clt_demo(uniform_pop, "Uniform")

# Exponential Distribution (λ=1)
exp_pop = np.random.exponential(1, 100000)
clt_demo(exp_pop, "Exponential")

# Binomial Distribution (n=10, p=0.3)
binom_pop = np.random.binomial(10, 0.3, 100000)
clt_demo(binom_pop, "Binomial")
```

## 4. Practical Applications

### 4.1 Statistical Inference
**Confidence Intervals**:
```python
sample = np.random.choice(population, 30)
ci = np.mean(sample) ± 1.96 * np.std(sample) / np.sqrt(30)
```

### 4.2 Quality Control
**Control Charts**:
- UCL = μ + 3σ/√n
- LCL = μ - 3σ/√n

### 4.3 Machine Learning
- Bootstrap sampling
- Ensemble methods
- Error estimation