from interpreter import Interpreter


# what_to_execute = {
#         "instructions": [("LOAD_VALUE", 0),
#                          ("STORE_NAME", 0),
#                          ("LOAD_VALUE", 1),
#                          ("STORE_NAME", 1),
#                          ("LOAD_NAME", 0),
#                          ("LOAD_NAME", 1),
#                          ("ADD_TWO_VALUES", None),
#                          ("PRINT_ANSWER", None)],
#         "numbers": [1, 2],
#         "names":   ["a", "b"] }

what_to_execute = {
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




interpreter = Interpreter()
interpreter.run_code(what_to_execute)
