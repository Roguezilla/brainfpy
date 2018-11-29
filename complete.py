import sys

def interpret(filename):
    code_map, f = [], None

    with open(filename, 'r') as f:
        for each_operation in ''.join(filter(lambda x: x in '.,[]<>+-', f.read())):
            code_map.append(each_operation)
        f.close()
	
    cell_map, operation_ptr, cell_ptr, bracket_ptr = [0]*30000, 0, 0, 0

    while operation_ptr < len(code_map):
        command = code_map[operation_ptr]

        if   command == '>':
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
            sys.stdout.write(chr(cell_map[cell_ptr]))
        
        elif command == ',':
            cell_map[cell_ptr] = ord(sys.stdin.read(1))
        
        elif command == '[':
            bracket_ptr = operation_ptr
        
        elif command == ']' and cell_map[cell_ptr] != 0:
            operation_ptr = bracket_ptr

        operation_ptr += 1

if __name__ == '__main__':
    interpret(sys.argv[1])
