# Day 3: Mull It Over

[Problem Link](https://adventofcode.com/2024/day/03)

## Part 1

This is a simple application of [regex](https://en.wikipedia.org/wiki/Regular_expression). I used the pattern `mul\((\d+),(\d+)\)`. When applied to the example input, this gives
```
[('2',  '4') 
 ('5',  '5') 
 ('11', '8') 
 ('8',  '5')]
```

which are example the numbers that I need to multiply and then sum.

## Part 2 

Part 2 is similar, just a slightly more complex regex pattern and subsequent parsing. I used the pattern `(do\(\))|(don't\(\))|(mul\((\d+),(\d+)\))`. When applied to the example input, this gives
```
[('',     '',        'mul(2,4)',  '2',  '4')
 ('',     "don't()", '',          '',   '')
 ('',     '',        'mul(5,5)',  '5',  '5')
 ('',     '',        'mul(11,8)', '11', '8')
 ('do()', '',        '',          '',   '')
 ('',     '',        'mul(8,5)',  '8',  '5')]
```
So now I can iterate through this sequence of matches. Every time the first element in the tuple is populated, I switch the `enabled` flag to `True`. Every time the second element in the tuple is populatd, I switch the `enabled` flag to `False`. Otherwise, I parse the second to last and last elements to obtain the numbers that I need to multiply and then sum.

One thing to note that wasn't immediately clear to me is that the `enabled` flag persists across reports. It does not get reset at the beginning of each report.
