from aoc.solutions.year2022.day12 import solve

def unit_test():
    input_text = """Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi
"""

    solution = solve(input_text)
    expected_solution = (31, 29)

    assert solution == expected_solution