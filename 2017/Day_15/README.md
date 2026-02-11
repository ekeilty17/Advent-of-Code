# Day 15: Dueling Generators

[Problem Link](https://adventofcode.com/2017/day/15)

## Part 1 and Part 2

I just brute forced the problem today, essentially just coding the problem exactly as described. So there is not much to discuss.

I don't like that my code takes seconds to run, but I don't see a way around this. I was hoping there would be a cute trick like maybe generator `A` or `B` cycle at some point and you could be clever about caching that information. But since `modulus` is about 2 billion and `N` is 40 million, this just doesn't happen (at least not in part 1).