# Day 8: Two-Factor Authentication

[Problem Link](https://adventofcode.com/2016/day/8)

## Load Input

I stored the instructions as objects. For example

```python
"rect 3x2" ==               {'type': 'rect',            'shape': (3, 2)}
"rotate column x=1 by 2" == {'type': 'rotate column',   'index': 1, 'shift': 2}
"rotate row y=0 by 4" ==    {'type': 'rotate row',      'index': 0, 'shift': 4}
```

## Part 1

I utilized [numpy](https://numpy.org/) for all of the grid operations rather than implementing by hand. From here it's just a matter of implementing the instructions correctly

## Part 2 

Same as part 1, except I use `utils.display_np.display_np_str()` to print out the grid.