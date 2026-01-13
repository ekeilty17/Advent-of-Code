# Day 3: Squares With Three Sides

[Problem Link](https://adventofcode.com/2016/day/3)

## Part 1

Each row represents a tuple of triangle sides. Just iterate and count how many are valid triangles using the function
```python
def is_valid_triangle(a: int, b: int, c: int) -> bool:
    return (a+b > c) and (b+c > a) and (c+a > b)
```

## Part 2 

The hardest part is just parsing the input to get the list of all triangles. First I transpose the input, exchanging the rows and columns. Then I iterate over each column and parse each triplet as a triangle. From here it's exactly the same as part 1.