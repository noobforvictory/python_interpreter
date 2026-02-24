
import array
from ast import Pass

from interpreter import Interpreter


def parse(program: str):
    start = 0
    end = 0
    arr = []
    interpreter = Interpreter()
    for i in range(1,len(program)):
        if not program[i].isnumeric():
            end = i-1
            if start == end:
                arr.append(program[start])
            else:
                arr.append(program[start: end+1])
            start = i+1
            arr.append(program[i])
    final_el = "".join(program[start:])
    arr.append(final_el)
    print(arr)
   
    perform_operations(arr, interpreter)

    print(arr)

def create_arithimatic_instrutions(first: str, second : str, operator: str):
    operation_def = {
        "/":"DIVIDE_TWO_VALUE",
        "*":"MULTIPLY_TWO_VALUES",
        "+":"ADD_TWO_VALUES",
        "-":"SUBSTRACT_TWO_VALUES"
    }
    instruction_set = {
        "instructions": [("LOAD_VALUE", 0),
                         ("LOAD_VALUE", 1),
                         (operation_def[operator], None),
                         ("PRINT_ANSWER", None)],
        "numbers": [float(first),float(second)],
        "names":   ["a", "b"] }
    return instruction_set

def perform_operations(arr: list, interpreter: Interpreter):
    is_div_left = True
    is_multi_left = True
    is_add_left = True
    is_subs_left = True
    while is_div_left:
        is_div_left = div_func(arr,interpreter)
    
    while is_multi_left:
        is_multi_left = multi_func(arr,interpreter)
    
    while is_subs_left:
        is_subs_left = subs_func(arr,interpreter)
    
    while is_add_left:
        is_add_left = add_func(arr,interpreter)



    

def div_func(arr, interpreter):
    # for loop for division
    for i in range(len(arr)):
        if arr[i] == "/":
            what_to_execute = create_arithimatic_instrutions(arr[i-1], arr[i+1], arr[i])
            val = interpreter.run_code(what_to_execute)
            del arr[i-1:i+2]
            arr.insert(i-1,val)
            return True
    return False

def multi_func(arr, interpreter):
    # for loop for multiplication
    for i in range(len(arr)):
        if arr[i] == "*":
            what_to_execute = create_arithimatic_instrutions(arr[i-1], arr[i+1], arr[i])
            val = interpreter.run_code(what_to_execute)
            del arr[i-1:i+2]
            arr.insert(i-1,val)
            return True
    return False

def add_func(arr, interpreter):
    # for loop for addition
    for i in range(len(arr)):
        if arr[i] == "+":
            what_to_execute = create_arithimatic_instrutions(arr[i-1], arr[i+1], arr[i])
            val = interpreter.run_code(what_to_execute)
            del arr[i-1:i+2]
            arr.insert(i-1,val)
            return True
    return False

def subs_func(arr, interpreter):
    # for loop for substraaction
    for i in range(len(arr)):
        if arr[i] == "-":
            what_to_execute = create_arithimatic_instrutions(arr[i-1], arr[i+1], arr[i])
            val = interpreter.run_code(what_to_execute)
            del arr[i-1:i+2]
            arr.insert(i-1,val)
            return True
    return False

def main():
    parse("1200+450*30-600/3+75*20")
 

if __name__ == "__main__":
    main()
