# Day 10: Knot Hash

[Problem Link](https://adventofcode.com/2017/day/10)

## Part 1

The crux of this problem is being able to reverse a circular subsection of a list. For example,
```
2 1) 0 (3 4   -->     4 3) 0 (1 2
```

I was trying to be a bit too fancy with this at first, and ultimately I think the most efficient and most straight-forward way is to do this using element-wise swaps. Using the above example

```
 2  {1}) 0 ({3}  4      -->      2  {3}) 0 ({1}  4
{2}  3 ) 0 ( 1  {4}     -->     {4}  3 ) 0 ( 1  {2}
```

The benefit of this is that everything occurs in-place, it does the minimum possible number of list operations, and it's simple to implement.

## Part 2 

Once we have the `knot_hash_round()` function written in `part_1.py`, the rest is just following the instructions of the Knot Hash function.