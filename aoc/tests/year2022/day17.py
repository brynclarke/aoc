from aoc.solutions.year2022.day17 import solve

def unit_test():
    input_text = ">>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>"

    solution = solve(input_text)
    expected_solution = (3068, 1514285714288)

    assert solution == expected_solution