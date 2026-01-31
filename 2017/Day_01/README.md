# Day 1: Inverse Captcha

[Problem Link](https://adventofcode.com/2017/day/1)

## Part 1

The solution is to just understand and implement the question. Let `N` be the length of the captcha string.  For each index `i`, compare `captcha[i]` and `captcha[(i+1) % N]` and sum `captcha[i]` if they are equal. The `% N` is so that the last index can loop back around and compare to the first index.

## Part 2 

Let `N` be the length of the captcha string. Part 2 is almost exactly the same as part 1, except we compare `captcha[i]` to `captcha[(i + (N//2)) % N]`. As the problem describes, this is the index half way around the loop