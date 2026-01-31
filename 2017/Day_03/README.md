# Day XX: ??

[Problem Link](https://adventofcode.com/2017/day/XX)

## Part 1

### Brute Force

In the brute force solution, I construct the spiral explicitly, using a combination of `np.column_stack()` and `np.vstack()`. Then I local the index with the value `1` and the target value `N` and find the Manhattan distance between them.

### Efficient Solution

However, we can solve this much more efficiently. If we print our more of the spiral

```
37 36 35 34 33  32  31
38 17 16 15 14  13  30
39 18  5  4  3  12  29
40 19  6 (1) 2  11  28
41 20  7  8 (9) 10  27
42 21 22 23 24 (25) 26
43 44 45 46 47  48 (49)
```

you'll notice that the bottom right diagonal are the squares of the odd numbers: $1, 9, 25, 49, \ldots$. Generally, we can express this as the formula $(2k+1)^2$ where $k$ is the **spiral layer**.

Suppose we are given a target number `N` and we want to determine what spiral layer it is in. The bottom right corner upper bounds all numbers in the spiral, therefore

$$
N \leq (2k+1)^2 \quad\implies\quad k = \left \lceil \frac{\sqrt{N}-1}{2} \right \rceil
$$

This value of $k$ gives us half of the Manhattan distance. As an example, suppose the target number is `30`. In this case, $k = 3$. Since `30` is in the rightmost row, its horizontal displacement is also $3$. Now we just have to find its vertical displacement. 

There might be better ways to do this. My method was to figure out the **bounding corners**. For `30`, these corners are `(25, 31)`. Now I can find the middle of this range - `28`. And the vertical displacement from `1` is the same as the vertical displacement from `28`, i.e. `2`. Therefore, the total Manhattan distance of `30` is `3 + 2 = 5`.

This algorithm involves only simple mathematical operations, so it is effectively $O(1)$.

## Part 2 

I believe brute force is required on this problem. My solution is best illustrated with an example. Suppose we have the following spiral

```
 5  4  2
10  1  1
11 23 25 ??
```

with `??` indicating the next value. First I pad a line of `0`'s in the last column

```
 5  4  2  0
10  1  1  0
11 23 25  0
```

Then I iterate one at a time, summing all of the values of the neighbors. By padding `0`'s, I don't need to deal with any edge cases. I can just sum all neighbors.

```
 5  4  2 57
10  1  1 54
11 23 25 26
```

Then, I rotate the array by 90-degrees so that the top becomes the right

```
11 10  5
23  1  4
25  1  2
26 54 57
```

Now, I can recurse and following exactly the same logic to append values on the right side. 

I continue this process and just check at every step if I hit a number greater than the puzzle input.