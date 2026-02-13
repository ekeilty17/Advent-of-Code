# Day 25: The Halting Problem

[Problem Link](https://adventofcode.com/2017/day/25)

## Part 1

A nice problem to end Advent of Code 2017. Here we are just simulating a Turing Machine. The hardest part of the problem is just extracting the relevant data from the text-heavy input. After that, we just simulate the Turing Machine as the problem describes.

Maybe one interesting choice to talk about is my implementation of the **ticker tape**. I used a dictionary instead of a list as I don't know in advance how much memory I will need to allocate, and the ticker tape extends in both directions. 