import operator
import sys

ops = {
    #The math operators
    "+": operator.add,
    "×": operator.mul,
    "-": operator.sub,
    "÷": operator.truediv,
    "^": operator.pow,
    "÷÷": operator.floordiv,
    "%": operator.mod,
    #The bitwise operators
    "AND": operator.and_,
    "OR": operator.or_,
    "XOR": operator.xor,
    "<<": operator.lshift,
    ">>": operator.rshift,
}
bitwise_ops = {"AND", "OR", "XOR", "<<", ">>"}
help_option = ["+: Addition", "x: Multiplying", "-: Subtracting", "÷: Dividing", "÷÷: Divides And gives the whole number (quotient)", "%: Divides And gives the leftover remainders", "AND: Matching bits", "OR: Either bits", "XOR: Different bits", "<<: shifting left", ">>: shifting right"]

while True:
    while True:
        raw_x = input("Starting number or exit: ")
        if raw_x.lower() == "exit":
            sys.exit(0)
        try:
            x = float(raw_x)
            break
        except ValueError:
            print("That is not a valid number")

    while True:
        op = input("Operators: + | - | × | ÷ | ^ | ÷÷ | % | AND | OR | XOR | << | >> | help | exit | return\nChoice: ")
        if op.lower() == "exit":
            sys.exit(0)
        if op.lower() == "return":
            print("\n--- Resetting ---\n")
            break
        if op.lower() == "help":
        	print("help", *help_option, sep="\n\t")
        	continue
        	
        if op in ops:
            raw_num = input("Next number or 'exit': ")
            if raw_num.lower() == "exit":
                sys.exit(0)
            try:
                num = int(raw_num) if op in bitwise_ops else float(raw_num)
                x = ops[op](int(x) if op in bitwise_ops else x, num)
                print("Result", x)
            except (ValueError, NameError):
                print("Invalid input")
            except ArithmeticError:
                print("\nMath Error")
        else:
            print("Try again")
