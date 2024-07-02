class MatrixOperations:

    def __init__(self) -> None:
        pass

    # Multiplies two matrices
    def multiply(self, m1: list[list[float]], m2: list[list[float]]) -> list[list[float]] | None:
        # Ensure matrices are compatible for multiplication
        if len(m1[0]) != len(m2):
            print("Matrices are incompatible for multiplication.")
            return None
        # Initialize the result matrix
        result = [[0 for _ in range(len(m2[0]))] for _ in range(len(m1))]
        # Perform matrix multiplication
        for i in range(len(m1)):
            for j in range(len(m2[0])):
                result[i][j] = sum(m1[i][k] * m2[k][j] for k in range(len(m2)))
        return result

    # Adds two matrices
    def add(self, m1: list[list[float]], m2: list[list[float]]) -> list[list[float]] | None:
        # Ensure matrices are compatible for addition
        if len(m1) != len(m2) or len(m1[0]) != len(m2[0]):
            print("Matrices are incompatible for addition.")
            return None
        # Initialize the result matrix
        result = [[m1[i][j] + m2[i][j] for j in range(len(m1[0]))] for i in range(len(m1))]
        return result

    # Subtracts two matrices
    def subtract(self, m1: list[list[float]], m2: list[list[float]]) -> list[list[float]] | None:
        # Ensure matrices are compatible for subtraction
        if len(m1) != len(m2) or len(m1[0]) != len(m2[0]):
            print("Matrices are incompatible for subtraction.")
            return None
        # Initialize the result matrix
        result = [[m1[i][j] - m2[i][j] for j in range(len(m1[0]))] for i in range(len(m1))]
        return result

    # Calculates the determinant of a matrix
    def determ(self, mat: list[list[float]]) -> float | None:
        # Ensure the matrix is square
        if len(mat) != len(mat[0]):
            print("Matrix is not square.")
            return None
        # Use recursion to calculate the determinant
        det = self.determ_helper(mat, 1)
        return det

    # Helper function for determinant calculation
    def determ_helper(self, mat: list[list[float]], load: float) -> float:
        # Base case: 2x2 matrix
        if len(mat) == 2:
            return load * ((mat[1][1] * mat[0][0]) - (mat[0][1] * mat[1][0]))
        # Calculate determinant for larger matrices
        sum = 0
        for i in range(len(mat)):
            temp_mat = self.partition(mat, 0, i)
            adder = self.determ_helper(temp_mat, mat[0][i])
            sum += adder if i % 2 == 0 else -adder
        return sum * load

    # Partitions the matrix into a smaller one by removing a specified row and column
    def partition(self, mat: list[list[float]], ival: int, jval: int) -> list[list[float]]:
        return [[mat[i][j] for j in range(len(mat[0])) if j != jval] for i in range(len(mat)) if i != ival]

    # Calculates the adjugate of a matrix
    def adjugate(self, mat: list[list[float]]) -> list[list[float]] | None:
        # Ensure the matrix is square
        if len(mat) != len(mat[0]):
            print("Matrix is not square.")
            return None
        # Initialize the result matrix
        result = [[0 for _ in range(len(mat))] for _ in range(len(mat))]
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                mat2 = self.partition(mat, i, j)
                fact = 1 if (i + j) % 2 == 0 else -1
                result[i][j] = self.determ_helper(mat2, fact)
        return self.transpose(result)

    # Transposes a matrix
    def transpose(self, mat: list[list[float]]) -> list[list[float]]:
        return [[mat[j][i] for j in range(len(mat))] for i in range(len(mat[0]))]

    # Performs scalar multiplication on a matrix
    def scalar(self, mat: list[list[float]], scalar: float) -> list[list[float]]:
        return [[round(mat[i][j] * scalar, 2) for j in range(len(mat[0]))] for i in range(len(mat))]

    # Calculates the inverse of a matrix
    def inverse(self, mat: list[list[float]]) -> list[list[float]] | None:
        adj = self.adjugate(mat)
        if adj is None:
            print("Matrix is not square and cannot have an adjugate.")
            return None
        det = self.determ_helper(mat, 1)
        if det == 0:
            print("Matrix is singular and cannot be inverted.")
            return None
        return self.scalar(adj, 1 / det)

    # Multiplies a row by a scalar
    def row_scalar(self, mat: list[list[float]], row: int, scal: float) -> list[list[float]]:
        mat[row] = self.list_scal(mat[row], scal)
        return mat

    # Adds a multiple of one row to another row
    def row_add(self, mat: list[list[float]], row: int, to_add: int, fact: float) -> list[list[float]]:
        mat[row] = self.list_add(mat[row], mat[to_add], fact)
        return mat

    # Multiplies a list by a scalar
    def list_scal(self, lst: list[float], scal: float) -> list[float]:
        return [round(x * scal, 2) for x in lst]

    # Adds two lists (one multiplied by a scalar)
    def list_add(self, lst1: list[float], lst2: list[float], fact: float) -> list[float]:
        return [lst1[i] + round(lst2[i] * fact, 2) for i in range(len(lst1))]

    # Reduces a matrix to row-reduced echelon form (RREF)
    def rref(self, mat: list[list[float]]) -> list[list[float]] | None:
        # Ensure the matrix has more columns than rows
        if len(mat) >= len(mat[0]):
            print("Matrix is incompatible for RREF.")
            return None
        # Make lower triangular
        for i in range(len(mat)):
            for j in range(len(mat)):
                if i < j:
                    mat = self.row_add(mat, j, i, -mat[j][i])
                elif i == j:
                    mat = self.row_scalar(mat, j, 1 / mat[j][i])
        # Make upper triangular
        for i in range(len(mat)):
            for j in range(len(mat)):
                if i > j:
                    mat = self.row_add(mat, j, i, -mat[j][i])
        return mat


# Test cases
if __name__ == "__main__":
    mo = MatrixOperations()

    # Test addition
    m1 = [[1, 2], [3, 4]]
    m2 = [[5, 6], [7, 8]]
    print("Addition of m1 and m2:")
    print(mo.add(m1, m2))

    # Test subtraction
    print("Subtraction of m2 from m1:")
    print(mo.subtract(m1, m2))

    # Test multiplication
    print("Multiplication of m1 and m2:")
    print(mo.multiply(m1, m2))

    # Test determinant
    print("Determinant of m1:")
    print(mo.determ(m1))

    # Test transpose
    print("Transpose of m1:")
    print(mo.transpose(m1))

    # Test scalar multiplication
    print("Scalar multiplication of m1 by 2:")
    print(mo.scalar(m1, 2))

    # Test adjugate
    print("Adjugate of m1:")
    print(mo.adjugate(m1))

    # Test inverse
    print("Inverse of m1:")
    print(mo.inverse(m1))

    # Test row operations
    print("Row scalar multiplication of first row of m1 by 2:")
    print(mo.row_scalar(m1, 0, 2))

    print("Row addition of first row multiplied by 2 to second row of m1:")
    print(mo.row_add(m1, 1, 0, 2))

    # Test RREF
    m3 = [[1, 2, 1], [2, 4, 0], [0, 1, 1]]
    print("RREF of m3:")
    print(mo.rref(m3))
