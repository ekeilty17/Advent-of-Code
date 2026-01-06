# Day 8: Matchsticks

[Problem Link](https://adventofcode.com/2015/day/8)

## Part 1

This is very much a language-specific problem with nuances in each. Python of course has lots of built-in libraries to do these types of things for you. 

In Python, `.encode()`, converts the string into bytes (UTF-8 by default). Then `.decode("unicode-escape")` converts it back into a string while also interpreting _escaped sequences_, e.g. `\"` and `\x27`.

Last thing of note is I use `string[1:-1]` to get rid of the first and last quote.

## Part 2

Part 2 is essentially doing the opposite of part 1. There are no ASCII characters in our strings, so all we have to do is correctly escape `"` and `\` characters in the string. 

I do this using the `.replace()` function.
```python
def escape(string: str) -> str:
    return '"' + string.replace('\\', '\\\\').replace('"', '\\"') + '"'
```

If you want to use built-in Python functionality, you can also use `json.dumps()`.
```python
def escape_using_json(string: str) -> str:
    return json.dumps(string)
```