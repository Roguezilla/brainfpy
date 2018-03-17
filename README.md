# Brainfuck Interpreter
An interpreter for Brainfuck written in Python.
# Info
main.py -> the lightweight interpreter (511 bytes)  
complete.py -> the fancy interpreter
# Usage of main.py
```
python main.py filename
```
Example with the included file.
```
python main.py hello_world.bf
```
# Usage of complete.py
```
python complete.py filename cell_number debug_info
```
Example with the included file.  
(If you don't want debug info, type something else instead of 'debug'.)  
Input:
```
python complete.py hello_world.bf 25 debug
```
Output:
```
Hello World!
Last instruction [108] -> [0, 100, 87, 33, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
Last cell is cell [#3] and it holds the value [33].
```
