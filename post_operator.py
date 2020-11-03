def do_calculation(val1, val2, operator):
    if operator == "+":
        result = int(val1) + int(val2)
    elif operator == "-":
        result = int(val1) - int(val2)
    elif operator == "*":
        result = int(val1) * int(val2)
    else:
        result = int(val1) // int(val2)

    return result

def my_solve(values):
    res2 = []
    for item in values:
        try:
            int(item)
        except:

            if len(res2) == 1:
                return res2
            ind_op = values.index(item)
            result = do_calculation(values[ind_op-2], values[ind_op-1], item)
            new_list = values[:ind_op-2] + [str(result)] + values[ind_op+1:]
            if len(new_list) > 1:
                res2 = my_solve(new_list)
            else:
                return new_list

def solve(values):
    a = my_solve(values)
    return int(a[0])

print(solve(['2', '5', '7','1', '+', '*', '-']))
assert solve(['1', '2', '+', '3', '+']) == 6
