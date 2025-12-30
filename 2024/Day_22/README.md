# Day 22: Monkey Market

[Problem Link](https://adventofcode.com/2024/day/23)

## Part 1

The solution just requires you to carefully read the definition of copmuting the next **secret number**. After successfully writing the function `compute_next_secret_number()`, there is not much else to the question. The brute force approach works in a reasonable time.

Maybe it's possble to package these numbers up so that you can compute the entire list at once with a much faster runtime? I'm not sure. 

## Part 2 

Again, the hardest part of the question is just reading and undestanding the requirements. Aftwards, the brute-force approach works in a reasonable time.

First I pre-compute the sequence of secret numbers, and then compute the corresponding prices and price changes
```python
prices = sequences % 10
price_changes = prices[:, 1:] - prices[:, :-1]
```

Then, I iterate over each row of `price_changes`. Within each row, I iterate over each consecutive sequence of `4` price changes, which have a corresponding price
```python
consecutive_change = price_changes[i, j:j+4]
price = prices[i, j+4]
```

Now it's just a matter of proper bookkeeping based on the question requirements. You can see the implementation in `part_2.py` for those details. By the end of my double for-loop, I have a dictionary of total prices by each consecutive change.

This is a brute force approach which takes about 5 seconds. I'm sure there are some optimizations which could be made, but I have other problems to work on.