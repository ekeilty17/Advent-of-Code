# Day 12: Leonardo's Monorail

[Problem Link](https://adventofcode.com/2016/day/12)

## Part 1

This is another problem where the solution is to just similate as described by the problem. The instruction logic is written in `opcodes.py`. In `part_1.py`, the `compile()` function compiles the opcodes, maintaining the registers and a program counter (`pc`).

## Part 2 

Exactly the same as part 1, just a different initial configuration of the registers.

## Disassembling

The following are the opcodes with comments explaining the lines

```
                ; chunk 0
1 :     cpy 1 a         ; a = 1
2 :     cpy 1 b         ; b = 1
3 :     cpy 26 d        ; d = 26
4 :     jnz c 2         ; if c != 0: goto 6
5 :     jnz 1 5         ; goto 10
                ; chunk 1
6 :     cpy 7 c         ; c = 7
7 :     inc d           ; d += 1
8 :     dec c           ; c -= 1
9 :     jnz c -2        ; if c != 0: goto 7
                ; chunk 2
10:     cpy a c         ; c = a
11:     inc a           ; a += 1
12:     dec b           ; b -= 1
13:     jnz b -2        ; if b != 0: goto 11
14:     cpy c b         ; b = c
15:     dec d           ; d -= 1
16:     jnz d -6        ; if d != 0: goto 10
                ; chunk 3
18:     cpy 17 c        ; c = 17
19:     cpy 18 d        ; d = 18
20:     inc a           ; a += 1
21:     dec d           ; d -= 1
22:     jnz d -2        ; if d != 0: goto 19
23:     dec c           ; c -= 1
24:     jnz c -5        ; if c != 0: goto 18
```

Now, let's rewrite this code in a more modern notation. The following is the equivalent Python code

```python
# chunk 0
a = 1
b = 1
d = 26

# chunk 1
if c != 0:
    c = 7
    while c != 0:
        d += 1
        c -= 1

# chunk 2
while d != 0:
    c = a
    while b != 0:
        a += 1
        b -= 1

    b = c
    d -= 1

# chunk 3
c = 17
while c != 0:
    d = 18
    while d != 0:
        a += 1
        d -= 1
    c -= 1
```

This simplifies into the following code. I'll leave it as an exercise to the reader to convince themselves that this is correct. 

```python
# chunk 0
a = 1
b = 1
d = 26

# chunk 1
if c != 0:
    d += 7

# chunk 2
for _ in range(d):
    b, a = a, a + b

# chunk 3
a += 17*18
```

Interestingly, chunk 2 is computing the Fibonnaci numbers since `a = b = 1`. Since `c` is effectively the input to this code (since `a`, `b`, and `d` all get overwritten), the algorithm computes

$$
17 \cdot 18 + \begin{cases}
    \text{Fib}(26) &\quad\text{if } c = 0 \\
    \text{Fib}(33) &\quad\text{if } c \neq 0
\end{cases}
$$

The files `part_1_disassembled.py` and `part_2_disassembled.py` implement the disassembled code.