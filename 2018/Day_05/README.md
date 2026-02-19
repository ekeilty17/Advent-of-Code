# Day 5: Alchemical Reduction

[Problem Link](https://adventofcode.com/2018/day/5)

## Part 1

We need to somehow model the recursive nature of the destruction. Using the example given by the problem,
```
dabA[cC]aCBAcCcaDA      <-- 'cC' destruct
dab[Aa]CBAcCcaDA        <-- 'Aa' destruct
dabCBAcCcaDA
```

Any algorithm which linearly iterates through the polymer would have already processed `A` and decided it should not be removed. But it actually does need to be removed due to the destruction of future elements.

### Naive Solution

The naive solution is to linearly iterate over the polymer and **delete** pairs which "match". Then, we have to move our pointer back by 1 to check for recursive destructions. This looks something like the following

```python
if is_match(polymer[i], polymer[i+1]):
    polymer = polymer[:i] + polymer[i+2:]       # destroy `polymer[i]` and `polymer[i+1]`
    i -= 1                                      # check for match on previous index
```

This is implemented in the function `reduce_polymer_slow()` in `part_1.py`. However, this algorithm $O(n^2)$ because in the worse case we have to make a copy of the polymer list in each iteration. It's not terrible, but we can do better.

### Efficient Solution

To solve this problem in linear time, each iteration has to do only constant time operations. The idea is to maintain a new list `reduced_polymer` which will eventually contain the final polymer after all of the destructions. We iterate linearly over the `polymer` list. In each iteration we compare the last unit in `reduced_polymer` to the current unit in `polymer`. If there is a match, then we **pop** the last unit out of `reduced_polymer`. If there is no match, then we **append** the current unit to `reduced_polymer`.

Let's show an example

```
        dabAcCaCBAcCcaDA        # No match, add 'd'
^       ^
d       dabAcCaCBAcCcaDA        # No match, add 'a'
^        ^
da      dabAcCaCBAcCcaDA        # No match, add 'b'
 ^        ^
dab     dabAcCaCBAcCcaDA        # No match, add 'A'
  ^        ^
dabA    dabAcCaCBAcCcaDA        # No match, add 'c'
   ^        ^
dabAc   dabAcCaCBAcCcaDA        # 'c' matches with 'C', remove 'c'
    ^        ^
dabA    dabAcCaCBAcCcaDA        # 'A' matches with 'a', remove 'A'
   ^          ^
dab     dabAcCaCBAcCcaDA        # No match, add 'C'
  ^            ^
dabC    dabAcCaCBAcCcaDA
   ^            ^
```

The right pointer gets to just iterate linearly over the given polymer, and the left pointer is just the last element in the reduced polymer. Very elegant, very fast, and very memory efficient. This algorithm is implemented in the function `reduce_polymer()` in `part_1.py`.

Note that the `reduced_polymer` is operating like the [stack](https://www.geeksforgeeks.org/dsa/stack-data-structure/) data structure.

## Part 2 

I brute forced part 2 by removing each "unit type" from the polymer and running the code from part 1 to determine the resulting reduced polymer. The solution is the minimum length polymer that can be produced