
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
    arr.append(program[-1])
    print(arr)

    # for loop for division
    for i in range(len(arr)):
        if arr[i] == "/":
            what_to_execute = create_arithimatic_instrutions(arr[i-1], arr[i+1], arr[i])
            val = interpreter.run_code(what_to_execute)
            
            del arr[i-1:i+2]
            arr.insert(i-1,val)

    # for loop for multiplication
    for i in range(len(arr)):
        if arr[i] == "*":
            what_to_execute = create_arithimatic_instrutions(arr[i-1], arr[i+1], arr[i])
            val = interpreter.run_code(what_to_execute)
            
            del arr[i-1:i+2]
            arr.insert(i-1,val)

    # for loop for addition
    for i in range(len(arr)):
        if arr[i] == "+":
            what_to_execute = create_arithimatic_instrutions(arr[i-1], arr[i+1], arr[i])
            val = interpreter.run_code(what_to_execute)
            
            del arr[i-1:i+2]
            arr.insert(i-1,val)

    # for loop for substraction
    for i in range(len(arr)):
        if arr[i] == "-":
            what_to_execute = create_arithimatic_instrutions(arr[i-1], arr[i+1], arr[i])
            val = interpreter.run_code(what_to_execute)
            
            del arr[i-1:i+2]
            arr.insert(i-1,val)
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
        "numbers": [int(first),int(second)],
        "names":   ["a", "b"] }
    return instruction_set

def main():
    parse("8+10/2*2-1")


if __name__ == "__main__":
    main()
