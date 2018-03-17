import sys
import os
import time
import re
import platform

#https://github.com/pocmo/Python-Brainfuck/blob/master/brainfuck.py#L51
def build_brace_map(code): 
    temp_bracestack, brace_map = [], {}

    for position, command in enumerate(code):
        if command == "[": temp_bracestack.append(position)
        if command == "]":
            start = temp_bracestack.pop()
            brace_map[start] = position
            brace_map[position] = start
    del temp_bracestack
    return brace_map

def interpret(filename, cell_num, debug):
    code_map = []

    with open(filename, 'r') as f:
        for each_operation in ''.join(filter(lambda x: x in '.,[]<>+-', f.read())):
            code_map.append(each_operation)

    brace_map = build_brace_map(''.join(code_map))

    cell_map, operation_ptr, cell_ptr = [0 for i in range(int(cell_num))], 0, 0

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

        operation_ptr += 1

    if debug == 'debug':
        print('\nLast instruction [{}] -> {}'.format(str(operation_ptr),str(cell_map)))
        print('Last cell is cell [#{}] and it holds the value [{}].'.format(cell_ptr, cell_map[cell_ptr]))
        if operation_ptr < len(code_map) - 1:
            if platform.system() == 'Windows': os.system('cls')
            else:                              os.system('clear') 

if __name__ == '__main__':
    interpret(sys.argv[1], sys.argv[2], sys.argv[3])