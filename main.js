'use strict'; import { AssertionError, AttributeError, BaseException, DeprecationWarning, Exception, IndexError, IterableError, KeyError, NotImplementedError, RuntimeWarning, StopIteration, UserWarning, ValueError, Warning, __JsIterator__, __PyIterator__, __Terminal__, __add__, __and__, __call__, __class__, __envir__, __eq__, __floordiv__, __ge__, __get__, __getcm__, __getitem__, __getslice__, __getsm__, __gt__, __i__, __iadd__, __iand__, __idiv__, __ijsmod__, __ilshift__, __imatmul__, __imod__, __imul__, __in__, __init__, __ior__, __ipow__,__irshift__, __isub__, __ixor__, __jsUsePyNext__, __jsmod__, __k__, __kwargtrans__, __le__, __lshift__, __lt__, __matmul__, __mergefields__, __mergekwargtrans__, __mod__, __mul__, __ne__, __neg__, __nest__, __or__, __pow__, __pragma__, __pyUseJsNext__, __rshift__, __setitem__, __setproperty__, __setslice__, __sort__, __specialattrib__, __sub__, __super__, __t__, __terminal__, __truediv__, __withblock__, __xor__, abs, all, any, assert, bool, bytearray, bytes, callable, chr, copy, deepcopy, delattr, dict, dir, divmod, enumerate, filter, float, getattr,hasattr, input, int, isinstance, issubclass, len, list, map, max, min, object, ord, pow, print, property, py_TypeError, py_iter, py_metatype, py_next, py_reversed, py_typeof, range, repr, round, set, setattr, sorted, str, sum, tuple, zip
} from "./org.transcrypt.__runtime__.js"; import { Fraction, adjoint_matrix, cofactor, determinant, get_input_matrix, matrix_add_sub, matrix_inverse, matrix_multiply, matrix_rank, print_matrix, row_echelon_form, transpose } from "./matrix_operations.js"; var __name__ = "__main__"; export var matrix_array = []; export var variable_dict =
    dict({}); export var parse_statement = function (statement) {
        var statement = statement.strip(); var parts = statement.py_split(); if (len(parts) == 1) { var matrix_name = parts[0]; if (__in__(matrix_name, variable_dict)) { var matrix = matrix_array[variable_dict[matrix_name]]; print_matrix(matrix) } else print("\u672a\u627e\u5230\u53d8\u91cf\u540d\u4e3a'{}'\u7684\u77e9\u9635\u3002".format(matrix_name)) } else if (parts[1] != "=") {
            var func_name = parts[0]; if (!__in__(func_name, ["det", "t", "+", "-", "*", "-1", "r", "rref"])) {
                print("\u65e0\u6548\u7684\u8ba1\u7b97\u51fd\u6570\u540d\u3002");
                return
            } var matrices = parts.__getslice__(1, null, 1); if (!all(function () { var __accu0__ = []; for (var matrix_name of matrices) __accu0__.append(__in__(matrix_name, variable_dict)); return py_iter(__accu0__) }())) { print("\u8ba1\u7b97\u8bed\u53e5\u4e2d\u5b58\u5728\u672a\u5b9a\u4e49\u7684\u77e9\u9635\u540d\uff0c\u8bf7\u68c0\u67e5\u540e\u91cd\u8bd5\u3002"); return } var input_matrices = function () { var __accu0__ = []; for (var matrix_name of matrices) __accu0__.append(matrix_array[variable_dict[matrix_name]]); return __accu0__ }();
            if (func_name == "det") { var det = determinant(input_matrices[0]); print("\u884c\u5217\u5f0f\u7684\u503c\u4e3a\uff1a{}".format(det)) } else if (func_name == "t") { var transposed = transpose(input_matrices[0]); print("\u8f6c\u7f6e\u4e3a\uff1a"); print_matrix(transposed); matrix_array[0] = transposed } else if (__in__(func_name, ["+", "-"])) {
                if (len(input_matrices) < 2) { print("\u77e9\u9635\u52a0\u51cf\u6cd5\u64cd\u4f5c\u9700\u8981\u81f3\u5c11\u4e24\u4e2a\u77e9\u9635\uff0c\u8bf7\u68c0\u67e5\u540e\u91cd\u8bd5\u3002"); return } var result =
                    input_matrices[0]; var operation = func_name; for (var matrix of input_matrices.__getslice__(1, null, 1)) { if (len(result) != len(matrix) || len(result[0]) != len(matrix[0])) { print("\u77e9\u9635\u52a0\u51cf\u6cd5\u64cd\u4f5c\u7684\u77e9\u9635\u5c3a\u5bf8\u4e0d\u5339\u914d\uff0c\u8bf7\u68c0\u67e5\u540e\u91cd\u8bd5\u3002"); return } var result = matrix_add_sub(result, matrix, operation) } if (operation == "+") print("\u77e9\u9635\u52a0\u6cd5\u7684\u7ed3\u679c\u4e3a\uff1a"); else print("\u77e9\u9635\u51cf\u6cd5\u7684\u7ed3\u679c\u4e3a\uff1a");
                print_matrix(result); matrix_array[0] = result
            } else if (func_name == "*") {
                if (len(input_matrices) < 2) { print("\u77e9\u9635\u4e58\u6cd5\u64cd\u4f5c\u9700\u8981\u81f3\u5c11\u4e24\u4e2a\u77e9\u9635\uff0c\u8bf7\u68c0\u67e5\u540e\u91cd\u8bd5\u3002"); return } var result = input_matrices[0]; for (var matrix of input_matrices.__getslice__(1, null, 1)) try {
                    if (len(result[0]) != len(matrix)) {
                        var __except0__ = ValueError("\u77e9\u9635\u4e58\u6cd5\u7684\u64cd\u4f5c\u6570\u5c3a\u5bf8\u4e0d\u5339\u914d\uff0c\u8bf7\u68c0\u67e5\u540e\u91cd\u8bd5\u3002");
                        __except0__.__cause__ = null; throw __except0__;
                    } var result = matrix_multiply(result, matrix)
                } catch (__except0__) { if (isinstance(__except0__, ValueError)) { var e = __except0__; print(e); return } else throw __except0__; } print("\u77e9\u9635\u4e58\u6cd5\u7684\u7ed3\u679c\u4e3a\uff1a"); print_matrix(result); matrix_array[0] = result
            } else if (func_name == "-1") try { var inverse = matrix_inverse(input_matrices[0]); print("\u77e9\u9635\u7684\u9006\u77e9\u9635\u4e3a\uff1a"); print_matrix(inverse); matrix_array[0] = inverse } catch (__except0__) {
                if (isinstance(__except0__,
                    ValueError)) { var e = __except0__; print(e) } else throw __except0__;
            } else if (func_name == "r") { var rank = matrix_rank(input_matrices[0]); print("\u77e9\u9635\u7684\u79e9\u4e3a\uff1a{}".format(rank)) } else if (func_name == "rref") { var echelon_form = row_echelon_form(input_matrices[0]); print("\u7b80\u5316\u7684\u884c\u9636\u68af\u5f62\u77e9\u9635\u4e3a\uff1a"); print_matrix(echelon_form); matrix_array[0] = echelon_form }
        } else if (parts[1] == "=") {
            var var_name = parts[0]; if (len(parts) == 3) {
                var value_name = parts[2]; if (!__in__(value_name,
                    variable_dict)) { print("\u672a\u627e\u5230\u53d8\u91cf\u540d\u4e3a'{}'\u7684\u77e9\u9635\u3002".format(value_name)); return } var matrix_data = matrix_array[variable_dict[value_name]]
            } else try { print("\u8bf7\u8f93\u5165\u4e8c\u7ef4\u6570\u7ec4(\u6bcf\u884c\u4ee5\u7a7a\u683c\u5206\u9694,\u56de\u8f66\u7ed3\u675f\u8f93\u5165):"); var matrix_data = get_input_matrix() } catch (__except0__) { if (isinstance(__except0__, ValueError)) { var e = __except0__; print(e); return } else throw __except0__; } if (__in__(var_name, variable_dict)) {
                matrix_array[0] =
                    matrix_array[variable_dict[var_name]]; matrix_array[variable_dict[var_name]] = matrix_data; print("\u53d8\u91cf\u540d'{}'\u5df2\u88ab\u4fee\u6539!".format(var_name)); return
            } matrix_array.append(matrix_data); variable_dict[var_name] = len(matrix_array) - 1; print("\u53d8\u91cf'{}'\u8d4b\u503c\u6210\u529f\uff01".format(var_name))
        } else print("\u65e0\u6548\u7684\u8bed\u53e5")
    }; export var print_help = function () {
        try {
            var file = open("help.txt", "r"); try { file.__enter__(); var help_text = file.read(); print(help_text); file.__exit__() } catch (__except0__) {
                if (!file.__exit__(__except0__.name,
                    __except0__, __except0__.stack)) throw __except0__;
            }
        } catch (__except0__) { if (isinstance(__except0__, FileNotFoundError)) print("\u5e2e\u52a9\u6587\u6863\u6587\u4ef6\u672a\u627e\u5230\u3002"); else throw __except0__; }
    }; export var main = function () {
        matrix_array.append([[]]); variable_dict["ans"] = len(matrix_array) - 1; print("\u6b22\u8fce\u4f7f\u7528\u77e9\u9635\u8ba1\u7b97\u5668\uff01\u8f93\u5165 help \u67e5\u770b\u5e2e\u52a9\u6587\u6863\u3002"); while (true) {
            var statement = input(">> "); if (statement.strip().lower() ==
                "quit") { print("\u611f\u8c22\u4f7f\u7528\u77e9\u9635\u8ba1\u7b97\u5668\uff01"); break } else if (statement.strip().lower() == "help") print_help(); else parse_statement(statement)
        }
    }; if (__name__ == "__main__") main();

//# sourceMappingURL=main.map