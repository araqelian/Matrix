from Matrix import Matrix

if __name__ == "__main__":
    try:
        print("\033[92m check printing matrix object (__str__)\033[00m")

        m = Matrix([[1, 2], [3, 4]])
        print(m, end='\n\n')


        print("\033[92m check matrix addition (__add__)\033[00m")
        m1 = Matrix([[1, 2], [3, 4]])
        m2 = Matrix([[5, 6], [7, 8]])
        result = m1 + m2
        print(result, end='\n\n')


        print("\033[92m check scalar multiplication and matrix multiplication (__mul__ and __matmul__)\033[00m")
        
        
        m3 = Matrix([[1, 2], [3, 4]])
        m4 = Matrix([[5, 6], [7, 8]])
        scalar = 2
        result1 = m3 * scalar
        result2 = m3 * m4
        print(result1)
        print(result2, end='\n\n')



        print("\033[92m check transpose of a matrix (transpose)\033[00m")
        
        m5 = Matrix([[1, 2, 3], [4, 5, 6]])
        result = m.transpose()
        print(result)

    except Exception as err:
        print(err)
