# StatisticsAndProbability.py

import math
from collections import Counter
from typing import List

# Calculates the mean (average) of a list of numbers.
def mean(data: List[float]) -> float:
    return sum(data) / len(data)

# Calculates the median of a list of numbers.
def median(data: List[float]) -> float:
    sorted_data = sorted(data)
    n = len(sorted_data)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_data[mid - 1] + sorted_data[mid]) / 2
    else:
        return sorted_data[mid]

# Calculates the mode(s) of a list of numbers.
def mode(data: List[float]) -> List[float]:
    counts = Counter(data)
    max_count = max(counts.values())
    return [key for key, count in counts.items() if count == max_count]

# Calculates the variance of a list of numbers.
def variance(data: List[float]) -> float:
    m = mean(data)
    return sum((x - m) ** 2 for x in data) / len(data)

# Calculates the standard deviation of a list of numbers.
def standard_deviation(data: List[float]) -> float:
    return math.sqrt(variance(data))

# Calculates the factorial of a number.
def factorial(n: int) -> int:
    if n == 0:
        return 1
    return n * factorial(n - 1)

# Calculates the number of combinations (n choose k).
def combinations(n: int, k: int) -> int:
    return factorial(n) // (factorial(k) * factorial(n - k))

# Calculates the number of permutations (nPk).
def permutations(n: int, k: int) -> int:
    return factorial(n) // factorial(n - k)

# Calculates the probability of k successes in n trials with probability p.
def binomial_probability(n: int, k: int, p: float) -> float:
    return combinations(n, k) * (p ** k) * ((1 - p) ** (n - k))

# Test cases
if __name__ == "__main__":
    data = [1, 2, 2, 3, 4]
    
    # Statistical functions tests
    print("Mean of data:")
    print(mean(data))
    
    print("Median of data:")
    print(median(data))
    
    print("Mode of data:")
    print(mode(data))
    
    print("Variance of data:")
    print(variance(data))
    
    print("Standard Deviation of data:")
    print(standard_deviation(data))
    
    # Probability functions tests
    print("5 factorial:")
    print(factorial(5))
    
    print("Combinations (5 choose 3):")
    print(combinations(5, 3))
    
    print("Permutations (5P3):")
    print(permutations(5, 3))
    
    print("Binomial probability (5 trials, 3 successes, probability 0.5):")
    print(binomial_probability(5, 3, 0.5))
