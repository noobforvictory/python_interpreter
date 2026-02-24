Components of interpretor->
1. take  human readabke commands in text (make your own language that is consistent)

2. convert it into bytecode
    - You need to parse the instructions
    -build sequence of exicutable bytecode instructions
    - once the first two are done, you need to pass on this bytecode to the the interpretor for exicution.
    
3. convert it into human readable bytecode instructions.
have interpretor functions that can implement all the commands that can be present in the byte code or the features we want to support in our interpretor.


**Goals**

Essential Capabilities & Features for toy language

    -Lexical Analysis & Parsing: Ability to read source code, turn it into tokens, and generate an Abstract Syntax Tree (AST).
    -Basic Data Types: Integer, String, and Boolean types.
    -Control Flow: If-else statements and while loops.
    -Variables: Assignment and reassignment of data.
    -Functions: Ability to define and call functions, preferably with recursion.
    -Input/Output: Simple print functionality to display results.

Reach Goal - Closures
