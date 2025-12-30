# Day 17: Chronospatial Computer

[Problem Link](https://adventofcode.com/2024/day/17)

## Part 1

Part 1 is straight forward. Just read the question carefully and implement the compiler as described.

One thing to note is the implementation of floor division by powers of 2. You could implement that as follows
```
x //= 2**n
```
However, you can equivalently implement it as a bit-wise shift
```
x >>= n
```
which is faster.

## Part 2 

Part 2 was quite tricky. It is asking us to find a [quine](https://en.wikipedia.org/wiki/Quine_(computing)) for our compiler, i.e. a program which generates its own source code. We do this by searching for the appropriate value for register `A`.

### Brute Force is Too Slow

Using our compiler from part 1, we can just iterate through all values of register `A` until we find a value which generates the program. However, the solution value for register `A` is far too large for this to work.

This naive solution is implemented in `part_2_slow.py`.

### Disassembling the Program

The first thing you need to do is "disassemble" the program. The first key insight is to notice that it's one giant loop. Both the example and actual inputs end with the instruction `3, 0` which encodes the logic.
1. **If** register `A == 0`, **then** halt
2. **Else** the instruction pointer jumps to position `0`

Now the question is, what happens in each loop iteration? First let's see the example input:
```
A: x
B: 0
C: 0
output: []

A: x >> 3
B: 0
C: 0
output: [(x >> 3) % 8]
```

We see that each iteration of the example program bit-shifts register `A` to the right by `3` (thus reducing its value), and then outputs some value (which we'll treat as pseudo-random). This loop will continue until register `A` has value `0`, then the program will terminate.

The actual program is similar, there is it's loop iteration:
```
A: x
B: 0
C: 0
output: []

A: x >> 3
B: ((x >> 3) % 8) ^ 5 ^ (x >> ((x >> 3) % 8))
C: x >> ((x >> 3) % 8)
output: [(x >> ((x >> 3) % 8)) % 8]
```

For all intents and purposes, the values of register `B`, `C` and `output` are pseudo-random. The key to solving this efficiently is the bit-shifting of register `A` after each iteration. Now let's see how we take advantage of that.

### The Efficient Solution

The key idea is to search backwards through the program. The target output is `2,4,1,3,7,5,1,5,0,3,4,2,5,5,3,0`. So we search as follows
1. Find a program which outputs `0`
2. Find a program which outputs `3,0`
3. Find a program which outputs `5,3,0`
4. Find a program which outputs `5,5,3,0`
5. Continue until you construct the entire program

Since `[0, 8) >> 3 == 0`, this is a bit of an edge case, so let's skip to the second iteration.

Using a linear search, we can find that `49` will produce and output of `3`. Then `49 >> 3 == 6` which produces an output of `1`. Therefore, setting register `A` to `49` will produce `3,0`.

Now in the third iteration, we know that any number `x` such that `x >> 3 == 49` will output `3,0`. Therefore, we should start at `49 << 3`. If that produces a `5` in the first iteration, then we are done. Otherwise, do a linear such until we find a number that does.

So, the full algorithm is the following
1. Initialize `register_A = 1`
2. **For each** `n = 2..(len(program)+1)`
    1. `register_A <<= 3` 
    2. **While** `True`
        1. run the program with `register_A` set
        2. **If** `output == program[-n:]`, **then** break while loop
        3. **Else** `register_A += 1`

`n = 1` is a weird edge-case as discussed above, so that's why I start at `n = 2`.

## Part 1 and Part 2 Alternative Solutions

Since I fully disassembled the program, I can actually simulate the entire loop in a single step, rather than using the `run_program()` function from. This is implemented in `part_1_alt.py` and `part_2_alt.py`. The time save here is probably negligible, I just thought it was interesting. 