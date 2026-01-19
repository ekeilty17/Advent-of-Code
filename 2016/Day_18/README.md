# Day 18: Like a Rogue

[Problem Link](https://adventofcode.com/2016/day/18)

## Background

### Elementary Cellular Automata

What this problem is asking us to do is simulate an [Elementary Cellular Automaton](https://en.wikipedia.org/wiki/Elementary_cellular_automaton). There are $2^{2^3} = 256$ possible rules to update a cell given itself and its left/right neighbors. 

If `1` indicates a **trap cell**, then the update rules for this problem are

| Neighborhood | 111 | 110 | 101 | 100 | 011 | 010 | 001 | 000 |
|--------------|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Next State   |  0  |  1  |  0  |  1  |  1  |  0  |  1  |  0  |

which is rule `01011010` which corresponds to [Rule 90](https://atlas.wolfram.com/01/01/90/).

Conversely, if `1` indicates a safe cell, then the update rules for this problem are

| Neighborhood | 111 | 110 | 101 | 100 | 011 | 010 | 001 | 000 |
|--------------|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Next State   |  1  |  0  |  1  |  0  |  0  |  1  |  0  |  1  |

which is rule `10100101` which corresponds to [Rule 165](https://atlas.wolfram.com/01/01/165/).


### Boolean Algebra

Let $\ell$, $c$, and $r$ be boolean variables representing if the left, center, and right tiles are **traps**. As described by the problem, whether a cell is a **trap** in the next iteration is determined by this boolean formula.

$$
T = (\ell \wedge c \wedge \overline{r}) \vee (\overline{\ell} \wedge c \wedge r) \vee (\ell \wedge \overline{c} \wedge \overline{r}) \vee (\overline{\ell} \wedge \overline{c} \wedge r)
$$

If you play around with it, you'll notice that this simplifies to the following [disjunctive normal form](https://en.wikipedia.org/wiki/Disjunctive_normal_form) (DNF)

$$
T = (\ell \wedge \overline{r}) \vee (\overline{\ell} \wedge r)
$$

or we could express in [conjunctive normal form](https://en.wikipedia.org/wiki/Conjunctive_normal_form) (CNF)

$$
T = (\ell \vee r) \wedge (\overline{\ell} \vee \overline{r})
$$

## Part 1

In part 1, I implemented this in a way that easy to understand but not necessarily the fastest to compute. I improve upon this implementation in part 2.

The first step is to negate everything in our derived formula for $T$. So now $\ell$, $c$, and $r$ represent whether a cell is **safe** and the boolean formula indicates whether the updated cell is **safe**.

$$
S = \overline{T} = (\ell \vee \overline{r}) \wedge (\overline{\ell} \vee r)
$$

This is implemented in `is_safe()`.

Now, for each row I maintain a boolean list indicating which cells are safe, for example

```
"..^^." --> [True, True, False, False, True]
```

Then, I pad the front and end with `True` to as indicated by the problem.
> nonexistent, so we assume "safe"

Finally, iterate over every triplet in the padded list to generate the new list.

```
[True, True, True,  False, False, True, True]
[      True, False, False, False, False     ]
```

Finally, repeat for the desired number of iterations.

## Part 2 

We can improve on the part 1 implementation by taking advantage of binary. We can encode a row using a binary integer instead of a list of booleans

```
"..^^." --> 11001
```

Now, we compute `left` and `right` by bit-shifting.

```
left   = 10010      # center << 1
center = 11001
right  = 01100      # center >> 1
```

Then we just need to replace the added `0`'s due to the bit shifting with `1`'s to indicate they are safe

```
left   = 10011
center = 11001
right  = 11100
```

And now, we apply the boolean formula all at once

```
row = (~left | right) & (left | ~right)
```

And this is much faster as binary operations are the fastest things computers can compute.

There is some extra complication that when we negate we need to ensure the bit-string is the exact length for the problem. See the `update()` function for those details.