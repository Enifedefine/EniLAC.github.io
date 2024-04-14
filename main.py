from matrix_operations import *

# 全局变量：矩阵数组和变量字典
matrix_array = []
variable_dict = {}

def parse_statement(statement):
    global matrix_array, variable_dict
    statement = statement.strip()
    parts = statement.split()
    if len(parts) == 1:
        # 只输入变量名时，输出对应矩阵的值
        matrix_name = parts[0]
        if matrix_name in variable_dict:
            matrix = matrix_array[variable_dict[matrix_name]]
            print_matrix(matrix)
        else:
            print(f"未找到变量名为'{matrix_name}'的矩阵。")
    elif parts[1] != '=':
        func_name = parts[0]
        if func_name not in ['det', 't', '+' , '-' ,'*', '-1', 'r' , 'rref']:
            print("无效的计算函数名。")
            return
        
        matrices = parts[1:]
        if not all(matrix_name in variable_dict for matrix_name in matrices):
            print("计算语句中存在未定义的矩阵名，请检查后重试。")
            return
        
        input_matrices = [matrix_array[variable_dict[matrix_name]] for matrix_name in matrices]

        if func_name == 'det':
            det = determinant(input_matrices[0])
            print(f"行列式的值为：{det}")
        elif func_name == 't':
            transposed = transpose(input_matrices[0])
            print("转置为：")
            print_matrix(transposed)
            matrix_array[0] = transposed
        elif func_name in ['+', '-']:
            if len(input_matrices) < 2:
                print("矩阵加减法操作需要至少两个矩阵，请检查后重试。")
                return
            result = input_matrices[0]
            operation = func_name
            for matrix in input_matrices[1:]:
                if len(result) != len(matrix) or len(result[0]) != len(matrix[0]):
                    print("矩阵加减法操作的矩阵尺寸不匹配，请检查后重试。")
                    return
                result = matrix_add_sub(result, matrix, operation)
            if operation == '+':
                print("矩阵加法的结果为：")
            else:
                print("矩阵减法的结果为：")
            print_matrix(result)
            matrix_array[0] = result
        elif func_name == '*':
            if len(input_matrices) < 2:
                print("矩阵乘法操作需要至少两个矩阵，请检查后重试。")
                return
            result = input_matrices[0]
            for matrix in input_matrices[1:]:
                try:
                    if len(result[0]) != len(matrix):
                        raise ValueError("矩阵乘法的操作数尺寸不匹配，请检查后重试。")
                    result = matrix_multiply(result, matrix)
                except ValueError as e:
                    print(e)
                    return
            print("矩阵乘法的结果为：")
            print_matrix(result)
            matrix_array[0] = result
        elif func_name == '-1':
            try:
                inverse = matrix_inverse(input_matrices[0])
                print("矩阵的逆矩阵为：")
                print_matrix(inverse)
                matrix_array[0] = inverse
            except ValueError as e:
                print(e)
        elif func_name == 'r':
            rank = matrix_rank(input_matrices[0])
            print(f"矩阵的秩为：{rank}")
        elif func_name == 'rref':
            echelon_form = row_echelon_form(input_matrices[0])
            print("简化的行阶梯形矩阵为：")
            print_matrix(echelon_form)
            matrix_array[0] = echelon_form
    elif parts[1] == '=':
        var_name = parts[0]
        if len(parts) == 3:
            value_name = parts[2]
            if value_name not in variable_dict:
                print(f"未找到变量名为'{value_name}'的矩阵。")
                return
            matrix_data = matrix_array[variable_dict[value_name]]
        else:
            matrix_data = get_input_matrix()
        if var_name in variable_dict:
            matrix_array[0] = matrix_array[variable_dict[var_name]]
            matrix_array[variable_dict[var_name]] = matrix_data
            print(f"变量名'{var_name}'已被修改!")
            return
        # 启动矩阵输入函数
        matrix_array.append(matrix_data)
        variable_dict[var_name] = len(matrix_array) - 1
        print(f"变量'{var_name}'赋值成功！")
    else:
        print("无效的语句")

def main():
    global matrix_array, variable_dict
    matrix_array.append([[]])
    variable_dict["ans"] = len(matrix_array) - 1
    print("欢迎使用矩阵计算器！")
    while True:
        statement = input(">> ")
        if statement.strip().lower() == 'quit':
            print("感谢使用矩阵计算器！")
            break
        
        parse_statement(statement)

if __name__ == "__main__":
    main()