import math
from collections import Counter
from typing import List

class StatisticsAndProbability:

    # Calculates the mean (average) of a list of numbers.
    def mean(self, data: List[float]) -> float:
        return sum(data) / len(data)

    # Calculates the median of a list of numbers.
    def median(self, data: List[float]) -> float:
        sorted_data = sorted(data)
        n = len(sorted_data)
        mid = n // 2
        if n % 2 == 0:
            return (sorted_data[mid - 1] + sorted_data[mid]) / 2
        else:
            return sorted_data[mid]

    # Calculates the mode(s) of a list of numbers.
    def mode(self, data: List[float]) -> List[float]:
        counts = Counter(data)
        max_count = max(counts.values())
        return [key for key, count in counts.items() if count == max_count]

    # Calculates the variance of a list of numbers.
    def variance(self, data: List[float]) -> float:
        m = self.mean(data)
        return sum((x - m) ** 2 for x in data) / len(data)

    # Calculates the standard deviation of a list of numbers.
    def standard_deviation(self, data: List[float]) -> float:
        return math.sqrt(self.variance(data))

    # Calculates the factorial of a number.
    def factorial(self, n: int) -> int:
        if n == 0:
            return 1
        return n * self.factorial(n - 1)

    # Calculates the number of combinations (n choose k).
    def combinations(self, n: int, k: int) -> int:
        return self.factorial(n) // (self.factorial(k) * self.factorial(n - k))

    # Calculates the number of permutations (nPk).
    def permutations(self, n: int, k: int) -> int:
        return self.factorial(n) // self.factorial(n - k)

    # Calculates the probability of k successes in n trials with probability p.
    def binomial_probability(self, n: int, k: int, p: float) -> float:
        return self.combinations(n, k) * (p ** k) * ((1 - p) ** (n - k))

# Test cases
if __name__ == "__main__":
    stats_prob = StatisticsAndProbability()
    data = [1, 2, 2, 3, 4]
    
    # Statistical functions tests
    print("Mean of data:")
    print(stats_prob.mean(data))
    
    print("Median of data:")
    print(stats_prob.median(data))
    
    print("Mode of data:")
    print(stats_prob.mode(data))
    
    print("Variance of data:")
    print(stats_prob.variance(data))
    
    print("Standard Deviation of data:")
    print(stats_prob.standard_deviation(data))
    
    # Probability functions tests
    print("5 factorial:")
    print(stats_prob.factorial(5))
    
    print("Combinations (5 choose 3):")
    print(stats_prob.combinations(5, 3))
    
    print("Permutations (5P3):")
    print(stats_prob.permutations(5, 3))
    
    print("Binomial probability (5 trials, 3 successes, probability 0.5):")
    print(stats_prob.binomial_probability(5, 3, 0.5))
