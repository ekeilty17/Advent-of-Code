# Day 3: Perfectly Spherical Houses in a Vacuum

[Problem Link](https://adventofcode.com/2015/day/3)

## Part 1

The question asks

> How many houses receive at least one present?

Which can be translated as "How many positions did Santa visit"? This is a perfect application of a [set](https://en.wikipedia.org/wiki/Set_(abstract_data_type)). Each position that Santa visits gets added to the set, and at the end we return the length of the set.

## Part 2 

This is essentially the same as part 1 except we have two position trackers, one for Santa and the other for robot Santa. Critically we still only maintain one set representing all of the houses that either Santa or robot Santa visited.