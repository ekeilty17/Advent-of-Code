# Day XX: ??

[Problem Link](https://adventofcode.com/2017/day/XX)

## Part 1

You can just simulate the opcodes, counting the number of times the `mul` instruction is executed. And this runs reasonably efficiently.

However, If we disassemble the program, we can solve part 1 by hand. After analyzing the input code, and converting it into modern notation it looks something like this

```python
def simplified():
    a = b = c = d = e = f = g = h = 0
    b = c = 79

    if a != 0:
        b = 100*b + 100000
        c = b + 17000

    for b in range(b, c+17, 17):
        f = 1
       
        for d in range(2, b):
            if b % d == 0:
                f = 0
            # (b - 2) mul instructions happen here

        if f == 0:
            h += 1
    
    return num_mul
```

Each variable has a clear interpretation
- `a` is a boolean to toggle part 1 and part 2 parameters
- `b` is the loop variable
- `c` is the upper-bound of the loop

The main loop iterates over the range `[b, c]` in steps of `17`. The interpretations of `d`, `f`, and `h` will be discussed in part 2. 

For part 1 all we care about are the number of multiplication instructions. We notice that `d` iterates `b - 2` times and does `b - 2` multiplications in each iteration. So in each iteration, we do `(b - 2)**2` multiplications.

Since `b == c`, there will only be 1 loop iteration. Therefore, the solution to part 1 will just be
$$
(79 - 2)^2 = 77^2 = 5929
$$

For the full analyze of the disassembled code, see the various functions in `part_1_disassembled.py`.

## Part 2 

For part 2, we need to figure out what the input code is actually computing. This brings us to the interpretations of the rest of the variables
- `d` is a potential factor of `b`
- `f` is a boolean indicating whether `b` is a prime
- `h` is a counter for the number of composite numbers found in the range `[b, c]`

Now that we understand this, we can greatly simplify it.

```python
def part_2():
    start = end = 79
    start = 100*start + 100000
    end = start + 17000

    num_composites = 0
    for n in range(start, end+17, 17):
        for k in range(2, n):
            if n % k == 0:
                num_composites += 1
                break
    
    return num_composites
```

This is called [Trial Division](https://en.wikipedia.org/wiki/Trial_division) for determining if something is prime. Actually we can add an easy improvement by modifying the second for-loop to
```python
for k in range(2, int(math.sqrt(n))+1):
```
since we only need to check up to $\sqrt{n}$ for prime factors.

There are also better algorithms than this, such as the [Segmented Sieve](https://www.geeksforgeeks.org/dsa/segmented-sieve-print-primes-in-a-range/) for getting primes within a range.