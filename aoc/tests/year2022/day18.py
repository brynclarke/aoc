from aoc.solutions.year2022.day18 import solve

def unit_test():
    input_text = "2,2,2\n1,2,2\n3,2,2\n2,1,2\n2,3,2\n2,2,1\n2,2,3\n2,2,4\n2,2,6\n1,2,5\n3,2,5\n2,1,5\n2,3,5\n"

    solution = solve(input_text)
    expected_solution = (64, 58)

    assert solution == expected_solution