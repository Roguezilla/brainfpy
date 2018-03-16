+++++ +++++           ;set cell #0 to 10
[                     ;loop thru the next four cells 10 times
    >+++++ +++++      ;add 10 to cell #1
    >+++++ ++         ;add 7  to cell #2
    >+++              ;add 3  to cell #3
    <<<-              ;subtract 1 from cell #0 each time to the loop ends until its 0
]                     ;end of the loop

                      ;at this point cell values are
                      ;cell #0 is 0
                      ;cell #1 is 100
                      ;cell #2 is 70
                      ;cell #3 is 30
                      ;current cell is #0

                      ;values: (H)72 (e)101 (l)108 (l)108 (o)111 (space)32 (W)87 (o)111 (e)114 (l)108 (d)100 (!)33

>> ++ .               ;jump to cell #3 and add 2 to it so it holds 72 : H
< + .                 ;jump to cell #2 and add 1 to it so it holds 101 : e
+++++ ++ .            ;add 7 to the same cell so it holds 108 : l
.                     ;same value which is 108: l
+++ .                 ;add 3 to the same cell so it holds 111 : o
>> ++ .               ;jump to cell #3 and add 2 to it so it hols 32 : space
< +++++ +++++ +++++ . ;jump to cell #2 and add 15 to it so it hols W : 87
< .                   ;jump to cell #1 which hols 111 : o
+++ .                 ;add 3 to the same cell so it holds 114 : r
----- - .             ;subtract 6 from the same cell so it holds 108 : l
----- --- .           ;subtract 8 from the same cell so it holds 100 : d
>> + .                ;jump to cell #4 and add 1 to is so it holds 33 : !