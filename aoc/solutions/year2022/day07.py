from anytree import AnyNode, PreOrderIter

def solve(input_text):
    input_lines = input_text.splitlines()

    root = AnyNode(id="/", dir=True, size=None)

    for line in input_lines:
        if line[0] == "$": # line is command
            cmd = line[2:]
            if cmd[:2] == "cd":
                chgdir = cmd[3:]
                if chgdir == "..":
                    cnode = cnode.parent
                elif chgdir == "/":
                    cnode = root
                else:
                    cnode = [n for n in cnode.children if n.id == chgdir][0]
            else:
                pass #ls

        else: # line is printed output
            prt_items = line.split(" ")            
            if prt_items[0] == "dir":
                AnyNode(id=prt_items[1], dir=True, parent=cnode, size=None)
            else:
                fsize = int(prt_items[0])
                AnyNode(id=prt_items[1], dir=False, parent=cnode, size=fsize)

    # recursively calculate directory sizes
    def traverse_node(node):
        if node.size is None:
            dir_size = 0
            for child in node.children:
                if child.size is None:
                    traverse_node(child)
                dir_size += child.size

            node.size = dir_size

        return node.size

    space_used = traverse_node(root)

    part1 = sum([n.size for n in PreOrderIter(root) if n.dir and n.size <= 100000])

    space_needed = space_used + 3e7 - 7e7
    part2 = min([n.size for n in PreOrderIter(root) if n.dir and n.size >= space_needed])

    return (part1, part2)