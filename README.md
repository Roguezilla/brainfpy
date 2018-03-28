# Brainfuck Interpreter
An interpreter for Brainfuck written in Python.
# Info
main.py -> the lightweight interpreter (495 bytes)  
complete.py -> the fancy interpreter  
gui.py -> an UI for the interpreter  
# Usage of gui.py
Example:  
![Alt text](https://i.imgur.com/DZc2B8V.png)  
How input works:  
![Alt text](https://i.imgur.com/TvQgCYG.png)
# Usage of both main.py and complete.py
```
python main/complete.py filename
```
Example with the included file:  
  
Input:
```
python main/complete.py sample.bf
```
Output:
```
                                *
                               * *
                              *   *
                             * * * *
                            *       *
                           * *     * *
                          *   *   *   *
                         * * * * * * * *
                        *               *
                       * *             * *
                      *   *           *   *
                     * * * *         * * * *
                    *       *       *       *
                   * *     * *     * *     * *
                  *   *   *   *   *   *   *   *
                 * * * * * * * * * * * * * * * *
                *                               *
               * *                             * *
              *   *                           *   *
             * * * *                         * * * *
            *       *                       *       *
           * *     * *                     * *     * *
          *   *   *   *                   *   *   *   *
         * * * * * * * *                 * * * * * * * *
        *               *               *               *
       * *             * *             * *             * *
      *   *           *   *           *   *           *   *
     * * * *         * * * *         * * * *         * * * *
    *       *       *       *       *       *       *       *
   * *     * *     * *     * *     * *     * *     * *     * *
  *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *
 * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
```
