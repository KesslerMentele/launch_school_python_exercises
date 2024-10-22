"""


Assume:
    - No invalid tokens
    - No illegal operations

this allows us to use an _ case and coerce the integer without checking
validity.

also, because all operations are legal and not invalid, we do not have to check
if the arg is a valid operation or keep a list of valid operations.

"""

def minilang(args:str):
    stack = []
    register = 0
    args = args.split()

    for arg in args:
        match arg:
            case "PUSH":
                stack.append(register)
            case "ADD":
                register += stack.pop()
            case "SUB":
                register -= stack.pop()
            case "MULT":
                register *= stack.pop()
            case "DIV":
                register //= stack.pop()
            case "REMAINDER":
                register %= stack.pop()
            case "POP":
                register = stack.pop()
            case "PRINT":
                print(register)
            case _ :
                register = int(arg)

minilang('PRINT')
# 0

minilang('5 PUSH 3 MULT PRINT')
# 15

minilang('5 PRINT PUSH 3 PRINT ADD PRINT')
# 5
# 3
# 8

minilang('5 PUSH POP PRINT')
# 5

minilang('3 PUSH 4 PUSH 5 PUSH PRINT ADD PRINT POP PRINT ADD PRINT')
# 5
# 10
# 4
# 7

minilang('3 PUSH PUSH 7 DIV MULT PRINT')
# 6

minilang('4 PUSH PUSH 7 REMAINDER MULT PRINT')
# 12

minilang('-3 PUSH 5 SUB PRINT')
# 8

minilang('6 PUSH')
# (nothing is printed)