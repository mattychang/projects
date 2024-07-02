import math
from typing import Tuple

class ComplexNumber:
    def __init__(self, real: float, imag: float) -> None:
        self.real = real
        self.imag = imag

    def __str__(self) -> str:
        return f"{self.real} + {self.imag}i"

    # Adds two complex numbers.
    def __add__(self, other: 'ComplexNumber') -> 'ComplexNumber':
        return ComplexNumber(self.real + other.real, self.imag + other.imag)

    # Subtracts one complex number from another.
    def __sub__(self, other: 'ComplexNumber') -> 'ComplexNumber':
        return ComplexNumber(self.real - other.real, self.imag - other.imag)

    # Multiplies two complex numbers.
    def __mul__(self, other: 'ComplexNumber') -> 'ComplexNumber':
        real = self.real * other.real - self.imag * other.imag
        imag = self.real * other.imag + self.imag * other.real
        return ComplexNumber(real, imag)

    # Divides one complex number by another.
    def __truediv__(self, other: 'ComplexNumber') -> 'ComplexNumber':
        denom = other.real ** 2 + other.imag ** 2
        if denom == 0:
            raise ZeroDivisionError("division by zero")
        real = (self.real * other.real + self.imag * other.imag) / denom
        imag = (self.imag * other.real - self.real * other.imag) / denom
        return ComplexNumber(real, imag)

    # Calculates the magnitude of the complex number.
    def magnitude(self) -> float:
        return math.sqrt(self.real ** 2 + self.imag ** 2)

    # Returns the conjugate of the complex number.
    def conjugate(self) -> 'ComplexNumber':
        return ComplexNumber(self.real, -self.imag)

    # Converts the complex number to polar coordinates.
    def to_polar(self) -> Tuple[float, float]:
        r = self.magnitude()
        theta = math.atan2(self.imag, self.real)
        return r, theta

    # Creates a complex number from polar coordinates.
    def from_polar(self, r: float, theta: float) -> 'ComplexNumber':
        real = r * math.cos(theta)
        imag = r * math.sin(theta)
        return ComplexNumber(real, imag)

# Test cases
if __name__ == "__main__":
    c1 = ComplexNumber(2, 3)
    c2 = ComplexNumber(1, 4)

    print("Complex number c1:")
    print(c1)
    
    print("Complex number c2:")
    print(c2)
    
    print("Addition of c1 and c2:")
    print(c1 + c2)
    
    print("Subtraction of c2 from c1:")
    print(c1 - c2)
    
    print("Multiplication of c1 and c2:")
    print(c1 * c2)
    
    print("Division of c1 by c2:")
    print(c1 / c2)
    
    print("Magnitude of c1:")
    print(c1.magnitude())
    
    print("Conjugate of c1:")
    print(c1.conjugate())
    
    print("Polar coordinates of c1:")
    print(c1.to_polar())
    
    r, theta = c1.to_polar()
    print("Convert back from polar to rectangular form:")
    print(c1.from_polar(r, theta))
