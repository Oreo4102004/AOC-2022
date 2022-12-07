import re
from copy import deepcopy
from parse import parse

def solve():
    with open(filename) as f:
        d = f.read().split('\n\n')
        stacks = {i:[] for i in range(1,10)}
        p = 0
        for i in d[0].split('\n'):
            for l in re.findall(r"[A-Z]+",i):
                p = i.index(l,p+1)
                stacks[(p+3)//4].insert(0,l)
            p = 0
        stacks2 = deepcopy(stacks)
        for o in d[1].split('\n'):
            s = parse("move {:d} from {:d} to {:d}",o)
            t = []
            t1 = []
            for i in range(s[0]):
                t.append(stacks[s[1]].pop())
                t1.append(stacks2[s[1]].pop())
            stacks[s[2]].extend(t)
            stacks2[s[2]].extend(list(reversed(t1)))
        return f'P1 : {"".join(i.pop() for i in stacks.values())}\nP2 : {"".join(i.pop() for i in stacks2.values())}'