# Day 9: Disk Fragmenter

[Problem Link](https://adventofcode.com/2024/day/9)

## Data Loading

Part 1 and part 2 required different data structures. Let's use the input `12345` as an example. To answer part 1, I converted this to the expanded **disk map**.

```
disk_map = [0, None, None, 1, 1, 1, None, None, None, None, 2, 2, 2, 2, 2]
```

This is just the Python primitive representation of the string representation `0..111....22222` shown in the problem statement.

To answer part 2 efficiently, I needed an easy way to reference the contiguous file blocks and the contiguous free spaces. In this example, the file blocks are represented as 

```
file_blocks = [(0, 1), (3, 6), (10, 15)]
```

where index `0` is `(0, 1)` meaning that the file ID `0` takes up block `0`. Likewise, index `1` is `(3, 6)` meaning that the file ID `1` takes up contiguous blocks `3, 4, 5`.

Free space blocks are represented similarly

```
free_spaces = [(1, 3), (6, 10)]
```

This means that indexes `1, 2` and `6, 7, 8, 9` are contiguous blocks of free space.

## Part 1

This problem asks us to fill all of the empty free spaces with file blocks in reverse order, such that the end result is a single contiguous block of files.

The algorithm works as follows. 
1. Let `D` be the disk map
2. **Initialize** pointer `l = 0`
3. **Initialize** pointer `r = D.length-1`
4. **While** `l <= r`
    1. **If** `D[r]` is a free space, **then** decrement `r`
    2. **Else if** `D[l]` is a file, **then** increment `l`
    3. **Otherwise** swap `D[l]` and `D[r]`
5. **Return** checksum `D`

Let's see an example of this algorithm on `0..111....22222`

```
0..111....22222     <-- initial positions
l             r

0..111....22222     <-- l is a file, increment
 l            r

02.111....2222.     <-- swap
 l            r

02.111....2222.     <-- r is a free space, decrement
 l           r

02.111....2222.     <-- l is a file, increment
  l          r

022111....222..     <-- swap
  l          r

etc...
```

Why does this algorithm work? The pointers `l` and `r` cut the disk map into 3 sections.
```
[ contiguous file blocks | unprocessed | contiguous free space ]
                         l             r
```

Therefore, once `l == r`, the disk map will become
```
[ contiguous file blocks | contiguous free space ]
                       l == r
```

which is the desired state.

## Part 2 

Part 2 is a little bit more complicated. A really important line of the problem statement is the following.

> Attempt to move each file **exactly once**...

A rare moment of our lives becoming slightly easier. My solution essentially implements the method you would use to do this manually.
1. Let `D` be the disk map
2. **For each** contiguous set of file blocks in reverse order
    1. Search for the leftmost span of free space blocks that could fit the file
    2. **If** one is found, **then** update `D` accordingly
    3. **Otherwise** continue to next file

This is done efficiently by using file block and free space lists computed by the data loader. In step 2.ii. in additional to updating `D` there is an extra step up updating the free space list. Refer to the code for the gory details.
