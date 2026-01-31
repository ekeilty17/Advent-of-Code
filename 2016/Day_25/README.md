# Day 25: Clock Signal

[Problem Link](https://adventofcode.com/2016/day/25)

## Disassembling the Program

Just like we've done in Day 12 and Day 23, let's go through the program line by line and simplify it into modern notation.

Starting with the assembly code
```
            ; chunk 1
1 : cpy a d             ; d = a
2 : cpy 4 c             ; c = 4

            ; chunk 2
3 : cpy 643 b           ; b = 643
4 : inc d               ; d += 1
5 : dec b               ; b -= 1
6 : jnz b -2            ; if b != 0: goto 4
7 : dec c               ; c -= 1
8 : jnz c -5            ; if c != 0: goto 3

            ; chunk 3
9 : cpy d a             ; a = d
10: jnz 0 0             ; 
            ; chunk 3.1
11: cpy a b             ; b = a
12: cpy 0 a             ; a = 0
            ; chunk 3.1.1
13: cpy 2 c             ; c = 2
14: jnz b 2             ; if b != 0: goto 16
15: jnz 1 6             ; goto 21
16: dec b               ; b -= 1
17: dec c               ; c -= 1
18: jnz c -4            ; if c != 0: goto 14
19: inc a               ; a += 1
20: jnz 1 -7            ; goto 13
            ; chunk 3.1.2
21: cpy 2 b             ; b = 2
22: jnz c 2             ; if c != 0: goto 24
23: jnz 1 4             ; goto 27
24: dec b               ; b -= 1
25: dec c               ; c -= 1
26: jnz 1 -4            ; goto 22
27: jnz 0 0             ; 
            ; chunk 3.1.3
28: out b               ; output b
29: jnz a -19           ; if a != 0: goto 10
30: jnz 1 -21           ; goto 9
```

This can be converted into the following Python code
```python
# chunk 1
d = a
c = 4

# chunk 2
while c != 0:
    b = 643
    while b != 0:
        d += 1
        b -= 1
    c -= 1

# chunk 3
while True:
    a = d

    # chunk 3.1
    while a != 0:
        b = a
        a = 0
        
        # chunk 3.1.1
        c = 2
        while b != 0:
            b -= 1
            c -= 1
            if c == 0:
                a += 1
                c = 2

        # chunk 3.1.2
        b = 2
        while c != 0:
            b -= 1
            c -= 1

        # chunk 3.1.3
        print(b)
```


Let's simplify a bit. The most complicated part by far is `chunk 3.1.1`. I'll leave this as an exercise to the reader to convince yourself that this is correct. 
```python
# chunk 1, 2
c = 4
d = a + 4 * 643

# chunk 3
while True:
    a = d

    # chunk 3.1
    while a != 0:
        b = a

        # chunk 3.1.1
        a = b // 2
        c = 1 if b % 2 else 2

        # chunk 3.1.2
        b = 2 - c
        c = 0

        # chunk 3.1.3
        print(b)
```

We notice that actually `b // 2` is the same as `b >> 1`, so we can simplify this even further. And I'll drop lines that don't matter
```python
# chunk 1, 2
d = a + 4 * 643

# chunk 3
while True:
    a = d

    # chunk 3.1
    while a != 0:
        print(a % 2)
        a >>= 1
```

So, what is this program doing? It is **printing out the binary digits `d` in reverse order over and over again**. 

## Part 1

Part 1 asks us to find the smallest positive value of register `a` such that the program prints out 
```
0, 1, 0, 1, 0, 1, ...
```
infinitely. Therefore, we need to find the smallest positive value of `a` such that `d` in binary looks like `1010...10`. Based on the code
```
d = a + 4 * 643
```
so the minimum value of `d` is `2572`. So we need to find the smallest integer greater than `2572` such that its binary digits look like `1010...10`.


I'm sure there many ways to accomplished this. I build the number up from 0, essentially computing

$$
d^* = \sum_{k=0}^{N} 2^{2k}
$$

iteratively incrementing $N$ until I find $d^* \geq 2752$ and finally

$$
a^* = d^* - 2752
$$

See my implementation in the function `solution()` in `part_1.py`.