# Day 5: Doesn't He Have Intern-Elves For This?

[Problem Link](https://adventofcode.com/2015/day/5)

## Part 1

The solution consists of writing logic for each of the three conditions.

#### Condition 1

Filter the string by only the characters which are vowels `aeiou`, an check if the length is greater than or equal to `3`.

#### Condition 2

Iterate through each pair of contiguous characters in the string `a, b`, and check if the `a == b`.

#### Condition 3

Iterate through each pair of contiguous characters in the string, and check if they are one of `["ab", "cd", "pq", "xy"]`

## Part 2 

The solution consists of writing the logic for each of the two conditions.

#### Condition 1

The annoying part of this one is dealing with the exceptions due to overlapping, e.g. `aaa` does not pass condition 1. To do this, I iterate over each set of four contiguous characters in the string `a, b, c, d`. In the generic case, we check if the pair `(a, b)` have appeared previously in the string. 

There are two exception cases. 1) if `a == b == c == d` which passes condition 1. 2) if `a == b == c` with a different `d`, and this does not pass condition 1.

#### Condition 2

Iterate through each triplet of contiguous characters in the string `a, b, c`, and check if `a == c`.