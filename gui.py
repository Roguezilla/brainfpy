from tkinter import *

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
    code_map, code, comma_count = [], ''.join(filter(lambda x: x in '.,[]<>+-', str(code_to_interpret.get(1.0, END)))), 0

    for operation in code:
        code_map.append(operation)
        if operation == ',':
            comma_count += 1

    cell_map, operation_ptr, cell_ptr, input_ptr, bracket_ptr = [0]*30000, 0, 0, 0, 0

    while operation_ptr < len(code_map):
        command = code_map[operation_ptr]

        if command == '>':
            cell_ptr += 1

        elif command == '<':
            cell_ptr -= 1

        elif command == '+':
            cell_map[cell_ptr] += 1

            if cell_map[cell_ptr] > 255:
                cell_map[cell_ptr] = 0

        elif command == '-':
            cell_map[cell_ptr] -= 1

            if cell_map[cell_ptr] < 0:
                cell_map[cell_ptr] = 255

        elif command == '.':
            output.insert(END, chr(cell_map[cell_ptr]))

        elif command == ',':
            if input_ptr < comma_count:
                input_ptr += 1

            for i in range(input_ptr):
                cell_map[cell_ptr] = ord(uinput.get(1.0, END)[i])

        elif command == '[':
            bracket_ptr = operation_ptr
        
        elif command == ']' and cell_map[cell_ptr] != 0:
            operation_ptr = bracket_ptr
		
        operation_ptr += 1

Button(text='Interpret',command=interpret, borderwidth=2).grid(row=4, column=1)

root.mainloop()
