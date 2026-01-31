# Day 4: High-Entropy Passphrases

[Problem Link](https://adventofcode.com/2017/day/4)

## Part 1

Just need to correctly implement the `is_valid_passphrase()` function. In part 1, this meant just iterating through every word and keeping track of the ones you have already seen. If you get a duplicate, then return `False`. If no duplicates, then return `True`. This is the perfect application for the [Set](https://en.wikipedia.org/wiki/Set_(abstract_data_type)) data structure. 

## Part 2 

This is almost the same as part 1, except now we care about unique **anagrams** rather than unique words. Instead of storing each word in our set, we store 
```
anagram = tuple(sorted(word))
```

This means that both `abcd` and `dcba` map to `abcd`. Therefore, they would count as duplicate words.