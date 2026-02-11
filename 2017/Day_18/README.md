# Day 18: Duet

[Problem Link](https://adventofcode.com/2017/day/18)

## Part 1

Part 1 is a typical assembly simulation that we've seen many times in Advent of Code. Just compile the instructions as written. This is implemented in `compile()` in `part_1.py`.

I also decompiled the assembly in `part_1_disassembled.py`. Although it didn't really simplify into anything, and it's only marginally faster.

## Part 2 

In part 2, we are essentially simulating threading between two simultaneous programs. To do this, I updated the `compile()` function to take in the entire program state, e.g. the registers, both program outputs, and the program counter. Then if we ever hit `snd` or `rcv` instructions, the program pauses and context-switches to the other program.

Furthermore, the function `compile()` now return as a boolean, which indicates if the program has halted. The program can halt either because it ran out of instructions or because it hit a `rcv` and is waiting.The entire system terminates if both programs have halted.

To count the number of times a program adds to their output, we need to count the number of times we see the `snd` instruction. I can actually compute this indirectly using this `haulted` flag. A program returns without halting only one a `snd` instruction.