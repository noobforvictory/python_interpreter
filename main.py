from interpreter import Interpreter
from my_parser import parse



what_to_execute1 = {
        "instructions": [("LOAD_VALUE", 0),
                         ("STORE_NAME", 0),
                         ("LOAD_VALUE", 1),
                         ("STORE_NAME", 1),
                         ("LOAD_NAME", 0),
                         ("LOAD_NAME", 1),
                         ("SUBSTRACT_TWO_VALUES", None),
                         ("STORE_NAME", 3),
                         ("LOAD_VALUE", 2),
                         ("STORE_NAME", 2),
                         ("LOAD_NAME", 3),
                         ("LOAD_NAME", 2),
                         ("SUBSTRACT_TWO_VALUES", None),
                         ("PRINT_ANSWER", None)],
        "numbers": [6, 2, 3],
        "names":   ["a", "b", "c", "d"] }

what_to_execute2 = {
        "instructions": [("LOAD_VALUE", 0),
                         ("STORE_NAME", 0),
                         ("LOAD_VALUE", 1),
                         ("STORE_NAME", 1),
                         ("LOAD_NAME", 0),
                         ("LOAD_NAME", 1),
                         ("SUBSTRACT_TWO_VALUES", None),
                         ("STORE_NAME", 3),
                         ("LOAD_VALUE", 2),
                         ("STORE_NAME", 2),
                         ("LOAD_NAME", 3),
                         ("LOAD_NAME", 2),
                         ("SUBSTRACT_TWO_VALUES", None),
                         ("PRINT_ANSWER", None)],
        "numbers": [6, 2, 4],
        "names":   ["a", "b", "c", "d"] }

# program = "8+10/2*2-1"

# what_to_execute = parse(program)

interpreter = Interpreter()
interpreter.run_code(what_to_execute1)
interpreter.run_code(what_to_execute2)
