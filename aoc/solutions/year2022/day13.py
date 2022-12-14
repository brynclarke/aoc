def solve(input_text):
    import sys
    from itertools import zip_longest
    from functools import cmp_to_key

    def compare(lhs, rhs):
        if isinstance(lhs, list) and isinstance(rhs, list): # both values are lists
            for lhs_item, rhs_item in zip_longest(lhs, rhs):
                if lhs_item is None and rhs_item is None: # both list ran out of items
                    continue # continue checking
                elif lhs_item is None: # left list ran out of items first
                    return -1 # in the right order
                elif rhs_item is None: # right list ran out of items first
                    return 1 # not in the right order
                else: # values in both lists, compare current values
                    item_compare = compare(lhs_item, rhs_item)
                    if item_compare != 0:
                        return item_compare

        elif not(isinstance(lhs, list) or isinstance(rhs, list)): # both values are integers
            if lhs < rhs: # left integer is lower than the right integer
                return -1 # in the right order
            elif lhs > rhs: # left integer is higher than the right integer
                return 1 # not in the right order
            else: # inputs are the same integer
                pass # continue checking the next part of the input

        else: # exactly one value is an integer
            if isinstance(lhs, list): # right value is integer
                return compare(lhs, [rhs])
            if isinstance(rhs, list): # left value is integer
                return compare([lhs], rhs)
        
        return 0

    # convert input text into list of tuples (pairs)
    pairs = [tuple(eval(item) for item in pair.split("\n")) for pair in input_text.strip().split("\n\n")]

    # part 1 = sum of indices (1-indexed) of pairs in right order
    part1 = sum([idx + 1 for idx, pair in enumerate(pairs) if compare(*pair) == -1])

    # flatten list of tuples, append divider keys, and sort using custom comparator
    pairs_w_dividers = sorted(list(sum(pairs, ())) + [[[2]]] + [[[6]]], key=cmp_to_key(compare))

    # part 2 = product of indices (1-indexed) of divider keys (after sorting)
    part2 = (pairs_w_dividers.index([[2]]) + 1) * (pairs_w_dividers.index([[6]]) + 1)

    return (part1, part2)
                