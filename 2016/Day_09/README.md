# Day 9: Explosives in Cyberspace

[Problem Link](https://adventofcode.com/2016/day/9)

## Part 1

There is a nice way to solve this with recursion. Let's use `X(8x2)(3x3)ABCY` as an example. There are 2 case. One a regular character, we just increment by `1` and recurse on the remaining string, i.e.

```python
decompress("X(8x2)(3x3)ABCY") = 1 + decompress("(8x2)(3x3)ABCY")
```

The second case is if we hit a marker. Let `encapsulation` be the length the marker applies to, and `repeat` be the number of times it needs to repeat. Then we increment by `encapsulation * repeat` and skip to the character after that encapsulation length, i.e.

```python
decompress("(8x2)(3x3)ABCY") = 8 * 2 + decompress("Y")
```

Putting it all together

```python
decompress("X(8x2)(3x3)ABCY")
1 + decompress("(8x2)(3x3)ABCY")
1 + 8 * 2 + decompress("Y")
1 + 8 * 2 + 1
18
```

## Part 2 

My solution only works due to cooperative input. For example, a case such as this never happens

```
(8x3)ABC(3x2)DEFG
```

Here, the marker `(8x3)` overlaps `(3x2)`, but it does not overlap `DEF`. This means to decompress this string, we would have to do

```
(8x3)ABC(3x2)DEFG
ABC(3x2)ABC(3x2)ABC(3x2)DEFG
ABCABCABCABCABCDEFDEFG
```

This case never happens in the given input, and my method would not handle this case correctly. In the input, if a marker encapsulates another marker, then it also encapsulates what that submarker encapulates. For example, my counter example would have to be `(11x3)ABC(3x2)DEFG`.

This property makes recursion very easy. It's probably easiest to see via the example `(11x3)ABC(3x2)DEFG`.

```python
decompress("(11x3)ABC(3x2)DEFG")
3 * decompress("ABC(3x2)DEF") + decompress("G")
3 * (decompress("ABC") + decompress("(3x2)DEF")) + decompress("G")
3 * (decompress("ABC") + 2 * decompress("DEF")) + decompress("G")
3 * (3 + 2 * 3) + 1
28
```