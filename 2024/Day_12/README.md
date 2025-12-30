# Day 12: Garden Groups

[Problem Link](https://adventofcode.com/2024/day/12)

I really like this problem. It requires a bit of everything to solve it - graph algorithms, intelligent data modeling, and some clever reframing. I think this is my favorite problem of Advent of Code 2024 so far.

## Background

### Some Definitions

- The **garden** is the entire input grid
- A **plot** is the index of the cell in the input grid
- A **plant** is the cell value in the input grid
- A **region** is a group of plots which are **orthogonally adjacent** and have the same plant type

Consider the following example grid

```
AAAAAA
AAABBA
AAABBA
ABBAAA
ABBAAA
AAAAAA
```

There are 2 plant types: `A` and `B`. There are 3 regions: one with all of the `A` plants, and two with the `B` plants.


## Part 1

### Preprocessing and Normalization

It is useful to abstract the grid of plots as an [undirected graph](https://en.wikipedia.org/wiki/Graph_(discrete_mathematics)#Undirected_graph). Each plot/plant is a vertex. There is an edge between a vertex if and only if the plot is orthogonally connected and has the same plant type (i.e. it's in the same region).

```
A-A-A-A-A-A
| | |     |
A-A-A B-B A
| | | | | |
A-A-A B-B A
|         |
A B-B A-A-A
| | | | | |
A B-B A-A-A
|     | | |
A-A-A-A-A-A
```

We can see that this definition correctly distinguishes each region as required to solve the problem; we just need to compute these regions. This can be done using a graph traversal, either [Breadth-First Search](https://en.wikipedia.org/wiki/Breadth-first_search) (BFS) or [Depth-First Search](https://en.wikipedia.org/wiki/Depth-first_search) (DFS). The result is a list of [components](https://en.wikipedia.org/wiki/Component_(graph_theory)). This is problem, this a list of garden indices partitioned into each distinct region.

```
regions = [
  {(4, 0), (3, 4), (4, 3), (5, 4), (5, 1), (0, 2), (0, 5), (2, 2), (1, 0), (2, 5), (3, 0), (4, 5), (3, 3), (5, 0), (5, 3), (0, 1), (1, 2), (0, 4), (2, 1), (1, 5), (3, 5), (5, 2), (4, 4), (5, 5), (0, 0), (1, 1), (0, 3), (2, 0)},
  {(2, 3), (2, 4), (1, 3), (1, 4)},
  {(3, 1), (3, 2), (4, 1), (4, 2)}
]
```

Now that we have each of the distinct regions, let's re-label this grid accordingly. For example, 

```
111111
111221
111221
133111
133111
111111
```

I will call these re-labeled region values the `region_ID`. For example, the plant `A` became the `region_ID` `1`

Furthermore, to solve this problem we need to identify certain properties of the boundaries of each region. When the boundary of a region coincides with the boundary of the entire garden, it causes annoying edge cases. For this reasion, I added a layer of padding.

```
00000000
01111110
01112210
01112210
01331110
01331110
01111110
00000000
```

This _normalized_ version of the garden makes answering the question much easier.

### Computing the Area

The area of each region is just the number of times its `region_ID` appears in the garden. I computed this by taking the length of the region indices.

```python
area = len(region_indices)
```

### Computing the Perimeter

The perimeter of each region can by computed by counting the number of 

counting the **number of edges segments** in the region. An edge occurs when a region has a neighbor which is outside of its region. Thus, one way of computing the perimeter is the following.

1. Given a `region_ID` and corresponding region `R`
2. **Initialize** `perimeter = 0`
3. **For each** `plot_index` in region `R`
    1. Get all orthogonally adjacent neighbors to `plot_index`
    3. Increment `perimeter` the number of neighbors which are not part of region `R`

The above algorithm was implemented in `part_1.py`. This could be made a bit more efficient by iterating over the entire garden and computing all perimeters simultaneously, and this method aligns nicely with the solution to part 2. This was done in `part_1_alt.py`. The solution is not noticeably faster. Much of the time is spent on computing the distinct regions.


## Part 2 

All of the same normalizations in part 1 also apply to part 2. Thus, we have the normalized garden 

```
00000000
01111110
01112210
01112210
01331110
01331110
01111110
00000000
```

Computing the area is exactly the same as part 1. Thus, the main task of part 2 is computing the **number of edges** of each region. This is more difficult than computing the perimeter. Recall in part 1 that the perimeter could be computed by aggregating local information (i.e. adjacent cells in different regions). However, an edge could be as long as the entire grid. Thus, local information doesn't seem to help us here.

After some thought, I finally had the insight that **number of edges == number of corners**. Since corners are a single point rather than a variable length line, they _can_ be determined with only local information. I believe this was the intended solution.

The idea of my solution is to iterate over every `2x2` square in the grid and determine if that square contains a corner. For example

```
+--+             +--+
|00|000000      0|00|00000
|01|111110      0|11|11110
+--+             +--+
 01 112210      0 11 12210
 01 112210      0 11 12210
 01 331110      0 13 31110
 01 331110      0 13 31110
 01 111110      0 11 11110
 00 000000      0 00 00000
```

The left example is a corner and the right example is not a corner. One way to identify corners in a `2x2` grid is to count the number of cells with the same `region_ID`. If the total is odd, then there is a corner. If the total is even, then it's not a corner with 1 important exception.

```
000 00 000
011 11 110
011 12 210
   +--+
011|12|210
013|31|110
   +--+
013 31 110
011 11 110
000 00 000
```

From the perspective of region `1`, there are actually 2 corners here. This exception occurs when the `2x2` region is a checkerboard.


### Efficiency Improvements

My first iteration of this solution is found in `part_2_slow.py`. Here I compute each `region_ID` individually. I can't do something like in part 1 where I get all orthogonal neighbors because I would double-count some corners. To efficiently iterate over regions I would have to know where the corners are apriori, which is what I'm trying to compute in the first place. So I take the brute-force approach and iterate over all `2x2` squares in the grid. Since this is done for each region, this is not very fast.

A better approach is to do a single sweep of all `2x2` regions and compute the number of corners of each `region_ID` simultaneously. This is my implementation in `part_2.py`. This solution runs faily quickly, with most of the run-time dedicated to computing the distinct regions.
