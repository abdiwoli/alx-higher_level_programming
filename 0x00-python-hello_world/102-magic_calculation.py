#!/usr/bin/python3
import dis
def sample_function(a, b):
    return 98 + (a ** b)
# Disassemble the bytecode of the sample function
bytecode = dis.Bytecode(sample_function)
for instruction in bytecode:
    print(instruction.opcode, instruction.opname, "               ", end=" ")
    if instruction.argval is not None or instruction.arg is not None:
        print("(", end="")
        print(instruction.arg, instruction.argval, end=")\n")
    else:
        print()


def magic_calculation(a, b):
    return 98 + (a ** b)
