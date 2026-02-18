# Day 3: No Matter How You Slice It

[Problem Link](https://adventofcode.com/2018/day/3)

## Part 1

I compute a dictionary `claims_by_square` which maps each position to the claims which cover it. The solution to part 1 is now just the number of positions in this dictionary which map to more than 1 claim.

## Part 2 

Again I compute `claims_by_square` in the same way as part 1. Now I need to figure out which of the claims does not overlap with anything. It's actually easy to compute the opposite, i.e. which claims do overlap with some other claim. I can do this by iterating over the `claims_by_square` dictionary, and checking for squares with `> 1` claim ID. This is the purpose of this code block

```python
is_overlapping_by_claim_id = {claim_id: False for claim_id, _, _ in claims}
for claim_ids in claims_by_square.values():
    if len(claim_ids) > 1:
        for claim_id in claim_ids:
            is_overlapping_by_claim_id[claim_id] = True
```

Now, the solution is to return the claim ID which is `False` in `is_overlapping_by_claim_id`.