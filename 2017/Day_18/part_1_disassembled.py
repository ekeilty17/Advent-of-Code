from typing import List
from utils.solve import test, solve

def example_solution() -> int:
    output = []

    a = 1
    a += 2
    a *= a
    a %= 5
    output.append(a)
    
    a = 1
    while True:
        return output[-1]


"""
                ; chunk 1
                            ; a = b = f = i = p = 0
1 :     set i 31            ; i = 31
2 :     set a 1             ; a = 1
3 :     mul p 17            ; p *= 17
4 :     jgz p p             ; if p > 0: goto 4+p
                ; chunk 2
5 :     mul a 2             ; a *= 2
6 :     add i -1            ; i -= 1
7 :     jgz i -2            ; if i > 0: goto 5
                ; chunk 3
8 :     add a -1            ; a -= 1
9 :     set i 127           ; i = 127
10:     set p 618           ; p = 618
                ; chunk 4
11:     mul p 8505          ; p *= 8505
12:     mod p a             ; p %= a
13:     mul p 129749        ; p *= 129749
14:     add p 12345         ; p += 12345
15:     mod p a             ; p %= a
16:     set b p             ; b = p
17:     mod b 10000         ; b %= 10000
18:     snd b               ; output b
19:     add i -1            ; i -= 1
20:     jgz i -9            ; if i > 0: goto 11
                ; chunk 5
21:     jgz a 3             ; if a > 0: goto 24
22:     rcv b               ; if b != 0: terminate
23:     jgz b -1            ; if b > 0: goto 22

                ; chunk 6
24:     set f 0             ; f = 0
25:     set i 126           ; i = 126
26:     rcv a               ; if a != 0; terminate
                ; chunk 7
27:     rcv b               ; if b != 0; terminate
28:     set p a             ; p = a
29:     mul p -1            ; p *= -1
30:     add p b             ; p += b
31:     jgz p 4             ; if p > 0: goto 35
32:     snd a               ; output a
33:     set a b             ; a = b
34:     jgz 1 3             ; goto 37
35:     snd b               ; output b
36:     set f 1             ; f = 1
37:     add i -1            ; i -= 1
38:     jgz i -11           ; if i > 0: goto 27
39:     snd a               ; output a
40:     jgz f -16           ; if f > 0: goto 24
41:     jgz a -19           ; if a > 0: goto 25
"""

def disassembled() -> List[int]:
    output = []

    # chunk 1
    a = b = f = i = p = 0
    i = 31
    a = 1

    # chunk 2
    while i > 0:
        a *= 2
        i -= 1

    # chunk 3
    a -= 1
    i = 127
    p = 618

    # chunk 4
    while i > 0:
        p = (p * 8505) % a
        p = (p * 129749 + 12345) % a
        b = p % 10000
        output.append(b)
        i -= 1

    # chunk 5
    if a <= 0 and b != 0:
        return output

    # chunk 6
    while f > 0 or a > 0:
        if f > 0:
            f = 0

        i = 126
        if a != 0:
            return output

        # chunk 7
        while i > 0:
            if b != 0:
                return output
            
            p = b - a
            if p == 0:
                output.append(a)
                a = b
            else:
                output.append(b)
            
            f = 1
            i -= 1
        
        output.append(b)

def efficient() -> List[int]:
    output = []

    # chunk 1, 2, 3
    a = 2**31 - 1
    p = 618

    # chunk 4
    for _ in range(127):
        p = (p * 8505) % a
        p = (p * 129749 + 12345) % a
        b = p % 10000
        output.append(b)

    # chunk 5
    if a <= 0 and b != 0:
        return output

    # chunk 6
    while True:
        
        if a != 0:
            return output

        # chunk 7
        for _ in range(126):
            if b != 0:
                return output
            
            if b - a == 0:
                output.append(a)
                a = b
            else:
                output.append(b)
        
        output.append(b)

def solution() -> int:
    # frequencies = disassembled()
    frequencies = efficient()
    return frequencies[-1]

if __name__ == "__main__":
    expected_answer = 4
    test(expected_answer, example_solution)

    solve(solution)