# Day 14: One-Time Pad

[Problem Link](https://adventofcode.com/2016/day/14)

## Part 1

This is a problem about efficient brute-forcing and avoiding repetitive computation. Let's assume that I have a working `is_key(h, next_n_hashes)` function which returns `True` if `h` is a valid key. The naive algorithm is the following

1. `num_valid_keys = 0`
2. `index = 0`
3. **while** `num_valid_keys < 64`
    1. `h = hash(index, salt)`
    2. `next_1000_hashes = [hash(index+k, salt) for k in range(1000)]`
    3. **if** `is_key(h, next_1000_hashes)`, **then** `num_valid_keys += 1`
    4. `index += 1`

However, this code is very very slow because we have to compute 1000 hashes at every iteration. Instead, we can precompute and store these beforehand. Then in each iteration, we just have to append the next hash in the sequence.

1. `hash_sequence = [hash(index+k, salt) for k in range(1000)]`
1. `num_valid_keys = 0`
2. `index = 0`
3. **while** `num_valid_keys < 64`
    1. `h = hash_sequence[index]`
    2. `next_1000_hashes = hash_sequence[index+1:index+1+1000]`
    3. **if** `is_key(h, next_1000_hashes)`, **then** `num_valid_keys += 1`
    4. `index += 1`
    5. `hash_sequence.append( hash(len(hash_sequence), salt) )`

Now, we only compute exactly as many hashes as we need to. So the bottleneck of the code becomes the `is_key()` function.

Implemented naively, `is_key()` is medium slow. But again, notice that there is lots of repeated computation going on. For example, at `index = 0` you have to find all of the quintuplets between hashes `[1, 1001]`. Then at `index = 1`, you have to find all of the quintuplets between hashes `[2, 1002]`. So hashes `[2, 1001]` all did unnecessary repeated computation.

Therefore, I wrote a `preprocess_hash()` function which computes the first triplet and all quintuplets found in each hash. Now when we call `is_key()`, we are just doing a series of set lookups.

## Part 2 

Part 2 is essentially the same, except the `hash()` function is different (and takes a lot longer). However, since we've written part 1 so efficiently, we are not wasting any unnecessary computations. Every hash is computed exactly once and stored for later use.