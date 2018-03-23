import sys
import re

#https://github.com/pocmo/Python-Brainfuck/blob/master/brainfuck.py#L51
def build_brace_map(code):
    temp_brace_stack, brace_map = [], {}

    for position, command in enumerate(code):
        if command == "[": temp_brace_stack.append(position)
        if command == "]":
            start = temp_brace_stack.pop()
            brace_map[start] = position
            brace_map[position] = start
    del temp_brace_stack
    return brace_map

def interpret(filename):
    code_map = []

    try:
        f = open(filename, 'r')
        for each_operation in ''.join(filter(lambda x: x in '.,[]<>+-', f.read())):
            code_map.append(each_operation)
    finally:
        f.close()

    brace_map = build_brace_map(''.join(code_map))

    cell_map, operation_ptr, cell_ptr = [0 for i in range(30000)], 0, 0

    while operation_ptr < len(code_map):
        command = code_map[operation_ptr]

        if   command == '>':                             cell_ptr += 1
        elif command == '<':                             cell_ptr -= 1
        elif command == '+':                             cell_map[cell_ptr] = cell_map[cell_ptr] + 1
        elif command == '-':                             cell_map[cell_ptr] = cell_map[cell_ptr] - 1
        elif command == '.':                             sys.stdout.write(chr(cell_map[cell_ptr]))
        elif command == ',':                             cell_map[cell_ptr] = ord(sys.stdin.read(1))
        elif command == '[' and cell_map[cell_ptr] == 0: operation_ptr = brace_map[operation_ptr]
        elif command == ']' and cell_map[cell_ptr] != 0: operation_ptr = brace_map[operation_ptr]

        if   cell_map[cell_ptr] > 255:                   cell_map[cell_ptr] = 0
        elif cell_map[cell_ptr] < 0:                     cell_map[cell_ptr] = 255

        operation_ptr += 1

if __name__ == '__main__':
    interpret(sys.argv[1])