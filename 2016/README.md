# Advent of Code 2016

This is my [Advent of Code 2016](https://adventofcode.com/2016) repository. I will push all of my code to here, and I might even include `README.md` files with explanations if I feel inclined.

## How to Run

```
pip install -r requirements.txt
```

I try my best not to use outside packages, but I use numpy for all of the grid-style problems.

All code is designed to be run at root of each year. In this case, inside the top level of `2016/`. Each day has `part_1.py` and `part_2.py`. For example,

```
cd 2016/
python -m Day_01.part_1
```

and more generally

```
python -m Day_XX.part_Y
```

where `XX` is the the two digit day number (e.g. use `01` instead of `1`) and `Y` is the part number.

## Structure of Code

Each `Day_XX` has its own folder. Additionally, in there is `utils/` which contains some helper code used throughout.

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
- [x] [Day 1](https://adventofcode.com/2016/day/1)
- [x] [Day 2](https://adventofcode.com/2016/day/2)
- [x] [Day 3](https://adventofcode.com/2016/day/3)
- [x] [Day 4](https://adventofcode.com/2016/day/4)
- [x] [Day 5](https://adventofcode.com/2016/day/5)
- [x] [Day 6](https://adventofcode.com/2016/day/6)
- [x] [Day 7](https://adventofcode.com/2016/day/7)
- [x] [Day 8](https://adventofcode.com/2016/day/8)
- [x] [Day 9](https://adventofcode.com/2016/day/9)
- [x] [Day 10](https://adventofcode.com/2016/day/10)
- [ ] [Day 11](https://adventofcode.com/2016/day/11)
- [x] [Day 12](https://adventofcode.com/2016/day/12)
- [x] [Day 13](https://adventofcode.com/2016/day/13)
- [x] [Day 14](https://adventofcode.com/2016/day/14)
- [x] [Day 15](https://adventofcode.com/2016/day/15)
- [x] [Day 16](https://adventofcode.com/2016/day/16)
- [x] [Day 17](https://adventofcode.com/2016/day/17)
- [x] [Day 18](https://adventofcode.com/2016/day/18)
- [x] [Day 19](https://adventofcode.com/2016/day/19)
- [x] [Day 20](https://adventofcode.com/2016/day/20)
- [x] [Day 21](https://adventofcode.com/2016/day/21)
- [ ] [Day 22](https://adventofcode.com/2016/day/22)
- [x] [Day 23](https://adventofcode.com/2016/day/23)
- [ ] [Day 24](https://adventofcode.com/2016/day/24)
- [ ] [Day 25](https://adventofcode.com/2016/day/25)