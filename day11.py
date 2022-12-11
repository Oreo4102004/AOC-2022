class monke:
    def __init__(self,i,o,d,t,f):
        self.items = deque(map(int,i.split(',')))
        self.op = o
        self.div = d
        self.t,self.f = t,f 
        self.ins = 0
monkes = []




@cache
def is_div(n,i):
    return not n % i

def solve(num,tr):
    with open(filename) as f:
        d = f.read().split('\n\n')
        for i in d:
            l = i.split('\n')
            items = parse('  Starting items: {}',l[1])[0]
            o = parse('  Operation: new = {}',l[2])[0]
            d = parse('  Test: divisible by {:d}',l[3])[0]
            t = parse('    If true: throw to monkey {:d}',l[4])[0]
            f = parse('    If false: throw to monkey {:d}',l[5])[0]
            monkes.append(monke(items,o,d,t,f))
        sol = prod(i.div for i in  monkes)
        for _ in range(num):
            for i in monkes:
                while i.items:
                    old = i.items.popleft()
                    n = (eval(i.op)//tr)%sol
                    if is_div(n,i.div):
                        monkes[i.t].items.append(n)
                    else:
                        monkes[i.f].items.append(n)
                    i.ins += 1
        r = prod(sorted([i.ins for i in monkes])[-2:])
        monkes.clear()
        return r

print(f"P1: {solve(20,3)}\nP2: {solve(10000,1)}")
