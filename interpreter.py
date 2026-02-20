class Interpreter:
    def __init__(self):
        self.stack = []

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

    def run_code(self, instruction_set):
        instructions = instruction_set["instructions"]
        numbers = instruction_set["numbers"]

        for instruction, argument in instructions:
            if instruction == "LOAD_VALUE":
                self.LOAD_VALUE(numbers[argument])
            elif instruction == "ADD_TWO_VALUES":
                self.ADD_TWO_VALUES()
            elif instruction == "PRINT_ANSWER":
                self.PRINT_ANSWER()
