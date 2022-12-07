import numpy as np
from anytree import AnyNode, PreOrderIter

def solve(input_text):
    input_lines = input_text.split("\n")[:-1]
    cmd_input_flag = np.array([line.startswith("$") for line in input_lines])
    cmd_splits_ind = (cmd_input_flag[:-1] != cmd_input_flag[1:])
    cmd_split = np.split(input_lines, np.argwhere(cmd_splits_ind).flatten() + 1)
    cmd = np.array(cmd_split, dtype="object").reshape(-1, 2)

    root = AnyNode(id="/", dir=True, size=-1)

    for i in range(len(cmd)):
        nav_instrs = cmd[i, 0]
        prt_outputs = cmd[i, 1]

        for nav in nav_instrs:
            nav = nav[2:]
            if nav[:2] == "cd":
                chgdir = nav[3:]
                if chgdir == "..":
                    cnode = cnode.parent
                elif chgdir == "/":
                    cnode = root
                else:
                    cnode = [n for n in cnode.children if n.id == chgdir][0]
            else:
                pass #ls

        
        for prt in prt_outputs:
            prt_items = prt.split(" ")
            
            if prt_items[0] == "dir":
                dname = prt_items[1]
                _ = AnyNode(id=dname, dir=True, parent=cnode, size=-1)
            else:
                fname = prt_items[1]
                try:
                    fsize = int(prt_items[0])
                except:
                    print(prt)
                _ = AnyNode(id=fname, dir=False, parent=cnode, size=fsize)

    def traverse_node(n):
        if n.size == -1:
            sz = 0
            for ch in n.children:
                if ch.size == -1:
                    traverse_node(ch)

                sz += ch.size

            n.size = sz

        return n.size

    space_used = traverse_node(root)

    part1 = sum([n.size for n in PreOrderIter(root) if n.dir and n.size <= 100000])

    space_needed = space_used + 3e7 - 7e7
    part2 = min([n.size for n in PreOrderIter(root) if n.dir and n.size >= space_needed])

    return (part1, part2)