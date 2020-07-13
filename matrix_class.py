import copy

class Matrix:
    def __init__(self, rows, columns, digits=None):
         self.rows = int(rows)
         self.columns = int(columns)
         if digits is None:
            self.value = [[0 for _ in range(self.columns)] for _ in range(self.rows)]
         else:
            self.value = digits
         self.size = [self.rows, self.columns]

    def add_matrix(self, other):
        if self.size != other.size:
            print("ERROR")
        result = Matrix(self.rows, self.columns)
        for i in range(self.rows):
            for j in range(self.columns):
                result.value[i][j] = self.value[i][j] + other.value[i][j]
        return result

    def multiply_by_constant(self, constant):
        result = Matrix(self.rows, self.columns)
        for i in range(self.rows):
            for j in range(self.columns):
                result.value[i][j] = self.value[i][j] * constant
        return result

    def multiply_by_matrix(self, other):
        if self.columns != other.rows:
            print("ERROR")
        result = Matrix(self.rows, other.columns)
        for i in range(self.rows):
            for j in range(other.columns):
                for k in range(self.columns):
                    result.value[i][j] += self.value[i][k] * other.value[k][j]
        return result

    def transpose_main_diagonal(self):
        result = Matrix(self.columns, self.rows)
        for i in range(result.rows):
            for j in range(result.columns):
                result.value[i][j] = self.value[j][i]
        return result

    def transpose_side_diagonal(self):
        result = Matrix(self.columns, self.rows)
        for i in range(result.rows):
            for j in range(result.columns):
                result.value[i][j] = self.value[~j][~i]
        return result

    def transpose_vertical(self):
        result = Matrix(self.rows, self.columns)
        for i in range(result.rows):
            for j in range(result.columns):
                result.value[i][j] = self.value[i][~j]
        return result

    def transpose_horizontal(self):
        result = Matrix(self.rows, self.columns)
        for i in range(result.rows):
            for j in range(result.columns):
                result.value[i][j] = self.value[~i][j]
        return result

    @staticmethod
    def get_minor(matrix, row_pos, col_pos):
        return [row[:col_pos] + row[col_pos+1:] for row in matrix[:row_pos] + matrix[row_pos+1:]]

    @staticmethod
    def get_determinant(matrix):
        if len(matrix) != len(matrix[0]):
            print("Remember only square matrices have determinants.")
        else:
            if len(matrix) == 1:
                return matrix[0][0]
            if len(matrix) == 2:
                result = matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]
                return result
            determinant = 0
            for column in range(len(matrix)):
                minor = Matrix.get_minor(matrix, 0, column)
                determinant += ((-1) ** column) * matrix[0][column] * Matrix.get_determinant(minor)
            return determinant

    @staticmethod
    def get_inverse(matrix):
        determinant = Matrix.get_determinant(matrix)
        if determinant == 0:
            print("This matrix doesn't have an inverse")
            exit()
        if len(matrix) == 2:
            return [[matrix[1][1]/determinant, (-1) * matrix[0][1]/determinant],
                [(-1) * matrix[1][0]/determinant, matrix[0][0]/determinant]]
        cofactors = []
        for i in range(len(matrix)):
            cofactor_i = []
            for j in range(len(matrix[0])):
                minor = Matrix.get_minor(matrix, i, j)
                cofactor_i .append(((-1) ** (i+j)) * Matrix.get_determinant(minor))
            cofactors.append(cofactor_i)
        cofactors = list(map(list, zip(*cofactors)))
        for i in range(len(cofactors)):
            for j in range(len(cofactors[0])):
                    cofactors[i][j] = cofactors[i][j]/determinant
        return Matrix(len(cofactors), len(cofactors[0]), cofactors)


    def get_output(self):
        for i in range(self.rows):
            print(*self.value[i])

def select_choice():
    selection = True
    while selection:
        menu = "1. Add matrices\n2. Multiply matrix by a constant\n3. Multiply matrices\n4. Transpose matrix\n5. Calculate a determinant\n6. Inverse matrix\n0. Exit"
        print(menu)
        choice = int(input("Your choice:"))
        if choice == 1:
            print("Enter size of first matrix:")
            try:
                rows1, columns1 = input().split(" ")
            except ValueError:
                print("Please indicate two values(rows and columns)")
                exit()
            print("Enter first matrix:")
            digits1 = [[float(x) for x in input().split(" ")] for i in range(int(rows1))]
            matrix1 = Matrix(rows1, columns1, digits1)
            print("Enter size of second matrix:")
            rows2, columns2 = input().split(" ")
            print("Enter second matrix:")
            digits2 =  [[float(x) for x in input().split(" ")] for i in range(int(rows2))]
            matrix2 = Matrix(rows2, columns2, digits2)
            result = matrix1.add_matrix(matrix2)
            print("The result is:")
            result.get_output()
        elif choice == 2:
            print("Enter size of matrix:")
            try:
                rows1, columns1 = input().split(" ")
            except ValueError:
                print("Please indicate two values(rows and columns)")
                exit()
            print("Enter matrix:")
            digits1 = [[float(x) for x in input().split(" ")] for i in range(int(rows1))]
            matrix1 = Matrix(rows1, columns1, digits1)
            print("Enter constant:")
            constant = float(input())
            result = matrix1.multiply_by_constant(constant)
            print("The result is:")
            result.get_output()
        elif choice == 3:
            print("Enter size of first matrix:")
            try:
                rows1, columns1 = input().split(" ")
            except ValueError:
                print("Please indicate two values(rows and columns)")
                exit()
            print("Enter first matrix:")
            digits1 = [[float(x) for x in input().split(" ")] for i in range(int(rows1))]
            matrix1 = Matrix(rows1, columns1, digits1)
            print("Enter size of second matrix:")
            rows2, columns2 = input().split(" ")
            print("Enter second matrix:")
            digits2 =  [[float(x) for x in input().split(" ")] for i in range(int(rows2))]
            matrix2 = Matrix(rows2, columns2, digits2)
            result = matrix1.multiply_by_matrix(matrix2)
            print("The result is:")
            result.get_output()
        elif choice == 4:
            sub_menu = print("1. Main diagonal\n2. Side diagonal\n3. Vertical line\n4. Horizontal line")
            sub_choice = int(input("Your choice:"))
            if sub_choice == 1:
                print("Enter size of matrix:")
                try:
                    rows1, columns1 = input().split(" ")
                except ValueError:
                    print("Please indicate two values(rows and columns)")
                    exit()
                print("Enter matrix:")
                digits1 = [[float(x) for x in input().split(" ")] for i in range(int(rows1))]
                matrix1 = Matrix(rows1, columns1, digits1)
                result = matrix1.transpose_main_diagonal()
                print("The result is:")
                result.get_output()
            elif sub_choice == 2:
                print("Enter size of matrix:")
                try:
                    rows1, columns1 = input().split(" ")
                except ValueError:
                    print("Please indicate two values(rows and columns)")
                    exit()
                print("Enter matrix:")
                digits1 = [[float(x) for x in input().split(" ")] for i in range(int(rows1))]
                matrix1 = Matrix(rows1, columns1, digits1)
                result = matrix1.transpose_side_diagonal()
                print("The result is:")
                result.get_output()
            elif sub_choice == 3:
                print("Entre size of matrix:")
                try:
                    rows1, columns1 = input().split(" ")
                except ValueError:
                    print("Please indicate two values(rows and columns)")
                    exit()
                print("Enter matrix:")
                digits1 = [[float(x) for x in input().split(" ")] for i in range(int(rows1))]
                matrix1 = Matrix(rows1, columns1, digits1)
                result = matrix1.transpose_vertical()
                print("The result is:")
                result.get_output()
            elif sub_choice == 4:
                print("Entre size of matrix:")
                try:
                    rows1, columns1 = input().split(" ")
                except ValueError:
                    print("Please indicate two values(rows and columns)")
                    exit()
                print("Enter matrix:")
                digits1 = [[float(x) for x in input().split(" ")] for i in range(int(rows1))]
                matrix1 = Matrix(rows1, columns1, digits1)
                result = matrix1.transpose_horizontal()
                print("The result is:")
                result.get_output()
        elif choice == 5:
            print("Enter size of matrix:")
            try:
                rows1, columns1 = input().split(" ")
            except ValueError:
                print("Please indicate two values(rows and columns)")
                exit()
            if rows1 != columns1:
                print("Remember that only square matrices have determinants.")
                exit()
            else:
                print("Enter matrix:")
                digits1 = [[float(x) for x in input().split(" ")] for i in range(int(rows1))]
                matrix1 = Matrix(rows1, columns1, digits1)
                result = matrix1.get_determinant(matrix1.value)
                print("The result is:")
                print(result)
        elif choice == 6:
            print("Enter size of matrix:")
            try:
                rows1, columns1 = input().split(" ")
            except ValueError:
                print("Please indicate two values(rows and columns)")
                exit()
            if rows1 != columns1:
                print("Remember that only square matrices have inverse.")
                exit()
            else:
                print("Enter matrix:")
                digits1 = [[float(x) for x in input().split(" ")] for i in range(int(rows1))]
                matrix1 = Matrix(rows1, columns1, digits1)
                result = matrix1.get_inverse(matrix1.value)
                print("The result is:")
                result.get_output()
        else:
            selection = False

select_choice()
