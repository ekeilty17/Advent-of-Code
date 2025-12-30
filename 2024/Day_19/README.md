# Day 19: Linen Layout

[Problem Link](https://adventofcode.com/2024/day/19)

## Part 1

Given a list of available towel patterns and a desired design, we are asked to determine if the design is possible to create by patching together a sequence of the available patterns. 

I solve this using a standard [Depth-First Search](https://en.wikipedia.org/wiki/Depth-first_search) (DFS) with the appropriate pruning. I believe this is essentially how someone would do this by hand. Let's define a **subdesign** as a substring of the desired design starting at index `0`. For example, `brw` is a subdesign of `brwrr`.

Starting with an empty string `subdesign = ""`, we try appending each of the available patterns. If `subdesign | pattern` is also a subdesign, then continue to the next iteration, otherwise prune. If ever `subdesign | pattern` is the desired towel design, then return `True`.

As an example, let `r, wr, b, g, bwu, rb, gb, br` be the list of available patterns. Let `brwrr` be the desired design. The DFS search only including nodes which are subdesigns is the following

```
b
|
+-  br
    |
    +-  brwr
        |
        +- brwrr
br
|
+-  brwr
    |
    +- brwrr
```

And since we are using a DFS, the second `br` subtree is never searched. 

## Part 2 

This question asks use to find the number of ways each desired design can be created from the available patterns. This is a classic combinatorics dynamic programming question.

As an example, let `rrbgbr` be the desired design, and let `r, wr, b, g, bwu, rb, gb, br` be the list of available patterns. Thus
```
rrbgbr = rrbgb | r

OR

rrbgbr = rrbg | br
```

Therefore, in order to create the design `rrbgbr`, we must first create either the design `rrbgb` or `rrbg`, and then we can add `r` or `br` respectively. Thus, we've reduced the problem into 2 smaller subproblem. Now we must determine the many ways can be create `rrbgb` and `rrbg`. And the number of ways to create `rrbgbr` is the sum of the number of ways to create `rrbgb` and `rrbg`.


Let's generalize. Let `target` be the string representing the desired design. Also suppose `N = len(target)`. Then, let `C[0..N]` denote the number of wants that subdesign `target[:n]` can be created from the available patterns. Then, the simplified <??> equation is the following

```
C[n] = sum(C[n-len(p)] for p in patterns)
```

There are some base-cases you have to consider, such as when `C[n] == pattern`. You can see the implementation in `part_2.py` for those details. The solution to part to is then `C[N]`.