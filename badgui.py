import sys
import os
import time
import re
import platform
from tkinter import *
from tkinter import ttk

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

root = Tk()

Label(root, text="Brainfuck interpreter").grid()
Label(root, text="Code").grid()
code = Entry(root)
code.grid()
Label(root, text="Cell number").grid()
cells = Entry(root)
cells.grid()

def interpret():
    code_map = []

    for each_operation in ''.join(filter(lambda x: x in '.,[]<>+-', str(code.get()))):
        code_map.append(each_operation)

    brace_map = build_brace_map(''.join(code_map))

    cell_map, operation_ptr, cell_ptr = [0 for i in range(int(cells.get()))], 0, 0

    while operation_ptr < len(code_map):
        command = code_map[operation_ptr]

        if   command == '>':                             cell_ptr += 1
        elif command == '<':                             cell_ptr -= 1
        elif command == '+':                             cell_map[cell_ptr] = cell_map[cell_ptr] + 1
        elif command == '-':                             cell_map[cell_ptr] = cell_map[cell_ptr] - 1
        elif command == '.':                             Label(root, text=chr(cell_map[cell_ptr])).grid()
        elif command == ',':                             cell_map[cell_ptr] = ord(sys.stdin.read(1))
        elif command == '[' and cell_map[cell_ptr] == 0: operation_ptr = brace_map[operation_ptr]
        elif command == ']' and cell_map[cell_ptr] != 0: operation_ptr = brace_map[operation_ptr]

        operation_ptr += 1

Button(text='Interpret',command=interpret).grid()


root.mainloop()