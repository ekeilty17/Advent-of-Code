# Day 7: Internet Protocol Version 7

[Problem Link](https://adventofcode.com/2016/day/7)

## Part 1

Not much to this one. The most annoying part was writing the `load_input()` function and separating the supernet sequences from the hypernet sequences. After that, just need to write the `is_abba()` function and apply the logic as described by the problem.

## Part 2 

First, I wrote a function `get_all_aba()` which given a sequence string finds all instances of `aba`. From this, I can get the set of all `ABA` strings in supernet and likewise all `ABA` in the hypernet. Then, convert `ABA` to `BAB` in one of the nets, e.g.
```python
supernet_bab = set([b + a + b for a, b, _ in supernet_aba])
```

Now, just take the set intersection. If any intersection exists, then it supports SSL.
```python
return bool(supernet_bab & hypernet_aba)
```