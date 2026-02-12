# Day 21: Fractal Art

[Problem Link](https://adventofcode.com/2017/day/21)

## Part 1 and Part 2

The solution is to just code the problem as described. The difficulty comes in just managing all of the data structures. 

I like my solution at a high-level, but I think the way I handled the details could use improvement. But hey, it works and it's pretty fast.

### Rule Preprocessing

The input is a list of rules which tell you how to transform an **input pattern** into an **output pattern**. Since each input pattern is unique, we can store this as a dictionary. For example,

```python
{
    "../..":        "..#/##./#..",
    "##/..":        "##./#../##.",
    ".#/#.":        "..#/##./.#.",
    ".#./#../...":  "###./..##/#..#/#...",
    "###/#../...":  ".###/#.../#..#/.##.",
    "#.#/.##/#..":  "##../#..#/#.../####"
}
```

Then, I preprocess this object `rules_by_size`, which partitions the rules by the side of the input pattern. The corresponding object for the above example is
```python
{
    2: {
        "../..":        "..#/##./#..",
        "##/..":        "##./#../##.",
        ".#/#.":        "..#/##./.#.",
    },
    3: {
        ".#./#../...":  "###./..##/#..#/#...",
        "###/#../...":  ".###/#.../#..#/.##.",
        "#.#/.##/#..":  "##../#..#/#.../####"
    }
}
```

In my actual code I did not store these as strings. I stored the input pattern as a flat boolean tuple and the output pattern as a numpy array. See the function `preprocess_rules()` in `part_1.py`.

### Grid Transformation

You could use the fact that the grid is always expanding in size by exactly 1 to code this more cleaning (e.g. add padding around the perimeter). However I coded this pretty generally.

I iterate over each size in the `rules_by_size` object (in numerical order). Then, I split the grid into a list of its corresponding sub-grids. Then I replace each sub-grid with its pattern. Finally, I merge the new sub-grids back together. Exactly as the problem describes. See `partition_by_size_and_apply_rules()` and `merge_subgrids()` in `part_1.py` for the details.

### Key to Decreasing Runtime

I think the key insight of this problem is to preprocess all of the different orientations of each input pattern. For example, consider the rule
```
..              ##.
.#      -->     #..
                ...
```

As a part of the rules preprocessing, I find all of the unique orientations of each 
input pattern, and map it to the same output pattern. For example

```
..              ##.
.#      -->     #..
                ...

..              ##.
#.      -->     #..
                ...

#.              ##.
..      -->     #..
                ...

.#              ##.
..      -->     #..
                ...
```

For a linear increase in memory, this will save a lot of computation; turning a linear search into an O(1) lookup. Note that the asymptotic memory is still O(n), we have just increased the constant in front of the linear term.