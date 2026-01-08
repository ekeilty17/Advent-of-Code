# Day 20: Infinite Elves and Infinite Houses

[Problem Link](https://adventofcode.com/2015/day/20)

## Part 1

This problem essentially down summing all of the factors of each number. To do this efficiently for a large group of numbers, I implement a version of the [Sieve of Eratosthenes](https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes). The key idea is to iterate over the factors, rather than iterating over the target numbers and finding factors 1 by 1.

I'm sure there is a faster algorithm that what I have written. I may circle back to this.

## Part 2 

Very similar to part 1, just some small changes.