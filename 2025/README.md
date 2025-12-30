# Advent of Code 2025

This is my [Advent of Code 2025](https://adventofcode.com/2025) repository. I will push all of my code to here, and I might even include `README.md` files with explanations if I feel inclined.

## How to Run

```
pip install -r requirements.txt
```

I try my best not to use outside packages, but I didn't feel like implementing integer programming, for example.

All code is designed to be run at root of each year. In this case, inside the top level of `2025/`. Each day has `part_1.py` and `part_2.py`. For example,

```
cd 2025/
python -m Day_01.part_1
```

and more generally

```
python -m Day_XX.part_Y
```

where `XX` is the the two digit day number (e.g. use `01` instead of `1`) and `Y` is the part number.

## Structure of Day_X Code

Each `Day_X` folder has the following files
- `const.py` - configuration constants
- `example_input.txt` - example input
- `input.txt` - challenge input
- `load_input.py` - converts the `.txt` input files into appropriate python objects
- `part_1.py` - solution to part 1
- `part_2.py` - solution to part 2
- `README.md` - explanation of solutions

Additionally, in there is `utils/test.py` which is used to test the example input.

## Solution Checklist
- [x] Day 1
- [x] Day 2
- [x] Day 3
- [x] Day 4
- [x] Day 5
- [x] Day 6
- [x] Day 7
- [x] Day 8
- [x] Day 9
- [x] Day 10
- [x] Day 11
- [ ] Day 12