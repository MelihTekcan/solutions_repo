# Problem 1



### ** Central Limit Theorem: Theoretical Foundations and Empirical Verification **

### 1. Introduction and Fundamental Concepts

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
from scipy import stats

def clt_demo(population, dist_name, sizes=[5,10,30,50,100], n_sim=10000):
    """Visual CLT demonstration"""
    fig, axs = plt.subplots(2, 3, figsize=(15,10))
    for ax, n in zip(axs.flat[:-1], sizes):
        means = [np.mean(np.random.choice(population, n)) for _ in range(n_sim)]
        sns.histplot(means, kde=True, ax=ax, stat='density')
        
        # Overlay normal curve
        xmin, xmax = ax.get_xlim()
        x = np.linspace(xmin, xmax, 100)
        mu, se = np.mean(means), np.std(means)
        ax.plot(x, stats.norm.pdf(x, mu, se), 'r-', lw=2)
        
        ax.set_title(f'n={n}\nSE={se:.4f}')
    fig.suptitle(f'CLT: {dist_name} Distribution', y=1.02)
    plt.tight_layout()
    plt.show()
```

### 3.2 Test Distributions
```python
# Configuration
np.random.seed(42)

# Uniform U(0,1)
uniform_pop = np.random.uniform(0, 1, 100000)
mu_uni = 0.5
sigma_uni = np.sqrt(1/12)

# Exponential (λ=1)
exp_pop = np.random.exponential(1, 100000)
mu_exp = 1
sigma_exp = 1

# Binomial (n=10,p=0.3)
binom_pop = np.random.binomial(10, 0.3, 100000)
mu_binom = 3
sigma_binom = np.sqrt(2.1)
```


## 4. Practical Applications

### 4.1 Statistical Inference
**Confidence Intervals**:
```python
sample = np.random.choice(population, 30)
ci = np.mean(sample) ± 1.96*np.std(sample)/np.sqrt(30)
```

### 4.2 Quality Control
**Control Charts**:
- UCL = μ + 3σ/√n
- LCL = μ - 3σ/√n

### 4.3 Machine Learning
- Bootstrap sampling
- Ensemble methods
- Error estimation

## 5. Limitations and Conclusion

### 5.1 Key Constraints
- **Sample Size Requirements**:
  - Minimum n=30 for symmetric distributions
  - n≥50 for skewed distributions
- **Distribution Challenges**:
  - Heavy-tailed distributions (finite variance required)
  - Dependent data structures
- **Real-world Considerations**:
  - Sampling bias effects
  - Measurement errors