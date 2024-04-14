from math import gcd
class Fraction:
    def __init__(self, numerator, denominator=1):
        common_divisor = gcd(numerator, denominator)
        self.numerator = numerator // common_divisor
        self.denominator = denominator // common_divisor
        if self.denominator < 0:
            self.numerator = 0 - self.numerator
            self.denominator = 0 - self.denominator
    def __str__(self):
        if self.denominator == 1:
            return str(self.numerator)
        else:
            return f"{self.numerator}/{self.denominator}"
    def __format__(self, format_spec):
        return str(self)
    def __mul__(self, other):
        if isinstance(other, Fraction) :
            return Fraction(self.numerator * other.numerator, self.denominator * other.denominator)
        else:
            return Fraction(self.numerator * other, self.denominator)
    
    def __rmul__(self, other):
        return self.__mul__(other)
    
    def __truediv__(self, other):
        if isinstance(other, Fraction):
            return Fraction(self.numerator * other.denominator, self.denominator * other.numerator)
        else:
            return Fraction(self.numerator, self.denominator * other)
    
    def __rtruediv__(self, other):
        return Fraction(other * self.denominator, self.numerator)
    
    def __add__(self, other):
        if isinstance(other, Fraction):
            return Fraction(self.numerator * other.denominator + other.numerator * self.denominator,
                            self.denominator * other.denominator)
        else:
            return Fraction(self.numerator + other * self.denominator, self.denominator)
    
    def __radd__(self, other):
        return self.__add__(other)
    
    def __sub__(self, other):
        if isinstance(other, Fraction):
            return Fraction(self.numerator * other.denominator - other.numerator * self.denominator,
                            self.denominator * other.denominator)
        else:
            return Fraction(self.numerator - other * self.denominator, self.denominator)
    
    def __rsub__(self, other):
        return self.__sub__(other)
    
    def __eq__(self, other):
        if isinstance(other, Fraction):
            return self.numerator * other.denominator == other.numerator * self.denominator
        else:
            return self.numerator == other * self.denominator

    @classmethod
    def from_float(cls, value, precision=1e-10):
        numerator = round(value)
        denominator = 1
        while abs(value - numerator / denominator) > precision:
            denominator *= 10
            numerator = round(value * denominator)
        return cls(numerator, denominator)

def get_input_matrix():
    print("请输入二维数组(每行以空格分隔,回车结束输入):")
    input_lines = []
    while True:
        line = input().strip()
        if line == '':  # 检测空行
            break
        else:
            input_lines.append(line)
    
    input_str = '\n'.join(input_lines)
    
    # 将输入的字符串转换为合适的数据类型：整数、分数、小数
    matrix_data = []
    row_max_length = max(len(row.split()) for row in input_str.split('\n'))  # 计算最长行的长度
    for row in input_str.split('\n'):
        row_data = []
        for item in row.split():
            if '/' in item:  # 处理分数形式
                numerator, denominator = map(int, item.split('/'))
                row_data.append(Fraction(numerator, denominator))
            else:  # 处理整数或小数形式
                row_data.append(Fraction.from_float(float(item)))
        # 补齐0
        row_data += [Fraction(0)] * (row_max_length - len(row_data))
        matrix_data.append(row_data)
    
    return matrix_data

def determinant(matrix):
    size = len(matrix)
    if size == 1:
        return matrix[0][0]
    elif size == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    else:
        det = Fraction(0)
        for col in range(size):
            sub_matrix = [row[:col] + row[col + 1:] for row in matrix[1:]]
            sub_det = determinant(sub_matrix)
            det += matrix[0][col] * ((-1) ** col) * sub_det
        return det

def transpose(matrix):
    return [[matrix[row][col] for row in range(len(matrix))] for col in range(len(matrix[0]))]

def matrix_add_sub(matrix1, matrix2, operation = '+'):
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        raise ValueError("矩阵尺寸不匹配，无法进行加法或减法运算。")
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            if operation == '+':
                row.append(matrix1[i][j] + matrix2[i][j])
            elif operation == '-':
                row.append(matrix1[i][j] - matrix2[i][j])
        result.append(row)
    return result

def matrix_multiply(matrix1, matrix2):
    # 确定第一个矩阵的行数和列数
    rows1 = len(matrix1)
    cols1 = len(matrix1[0])
    
    # 确定第二个矩阵的行数和列数
    rows2 = len(matrix2)
    cols2 = len(matrix2[0])
    
    if cols1 != rows2:
        raise ValueError("矩阵尺寸不匹配，无法进行乘法运算。")
    
    # 创建结果矩阵，初始化为零矩阵
    result = [[0 for _ in range(cols2)] for _ in range(rows1)]
    
    # 计算乘法
    for i in range(rows1):
        for j in range(cols2):
            for k in range(cols1):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    
    return result

def cofactor(matrix, i, j):
    # 获取子矩阵
    sub_matrix = [row[:j] + row[j + 1:] for row in (matrix[:i] + matrix[i + 1:])]
    # 计算代数余子式
    cofactor_value = (-1) ** (i + j) * determinant(sub_matrix)
    return cofactor_value

def adjoint_matrix(matrix):
    n = len(matrix)
    adjoint = [[cofactor(matrix, i, j) for j in range(n)] for i in range(n)]
    return transpose(adjoint)

def matrix_inverse(matrix):
    # 计算矩阵的行数和列数
    n = len(matrix)
    
    # 计算矩阵的行列式
    det = determinant(matrix)
    
    if det == 0:
        raise ValueError("矩阵不可逆")
    
    # 计算伴随矩阵
    adjoint = adjoint_matrix(matrix)
    
    # 计算逆矩阵
    inverse = [[element / det for element in row] for row in adjoint]
    
    return inverse

def row_echelon_form(matrix):
    echelon_form = [row[:] for row in matrix]
    rows, cols = len(echelon_form), len(echelon_form[0])

    pivot_row = 0
    for col in range(cols):
        # 找到当前列非零元素所在的行
        non_zero_row = None
        for row in range(pivot_row, rows):
            if echelon_form[row][col] != 0:
                non_zero_row = row
                break

        if non_zero_row is not None:
            # 将当前列的非零元素所在行交换到主元行位置
            echelon_form[pivot_row], echelon_form[non_zero_row] = echelon_form[non_zero_row], echelon_form[pivot_row]

            # 将主元行的第一个非零元素缩放为1
            pivot_value = echelon_form[pivot_row][col]
            echelon_form[pivot_row] = [elem / pivot_value for elem in echelon_form[pivot_row]]

            # 利用主元行将上方和下方的元素化为0
            for i in range(pivot_row):
                factor = echelon_form[i][col]
                echelon_form[i] = [elem - factor * echelon_form[pivot_row][j] for j, elem in enumerate(echelon_form[i])]
            for i in range(pivot_row + 1, rows):
                factor = echelon_form[i][col]
                echelon_form[i] = [elem - factor * echelon_form[pivot_row][j] for j, elem in enumerate(echelon_form[i])]

            pivot_row += 1

    return echelon_form

def matrix_rank(matrix):

    echelon_form = row_echelon_form(matrix)
    non_zero_rows = sum(any(val != 0 for val in row) for row in echelon_form)
    
    return non_zero_rows

def print_matrix(matrix):
    max_length = max(len(str(matrix[i][j])) for i in range(len(matrix)) for j in range(len(matrix[0])))
    for row in matrix:
        print(' '.join(str(elem).ljust(max_length + 1) for i, elem in enumerate(row)))