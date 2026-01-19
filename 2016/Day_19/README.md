# Day 19: An Elephant Named Joseph

[Problem Link](https://adventofcode.com/2016/day/19)

## Part 1

This is a cool problem, I solved it twice. Once to get a solution that I knew was right by simulating it, and then again to solve it in nanoseconds once I understood the pattern.

### Simulation

In the function `simulate()`, I essentially simulate the problem as described, but still semi-efficiently. I maintain a list `elves` which is just a list of integers `1` to `num_elves`. Starting from the beginning of the list of elves, every odd-index elf get their presents stollen, and therefore don't contribute, so they are removed from the list. This is the purpose of
```python
elves = elves[::2]
```

If the original `elves` list was **even** in length, then we will end by the second-to-last elf steeling from the last elf. And then we have the same situation as before but a smaller list. If the original `elves` list was **odd** in length, then the last elf will steel from the new first elf. That is the purpose of the lines
```python
if is_odd:
    elves = elves[1:]
```

and now again, we can start at the beginning of the `elves` list and recurse until it's length `1`.

### Formula

Now we want to see if we can solve this much more efficiently. I printed out the first 100 solutions

```python
for n in range(2, 100):
    print(n, simulate(n))
```

and a clear pattern emerges.

| num_elves | 1 |  2  |  3  |  4  |  5  |  6  |  7  |  8  |  9  | 10  | 11  | 12  | 13  | 14  | 15  | 16  |
|:----------|:-:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| solution  | 1 |  1  |  3  |  1  |  3  |  5  |  7  |  1  |  3  |  5  |  7  |  9  | 11  | 13  | 15  |  1  |

We see that if the number of elves is a perfect power of 2, then elf `1` will win. If you run through the simulation yourself, you'll see why.

Let $n$ be the number of elves, and let $a$ be the largest integer such that $2^a < n$ (e.g. $a = \lfloor\log_2 n \rfloor$). Essentially what happens is the elf who wins is completely determined by the number of elfs left over after $2^a$. Every time we remove half of the list, those elves will be left over and remove an elf from the front of the list. 

After some thought, I came up with the following formula for the winning elf.

$$
2 \cdot (n - 2^a) + 1
$$

In my solution, I compute $n - 2^a$ using a bit-mask. See `compute()` in `part_1.py` for the details.

## Part 2 

I employed a similar strategy to solve this one. Simulate and then pattern match to find a faster formula.

### Simulation

This simulation is much more tricky as I think I have to remove elves one by one. I cannot do a batch like I could in part 1. 

First, `i` is the index of the elf who is stealing from elf at index `j`. Based on the problem description
```python
m = len(elves) // 2
j = (i+m)%len(elves)
```

Now, if `j <= i`, then when I call `del elves[j]`, `i` will be automatically incremented by `1`. It's only if `j > i` do I need to increment `i`.

### Formula

Again, I just ran 
```python
for n in range(2, 100):
    print(n, simulate(n))
```

to see what happened and again a clear pattern emerges.

| num_elves | 1 |  2  |  3  |  4  |  5  |  6  |  7  |  8  |  9  | 10  | 11  | 12  | 13  | 14  | 15  | 16  | 17  | 18  | 19  | 20  | 21  | 22  | 23  | 24  | 25  | 26  | 27  |
|:----------|:-:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| solution  | 1 |  1  |  3  |  1  |  2  |  3  |  5  |  7  |  9  |  1  |  2  |  3  |  4  |  5  |  6  |  7  |  8  |  9  | 11  | 13  | 15  | 17  | 19  | 21  | 23  | 25  | 27  |

Like before, let $n$ be the number of elves and $a$ be the largest integer such that $3^a \leq n$ (e.g. $a = \lfloor\log_3 n \rfloor$). Just through rote pattern matching, I derived the following formula for the winning elf.

$$
\begin{cases}
    n &\quad\text{if } n = 3^a \\
    n - 3^a &\quad\text{if } 3^a < n < 2 * 3^a \\ 
    3^a + 2 \cdot (n - 2 \cdot 3^a) &\quad\text{if } n \geq 2 \cdot 3^a %\\
    % 2 \cdot (n - 3^a) - 3^a &\quad\text{if } n \geq 2 \cdot 3^a
\end{cases}
$$

That last case might seem tedious, but it's more natrual to implement when considering $n$ as a trinary number. $(n - 2 \cdot 3^a)$ is just removing the most significant trit. For the full implementation, see `compute()` in `part_2.py`.