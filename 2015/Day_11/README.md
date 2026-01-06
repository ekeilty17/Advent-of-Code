# Day 11: Corporate Policy

[Problem Link](https://adventofcode.com/2015/day/11)

## Part 1

This was really just a case of coding exactly the specs of the question. First, I converted the alphabetic string password a list of integers to make it easier to work with. Effectively, the variable `numeric_password` is a base `26` number.

Then, I wrote `is_valid_password()` which just checks each of the outlined password requirements.

Then, I wrote `increment()` which increments the base `26` number by one. One additional bit of logic was if we incremeneted to one of `i`, `o`, or `l`, then we increment one more time as we know the password will be invalid otherwise.

Finally, I just brute force it by incrementing until I find a valid password.

## Part 2 

Exactly the same as part 1, just a different input