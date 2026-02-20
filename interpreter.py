from ast import Pass


class Interpreter:
    def __init__(self):
        self.stack = []
        self.environment = {}

    def LOAD_VALUE(self, number):
        self.stack.append(number)

    def ADD_TWO_VALUES(self):
        first_val = self.stack.pop()
        second_val = self.stack.pop()
        result = first_val + second_val
        self.stack.append(result)

    def PRINT_ANSWER(self):
        result = self.stack.pop()
        print(result)

    def STORE_NAME(self, name):
        self.environment[name] = self.stack.pop()

    def LOAD_NAME(self, name):
        val = self.environment[name]
        self.stack.append(val)

    def parse_arguments(self, instruction, argument, instruction_set):
        number = ["LOAD_VALUE"]
        variable = ["STORE_NAME", "LOAD_NAME"]

        if instruction in number:
            return instruction_set["numbers"][argument]
        elif instruction in variable:
            return instruction_set["names"][argument]

    def run_code(self, instruction_set):
        instructions = instruction_set["instructions"]

        for instruction, argument in instructions:
            argument = self.parse_arguments(instruction, argument, instruction_set)
            bytecode_method = getattr(self, instruction)

            if not argument:
                bytecode_method()
            else:
                bytecode_method(argument)
