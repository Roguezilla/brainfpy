import bimpy

ctx = bimpy.Context()
ctx.init(275, 110, 'Interpreter')

icode = bimpy.String('++++++++++[>++++++++++>+++++++>+++<<<-]>>++.<+.+++++++..+++.>>++.<+++++++++++++++.<.+++.------.--------.>>+.')
uinput = bimpy.String('')
output = bimpy.String('')

def interpret():
    global output
    code_map, code, comma_count = [], ''.join(filter(lambda x: x in '.,[]<>+-', str(icode.value))), 0

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
            output.value += chr(cell_map[cell_ptr])

        elif command == ',':
            if input_ptr < comma_count:
                input_ptr += 1

            for i in range(input_ptr):
                cell_map[cell_ptr] = ord(uinput.value[i])

        elif command == '[':
            bracket_ptr = operation_ptr
        
        elif command == ']' and cell_map[cell_ptr] != 0:
            operation_ptr = bracket_ptr
		
        operation_ptr += 1

while(not ctx.should_close()):
    ctx.new_frame()

    bimpy.begin('', flags=(bimpy.WindowFlags.AlwaysAutoResize | bimpy.WindowFlags.NoTitleBar))
    bimpy.input_text('Code', icode, 2048)
    bimpy.input_text('Input', uinput, 2048)
    if bimpy.button('Interpret'):
        interpret()
    bimpy.input_text('Output', output, 2048)
    bimpy.end()

    ctx.render()
