# Day 2: Gift Shop

[Problem Link](https://adventofcode.com/2025/day/2)

## Part 1

Not much to say here. Just brute force iterating over every produce ID in the given product ID ranges, and checking if the first half of the string matches the second half of the string.

## Part 2

### Brute Force

Brute forcing is medium speed, it's not instant but not very fast either. This entails iterating through every substring and checking if the full string is equal to its repetition. For example

```
123123123123
    -> (1)23123123123 != (1)11111111111
    -> (12)3123123123 != (12)1212121212
    -> (123)123123123 == (123)123123123
```

This is obviously not very efficient. This is implemented in `part_2_slow.py`.

### String Doubling Trick

I couldn't find a name for this algorithm apart from the **string doubling trick**. The algorithm is very elegant.

```python
def is_repeated_substring(s):
    return s in (s + s)[1:-1]
```

Why does this work? Let's prove it. 

Let `|` be the _concatenate_ operation. Let `X = X[0:n-1]` be some substring of length `n`. Let `s` be the string `X` repeated `m > 1` times, i.e. `s = X | ... | X = X^m`. Now consider `s | s = X^n | X^n`. Then if we trim off the first and last elements we get

```
(s | s)[1:-1] = X[1:] | X^{n-1} | X^{n-1} | X[:-1]
````

And clearly `s` is contained in `X^{n-1} | X^{n-1}`.

<br/>

Now the other direction. Suppose `s = s[0:n-1]` is a non-repeating string. Assume towards a contradiction that `s` appears somewhere in `(s | s)[1:-1]`. Then, this means there exists some `k > 0` such that
```
s = s[k:n] | s[0:k]
```

Expanding both sides

```
s[0:k] | s[k:n] = s[k:2k] | s[2k:n] | s[0:k]      -->     s[0:k] = s[k:2k]
```

But then let's expand this out again

```
s[0:k] | s[k:2k] | s[2k:n] =  s[k:n] | s[2k:3k] | s[3k:n] | s[0:k]      -->     s[0:k] = s[k:2k] = s[2k:3k]
```

We can keep applying this argument to show that `s = (s[0:k])^{n//k}` and therefore `s` must contain a repeating substring. But this is a contradiction. Therefore, `s` cannot appear inside `(s | s)[1:-1]`.
