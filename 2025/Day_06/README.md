# Day 6: Trash Compactor

[Problem Link](https://adventofcode.com/2025/day/6)

## Data Loading

Loading the data is the most annoying part of this problem. Here is an example of the input

```
123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  
```

Due to part 2, the white space is extremely important. Each operation essentially defines the start of the column.

```
|123 |328 | 51 |64  |
| 45 |64  |387 |23  |
|  6 |98  |215 |314 |
|*   |+   |*   |+   |
---------------------
|-4--|-4--|-4--|-4--|
```

In this example all of the column lengths are `4`, but in the larger input the columns can be different lengths. The key to parsing is that the operation (`+` or `*`) always appears at the start of its corresponding column. By counting the spaces between the operation symbols, we can determine the number of characters in each column, and eventually parse as an array that preserves the white space.

```
[['123', '328', ' 51', '64 '], 
 [' 45', '64 ', '387', '23 '], 
 ['  6', '98 ', '215', '314'], 
 ['*  ', '+  ', '*  ', '+  ']]
```

And now we have the information we need to answer both parts.

## Part 1

This is just a parsing game. I just need the list of operations and the parallel list of integers to which the operation applies. 90% of the hard work was done by the data loader.

## Part 2

This is also just a parsing game, but more complicated. Each column of digits is isolated and expanded into 2D array.

```
['123',             [['1', '2', 3'],
 ' 45',     -->      [' ', '4', '5'],
 '  6']              [' ', ' ', '6']]
```

This 2D array is transposed, its rows joined, and finally converted into integers.

```
[['1', ' ', ' '],           ['1',            [1,
 ['2', '4', ' ']    -->      '24',    -->     24, 
 ['3', '5', '6']]            '356']           356]
```

And these are the integers to which part 2 wants us the corresponding operation. From here it is identical to part 1.
