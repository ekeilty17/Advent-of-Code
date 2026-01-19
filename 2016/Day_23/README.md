# Day 23: Safe Cracking

[Problem Link](https://adventofcode.com/2016/day/23)

## Part 1

Initially for part 1, I simulated the instructions the brute-force way, adding extra logic to handle the new `tgl` instruction. However, in `part_1_disassembled.py`, I also solved it by figuring out what the code in `input.txt` is actually doing, which was required for part 2.

## Part 2 

Part 2 requires us to disassemble the code, as it takes too long to compute the brute-force way. The following are the opcodes with comments explaining the lines

```
            ; chunk 0
1 : cpy a b         ; b = a
2 : dec b           ; b -= 1
            ; chunk 1
            ; chink 1.1
3 : cpy a d         ; d = a
4 : cpy 0 a         ; a = 0
5 : cpy b c         ; c = b
6 : inc a           ; a += 1
7 : dec c           ; c -= 1
8 : jnz c -2        ; if c != 0: goto 6
9 : dec d           ; d -= 1
10: jnz d -5        ; if d != 0: goto 5
            ; chunk 1.2
11: dec b           ; b -= 1
12: cpy b c         ; c = b
13: cpy c d         ; d = c
14: dec d           ; d -= 1
15: inc c           ; c += 1
16: jnz d -2        ; if d != 0: goto 14
17: tgl c           ; toggle 17+c (c is always positive and even)
18: cpy -16 c       ; c = -16
19: jnz 1 c         ; toggled: (goto 3) OR (c = 1)
            ; chunk 2
20: cpy 81 c        ; c = 81
21: jnz 73 d        ; toggled: d = 73
22: inc a           ; a += 1
23: inc d           ; toggled: d -= 1
24: jnz d -2        ; if d != 0: goto 22
25: inc c           ; toggled: c -= 1
26: jnz c -5        ; if c != 0: goto 21
```

Let's take a second to understand how `17: tgl c` works. Following the flow of the code (which we will see shortly), you'll notice that `c` is always even and is decreasing. So essentially, the **toggle** will toggle each opcode an even number of lines after line `17`, i.e. line `19`, `21`, `23`, and `25`.

Now, lets see what this looks like in python code.

```python
# chunk 0
b = a
b -= 1

# chunk 1
while c != 2:        # when c == 2, the jnz instruction becomes cpy

    # chunk 1.1
    d = a
    a = 0
    while d != 0:
        c = b
        while c != 0:
            a += 1
            c -= 1
        d -= 1

    # chunk 1.2
    b -= 1
    c = b
    d = c
    while d != 0:
        d -= 1
        c += 1

# chunk 2
c = 81
while c != 0:
    d = 73
    while d != 0:
        a += 1
        d -= 1
    c -= 1
```

This can be condensed to the following. Notice that `c = 2*b` so we can replace the condition in the `while` loop and get rid of `c` all together.

```python
# chunk 0
b = a - 1

# chunk 1
while b != 1:
    # chunk 1.1
    a += a * b

    # chunk 1.2
    b -= 1

# chunk 2
a += 81 * 73
c = d = 0
```

Now consider what `chunk 1` is doing. We're iteratively multiplying `a` by `a-1`. This is exactly the factorial function! So the code is further condensed to.

```python
# chunk 1
import math
a = math.factorial(a)
b = 1

# chunk 2
a += 81 * 73
c = d = 0
```

Let $n$ be the number of eggs in the puzzle (which is what register `a` is set to), then the value that is set to the safe is

$$
n! + 73 \cdot 81
$$

And now we understand what the hint
> Don't bunnies usually multiply?

was implying.