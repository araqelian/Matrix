from typing import List, Union

class Matrix:
    def __init__(self, matrix: List[List[Union[int, float]]]):
        self.matrix = matrix
        self.rows = len(self.matrix)
        self.columns = len(self.matrix[0])

        for line in self.matrix:
            if len(line) != self.columns:
                raise TypeError("Error!\nAll columns of the matrix must be equal to each other.")

    def __add__(self, other: "Matrix") -> "Matrix":
        if self.rows == other.rows and self.columns == other.columns:
            result = []
            for i in range(self.rows):
                row = []
                for j in range(self.columns):
                    row.append(self.matrix[i][j] + other.matrix[i][j])
                result.append(row)

            return Matrix(result)
        else:
            raise ValueError("Error!\nMatrix dimensions are not compatible for addition.")

    def __str__(self) -> str:
        str_matrix = ""
        for el in self.matrix:
            str_matrix += "\t".join(str(i) for i in el)
            str_matrix += "\n"

        return str_matrix

    def __mul__(self, other: Union["Matrix", int, float]) -> "Matrix":

            if isinstance(other, (int, float)):
                result = []

                for i in range(self.rows):
                    row = []
                    for j in range(self.columns):
                        row.append(other * self.matrix[i][j])
                    result.append(row)

                return Matrix(result)

            if isinstance(other, Matrix):
                if other.rows == self.columns:
                    result = []

                    for i in range(self.rows):
                        row = []
                        for j in range(other.columns):
                            element = 0
                            for k in range(self.columns):
                                element += self.matrix[i][k] * other.matrix[k][j]
                            row.append(element)
                        result.append(row)

                    return Matrix(result)
                else:
                    raise ValueError("Error!\nMatrix dimensions are not compatible for multiplication.")

            raise TypeError("Error!\nUnsupported operand type for multiplication.")

    def __matmul__(self, other: "Matrix") -> "Matrix":
        return self.__mul__(other)

    def transpose(self) -> "Matrix":
        result = []

        for i in range(self.columns):
            row = []
            for j in range(self.rows):
                row.append(self.matrix[j][i])
            result.append(row)

        return Matrix(result)
