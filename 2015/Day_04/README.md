# Day 4: The Ideal Stocking Stuffer

[Problem Link](https://adventofcode.com/2015/day/4)

## Part 1

I was lazy and just used a Python library for the MD5 hash function, rather than implementing myself. 

```python
import hashlib
def MD5(secret_key: str) -> str:
    return hashlib.md5(secret_key.encode()).hexdigest()
```

From here it's just a brute force search. I don't think you can improve on this unless you start exploiting the particulars of the MD5 hash algorithm. 

## Part 2 

Exactly the same as part 1, except with `num_leading_zeros = 6` instead of `5`.