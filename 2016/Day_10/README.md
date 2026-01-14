# Day 10: Balance Bots

[Problem Link](https://adventofcode.com/2016/day/10)

## Part 1

To me the hardest part of this problem was 1) understanding what the problem was asking, and 2) figuring out the best way to store the input.

The first key thing to understand is the input is not in order. The question says

> each bot only proceeds when it has two microchips, and once it does, it gives each one to a different bot or puts it in a marked "output" bin

When reading the `input.txt`, there are two cases. There are value _initializations_ of the form
```
value 5 goes to bot 2
```
and there are value _transfers_ of the form
```
bot 2 gives low to bot 1 and high to bot 0
```
The initializations can all be done up-front. The transfers only execute once a bot has 2 microchips. 

The main issue of the problem is knowing when to execute each transfer. One method of doing this would be to compute a dependency dictionary, e.g. bot `2` depends on bot `5`, etc. This would give you the exact order of the transfers. Because the input is so small I take the easier brute-force approach. I just iterate through every transfer, if the bot has 2 microchips, then I make the transfer. Otherwise, I continue to the next. I do this until every transfer has been executed.

## Part 2 

Exactly the same as part 1, just getting a different number at the end.