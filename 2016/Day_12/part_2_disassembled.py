from Day_12.part_1_disassembled import example_solution, solution
from utils.solve import test, solve

if __name__ == "__main__":
    registers = {"a": 0, "b": 0, "c": 1, "d": 0}
    target_register = "a"

    expected_answer = 42
    test(expected_answer, example_solution, registers, target_register)

    solve(solution, registers, target_register)