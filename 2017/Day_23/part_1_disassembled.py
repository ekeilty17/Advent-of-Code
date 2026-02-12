from utils.solve import solve

"""
                    ; chunk 1
1 :     set b 79                ; b = 79
2 :     set c b                 ; c = b
                    ; chunk 2
3 :     jnz a 2                 ; if a != 0: goto 5
4 :     jnz 1 5                 ; goto 9
5 :     mul b 100               ; b *= 100
6 :     sub b -100000           ; b += 100000
7 :     set c b                 ; c = b
8 :     sub c -17000            ; c += 17000
                    ; chunk 3
9 :     set f 1                 ; f = 1
10:     set d 2                 ; d = 2
                    ; chunk 4
11:     set e 2                 ; e = 2
                    ; chunk 5
12:     set g d                 ; g = d
13:     mul g e                 ; g *= e
14:     sub g b                 ; g -= b
15:     jnz g 2                 ; if g != 0: goto 17
16:     set f 0                 ; f = 0
17:     sub e -1                ; e += 1
18:     set g e                 ; g = e
19:     sub g b                 ; g -= b
20:     jnz g -8                ; if g != 0: goto 12
21:     sub d -1                ; d += 1
22:     set g d                 ; g = d
23:     sub g b                 ; g -= b
24:     jnz g -13               ; if g != 0: goto 11
                    ; chunk 6
25:     jnz f 2                 ; if f != 0: goto 27
26:     sub h -1                ; h += 1
27:     set g b                 ; g = b
28:     sub g c                 ; g -= c
29:     jnz g 2                 ; if g != 0: goto 31
30:     jnz 1 3                 ; goto 33
31:     sub b -17               ; b += 17
32:     jnz 1 -23               ; goto 9
"""

def disassembled() -> int:
    a = b = c = d = e = f = g = h = 0
    num_mul = 0

    # chunk 1
    b = c = 79

    # chunk 2
    if a != 0:
        b = 100*b + 100000
        c = b + 17000

    # chunk 3
    g = 1
    while g != 0:
        f = 1
        d = 2
       
        # chunk 4
        while g != 0:
            e = 2
            
            # chunk 5
            while g != 0:
                g = d*e - b
                num_mul += 1

                if g == 0:
                    f = 0
                e += 1
                g = e - b

            d += 1
            g = d - b
        
        # chunk 6
        if f == 0:
            h += 1
        g = b - c

        if g != 0:
            b += 17
    
    # print(a, b, c, d, e, f, g, h)
    return num_mul
    

def simplified() -> int:
    a = b = c = d = e = f = g = h = 0
    num_mul = 0

    # chunk 1
    b = c = 79

    # chunk 2
    if a != 0:
        b = 100*b + 100000
        c = b + 17000

    # chunk 3
    for b in range(b, c+17, 17):
        f = 1       # f == is_prime
       
        # chunk 4
        for d in range(2, b):
            
            # chunk 5
            if b % d == 0:
                f = 0
            num_mul += b - 2

        # chunk 6
        if f == 0:
            h += 1  # h == prime_count
    
    # print(a, b, c, d, e, f, g, h)
    return num_mul


def efficient() -> int:
    start = end = 79        # the answer will just be 77^2 in this case

    num_mul = 0
    for n in range(start, end+17, 17):
        num_mul += (n - 2)**2
    
    return num_mul

def solution() -> int:
    # return disassembled()
    # return simplified()
    return efficient()

if __name__ == "__main__":
    solve(solution)