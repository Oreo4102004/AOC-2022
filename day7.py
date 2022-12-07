from parse import parse


class node:
    def __init__(self,c,p):
        self.curr = c
        self.parent = p
        self.v = {}
        self.sum = 0
    @property
    def total(self):
        return self.sum + sum(i.total for i in self.v.values() if isinstance(i,node)) 

def solve():
    with open(filename) as f:
        d = f.read().split('$')
        d = [i.strip() for i in d if i]
        entry = node('/',None)
        n = entry
        # tree = {'/':[]}
        for l in d:
            if l.startswith('cd'):
                match i:=(parse('cd {}',l)[0]):
                    case '/':
                        n = entry
                    case '..':
                        n = n.parent
                    case _:
                        if i not in n.v:
                            n.v[i] = node(i,n)
                        n = n.v[i]
                continue
            for j in l.split('\n')[1:]:
                if j.startswith('dir'):
                    f = parse('dir {}',j)[0]
                    if f not in n.v:
                        n.v[f] = node(j,n)
                    continue
                size,name = j.split()
                size = int(size)
                if size not in n.v:
                    n.v[size] = name
                n.sum += size
    return entry
                   
res = []               
t = []
def recur(n,flag = None):
    if flag:
        if n.total <= 100000:
            t.append(n.total)
    else:
        t.append(n.total)
    for i in n.v.values():
        if isinstance(i,node):
            recur(i,flag)

recur(e:=solve(),flag = 100000)
res.append(sum(t))
recur(solve())
free = e.total - 40000000
res.append(min(i for i in t if i >= free))
print(f"P1 : {res[0]}\nP2 : {res[1]}")
