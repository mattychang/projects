class Numbers:

    def __init__(self) -> None:
        pass

    # Performs prime factorization of a given number
    def prime_factorization(self, num: int) -> None:
        x = num - 1
        while x > 1:
            if num % x == 0:
                self.prime_factorization(x)
                self.prime_factorization(num // x)
                return
            x -= 1
        print(int(num))

    # Computes the greatest common divisor (GCD) of two numbers
    def gcd(self, a: int, b: int) -> int:
        while b:
            a, b = b, a % b
        return a

    # Computes the least common multiple (LCM) of two numbers
    def lcm(self, a: int, b: int) -> int:
        return a * b // self.gcd(a, b)

    # Checks if a number is prime
    def is_prime(self, num: int) -> bool:
        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    # Generates all prime numbers up to a given limit using the Sieve of Eratosthenes
    def generate_primes(self, limit: int) -> list[int]:
        sieve = [True] * (limit + 1)
        sieve[0], sieve[1] = False, False  # 0 and 1 are not prime numbers
        for start in range(2, int(limit ** 0.5) + 1):
            if sieve[start]:
                for multiple in range(start * start, limit + 1, start):
                    sieve[multiple] = False
        return [num for num in range(limit + 1) if sieve[num]]

    # Finds all factors of a given number
    def factors(self, num: int) -> list[int]:
        result = []
        for i in range(1, int(num ** 0.5) + 1):
            if num % i == 0:
                result.append(i)
                if i != num // i:
                    result.append(num // i)
        result.sort()
        return result


# Test cases
if __name__ == "__main__":
    num_ops = Numbers()

    # Test prime factorization
    print("Prime factorization of 56:")
    num_ops.prime_factorization(56)

    # Test GCD
    print("GCD of 48 and 18:")
    print(num_ops.gcd(48, 18))

    # Test LCM
    print("LCM of 48 and 18:")
    print(num_ops.lcm(48, 18))

    # Test is_prime
    print("Check if 29 is prime:")
    print(num_ops.is_prime(29))

    print("Check if 28 is prime:")
    print(num_ops.is_prime(28))

    # Test generate_primes
    print("Prime numbers up to 50:")
    print(num_ops.generate_primes(50))

    # Test factors
    print("Factors of 28:")
    print(num_ops.factors(28))
