import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

p = 0.3
q = 0.7

# X=1 represents customer clicks
# X=0 represents customer not clicks

# Possible values of X is 0 and 1

# X is discrete and has Bernouli distribution
sample_size = 20
samples = np.random.binomial( n=1, p=p, size=sample_size )

# 20 observations were generated

Probability_0 = sum(1 for x in samples if x==0)/sample_size
Probability_1 = sum(1 for x in samples if x==1)/sample_size

print("P(X=0) :",Probability_0)
print("P(X=1) :",Probability_1)

number_of_clicks = np.sum(samples == 1) 

 

number_of_non_clicks = np.sum(samples == 0) 

 

print("Number of clicks:", number_of_clicks) 

print("Number of non-clicks:", number_of_non_clicks)

x = [0, 1]
theoretical_pmf = [q, p]
empirical_pmf = [Probability_0, Probability_1]

width = 0.35

plt.bar(
    np.array(x) - width/2,
    theoretical_pmf,
    width,
    label = "Theoretical PMF"
)

plt.bar(
    np.array(x) + width/2,
    empirical_pmf,
    width,
    label= "Empirical PMF"
)

plt.xlabel("Outcome X")
plt.ylabel("Probability")
plt.title("Theoretical vs Empirical PMF")
plt.xticks(x)
plt.legend()
plt.tight_layout()
plt.show()

print("Theroritcal expectation :",p)
print("Theoritical Variance :",p*q)

empirical_expectation = np.mean(samples)
print("Empiral expectation :",empirical_expectation)
print("Empiracl Varicance :",np.var(samples))

sample_size = [10, 100, 1000, 10000]
results = []

for n in sample_size:
    samples=np.random.binomial(n=1,p=p,size=n)

    prob_0 = np.mean(samples == 0)
    prob_1 = np.mean(samples == 1)

    # Calculate empirical expectation and variance
    empirical_expectation = np.mean(samples)
    empirical_variance = np.var(samples)

    results.append({
        "Sample Size": n,
        "P(X=0)": prob_0,
        "P(X=1)": prob_1,
        "Expectation": empirical_expectation,
        "Variance": empirical_variance
    })

df = pd.DataFrame(results)

print("Theoretical Values:")
print("P(X=0):", q)
print("P(X=1):", p)
print("Expectation:", p)
print("Variance:", p * q)

print("\nEffect of Sample Size:")
print(df.round(4).to_string(index=False))

# Binomial Distribution

n=50
number_of_hours = 20000
p=0.04
q=1-p

X = np.random.binomial(n=n,p=p,size=number_of_hours)
# Display the first 20 simulated hours
print("Flagged transactions in the first 20 hours:")
print(X[:20])

# Basic summary

print("\nTotal simulated hours:", len(X))
print("Average flagged transactions per hour:", np.mean(X))
print("Minimum flagged transactions in an hour:", np.min(X))
print("Maximum flagged transactions in an hour:", np.max(X))