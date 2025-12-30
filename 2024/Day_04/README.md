# Day 4: Ceres Search

[Problem Link](https://adventofcode.com/2024/day/4)

## Part 1

The problem can be boiled down to iterating over rows, columns, main diagonals (top-left to bottom-right), and anti-diagonals (top-right to bottom-left). Numpy helps remove some of the tedium.

One thing to note is the implementation of `check_columns()` and `check_anti_diagonals()`

```python
def check_columns(crossword, pattern):
    return check_rows(crossword.T, pattern)
```

```python
def check_anti_diagonals(crossword, pattern):
    return check_main_diagonals(np.fliplr(crossword), pattern)
```

The former works since the transpose converts rows into columns. Likewise, the latter works because we've converted main diagonals into anti-diagonals. This helps reduce repetitive code.

## Part 2 

For fun I tried to code this fairly generically, so you could run this code to get the counts for any `m` x `n` pattern. First, given a pattern, we compute all of its unique orientations. For example, in this question the given pattern is
```
[['M' '.' 'S']
 ['.' 'A' '.']
 ['M' '.' 'S']]
```

which has the following additional orientations
```
[['S' '.' 'S']
 ['.' 'A' '.']
 ['M' '.' 'M']]

[['M' '.' 'M']
 ['.' 'A' '.']
 ['S' '.' 'S']]

[['S' '.' 'M']
 ['.' 'A' '.']
 ['S' '.' 'M']]
```

Then we just iterate over the crossword grid and increment every time any of these orientations get a match.

I am confident that you could a more efficent algorithm if you take advantage of the symmetry in this particular pattern.
