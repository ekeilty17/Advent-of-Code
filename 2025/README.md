# Advent of Code 2025

This is my [Advent of Code 2025](https://adventofcode.com/2025) repository. I will push all of my code to here, and I might even include `README.md` files with explanations if I feel inclined.

## How to Run

```
pip install -r requirements.txt
```

I try my best not to use outside packages, but I use numpy for all of the grid-style problems. Also, this year required an integer programming solver, which I did not feel like implementing by hand.

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

## Structure of Code

Each `Day_XX` has its own folder. Additionally, in there is `utils/` which contains some helper code used thoughout.

### Day_XX

Each `Day_XX` folder generally has the following files, although there is some variation
- `const.py` - configuration constants
- `example_input.txt` - example input
- `input.txt` - challenge input
- `load_input.py` - converts the `.txt` input files into appropriate python objects
- `part_1.py` - solution to part 1
- `part_2.py` - solution to part 2
- `README.md` - explanation of solutions

## Solution Checklist
- [x] [Day 1](https://adventofcode.com/2025/day/1)
- [x] [Day 2](https://adventofcode.com/2025/day/2)
- [x] [Day 3](https://adventofcode.com/2025/day/3)
- [x] [Day 4](https://adventofcode.com/2025/day/4)
- [x] [Day 5](https://adventofcode.com/2025/day/5)
- [x] [Day 6](https://adventofcode.com/2025/day/6)
- [x] [Day 7](https://adventofcode.com/2025/day/7)
- [x] [Day 8](https://adventofcode.com/2025/day/8)
- [x] [Day 9](https://adventofcode.com/2025/day/9)
- [x] [Day 10](https://adventofcode.com/2025/day/10)
- [x] [Day 11](https://adventofcode.com/2025/day/11)
- [x] [Day 12](https://adventofcode.com/2025/day/12)