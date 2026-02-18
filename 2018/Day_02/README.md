# Day 2: Inventory Management System

[Problem Link](https://adventofcode.com/2018/day/2)

## Part 1

In this part, I write a function `get_letter_counts()` which counts the number of instances of every character in a string. This is essentially the same as calling [Counter](https://docs.python.org/3/library/collections.html#collections.Counter) from the collections library in Python.

Using my counter dictionary, I can easily check if any letter has a frequency of `2` or `3`, and return the desired result.

## Part 2 

In part 2, I write a function `get_common_letters()` which returns the common parts between two strings. For example
```python
get_common_letters("fghij", "fguij") == "fgij"
```

To find the solution, I just check if the length of the common substring is one less than the length of the IDs. This means the two ID strings must have differed by exactly 1 character.