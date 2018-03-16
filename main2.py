import sys, re

def buildbracemap(code): 
  temp_bracestack, bracemap = [], {}

  for position, command in enumerate(code):
    if command == "[": temp_bracestack.append(position)
    if command == "]":
      start = temp_bracestack.pop()
      bracemap[start] = position
      bracemap[position] = start
  return bracemap

def run(filename):
  code = []
  with open(filename, 'r') as f:
    for each_char in ''.join(filter(lambda x: x in '.,[]<>+-', re.sub('\n', '', f.read()))):
      code.append(each_char)

  bracemap = buildbracemap(''.join(code))

  cells = [0 for i in range(9999)]
  codeptr = 0
  cellptr = 0

  while codeptr < len(code):
    command = code[codeptr]

    if command == '>':
      cellptr += 1
    elif command == '<':
      cellptr -= 1
    elif command == '+':
      cells[cellptr] = cells[cellptr] + 1
    elif command == '-':
      cells[cellptr] = cells[cellptr] - 1
    elif command == '.':
      sys.stdout.write(chr(cells[cellptr]))
    elif command == ',':
      cells[cellptr] = ord(sys.stdin.read(1))
    elif command == '[' and cells[cellptr] == 0:
      codeptr = bracemap[codeptr]
    elif command == ']' and cells[cellptr] != 0:
      codeptr = bracemap[codeptr]

    codeptr += 1

run(sys.argv[1])
