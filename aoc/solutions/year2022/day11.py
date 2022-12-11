def solve(input_text):
    monkey_lines = [line.split("\n") for line in input_text[:-1].split("\n\n")]

    def get_monkey_business(part):
        n_monkeys = len(monkey_lines)
        monkey_items = [None] * n_monkeys
        monkey_ops = [[None, None]] * n_monkeys
        monkey_tests = [[None, None, None]] * n_monkeys

        for m, lines in enumerate(monkey_lines):
            items = lines[1][2:].replace("Starting items: ", "").split(", ")
            items = [int(i) for i in items]
            monkey_items[m] = items

            op = lines[2][2:].replace("Operation: new = old ", "").split(" ")
            monkey_ops[m] = [op[0], op[1]]

            div_by = int(lines[3][2:].replace("Test: divisible by ", ""))
            if_true = int(lines[4][3:].replace("If true: throw to monkey ", "")[1:])
            if_false = int(lines[5][3:].replace("If false: throw to monkey ", "")[1:])

            monkey_tests[m] = [div_by, if_true, if_false]

        prod = eval("*".join([str(t[0]) for t in monkey_tests]))

        inspected = [0] * n_monkeys

        n_rounds = 20 if part == 1 else 10000
        for round in range(n_rounds):
            for m, lines in enumerate(monkey_lines):
                items = monkey_items[m]
                ops = monkey_ops[m]
                tests = monkey_tests[m]

                for n in range(len(items)):
                    inspected[m] += 1
                    item = items.pop(0)

                    operand = item if ops[1] == "old" else int(ops[1])
                    if ops[0] == "*":
                        worry = item*operand % prod
                    elif ops[0] == "+":
                        worry = item + operand
                    else:
                        assert False
                    
                    if part == 1:
                        worry = int(worry / 3)

                    test_res = worry % tests[0] == 0
                    if test_res:
                        throw_to = tests[1]
                    else:
                        throw_to = tests[2]
                    
                    monkey_items[throw_to] = monkey_items[throw_to] + [worry]


        inspected = sorted(inspected)
        return inspected[-2] * inspected[-1]
    
    part1 = get_monkey_business(1)
    part2 = get_monkey_business(2)

    return part1, part2