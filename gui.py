import sys
import os
import time
import re
import platform
from tkinter import *

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
root.title('Brainfuck Interpreter')
root.iconbitmap(r'icon.ico')
root.resizable(False, False)

Label(root, text="   ").grid(row=1, column=2)
Label(root, text="Code").grid(row=1, column=0)
code_to_interpret = Text(root, height=20, borderwidth=2, relief='groove')
code_to_interpret.grid(row=1, column=1)

Label(root, text="Input").grid(row=2, column=0)
uinput = Text(root, height=1, borderwidth=2, relief='groove')
uinput.grid(row=2, column=1)

Label(root, text="Output").grid(row=5, column=0)
output = Text(root, height=5, borderwidth=2, relief='groove')
output.grid(row=5, column=1)

def interpret():
    code_map = []

    for each_operation in ''.join(filter(lambda x: x in '.,[]<>+-', str(code_to_interpret.get(1.0, END)))):
        code_map.append(each_operation)

    brace_map = build_brace_map(''.join(code_map))

    cell_map, operation_ptr, cell_ptr, i_wasted_3_hours_on_a_solution_for_input_when_it_was_this_simple = [0 for i in range(100)], 0, 0, 0

    while operation_ptr < len(code_map):
        command = code_map[operation_ptr]

        if   command == '>':
            cell_ptr += 1

        elif command == '<':
            cell_ptr -= 1

        elif command == '+':
            cell_map[cell_ptr] = cell_map[cell_ptr] + 1

            if cell_map[cell_ptr] > 255:
                cell_map[cell_ptr] = 0

        elif command == '-':
            cell_map[cell_ptr] = cell_map[cell_ptr] - 1

            if cell_map[cell_ptr] < 0:
                cell_map[cell_ptr] = 255

        elif command == '.':
            output.insert(END, chr(cell_map[cell_ptr]))

        elif command == ',':
            cell_map[cell_ptr] = ord(uinput.get(1.0, END)[i_wasted_3_hours_on_a_solution_for_input_when_it_was_this_simple])

        elif command == '[' and cell_map[cell_ptr] == 0:
            operation_ptr = brace_map[operation_ptr]

        elif command == ']' and cell_map[cell_ptr] != 0:
            operation_ptr = brace_map[operation_ptr]

        if i_wasted_3_hours_on_a_solution_for_input_when_it_was_this_simple < 1:
            i_wasted_3_hours_on_a_solution_for_input_when_it_was_this_simple += 1
            print(i_wasted_3_hours_on_a_solution_for_input_when_it_was_this_simple)

        operation_ptr += 1

Button(text='Interpret',command=interpret, borderwidth=2).grid(row=4, column=1)

root.mainloop()