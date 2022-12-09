class vec:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    @property
    def pos(self):
        return self.x,self.y
    def __add__(self,other):
        return vec(self.x+other.x,self.y+other.y)
    def __sub__(self,other):
        return vec(other.x-self.x,other.y-self.y)
    def dist(self,other):
        r = self - other
        return int((r.x**2 + r.y**2)**0.5)
    def follow(self,other):
        r = self - other
        e = vec(r.x//abs(r.x) if r.x else 0,r.y//abs(r.y) if r.y else 0)
        return e
        
p = [vec(0,0)] + [vec(0,0) for i in range(9)]



def recur(f,n=1):
    if p[n].dist(f) >= 2:
        p[n] += p[n].follow(f)
    if n == 9:
        return
    return recur(p[n],n+1)

step = {'R' : vec(1,0),'U':vec(0,1),'L':vec(-1,0),'D':vec(0,-1)}

def solve():
    global p
    with open(filename) as f:
        d = f.read().split('\n')
    grid = dic()
    def move(n):
        nonlocal grid
        grid = dic()
        grid[0,0] = '#'
        for i in d:
            direc,c = parse('{} {:d}',i)
            for j in range(c):
                s = step[direc]
                p[0] += s
                recur(p[0])
                grid[p[n].x,p[n].y] = '#'
    move(1)    
    p1 = sum(1 for i in grid.values() if i == '#')
    p = [vec(0,0)] + [vec(0,0) for i in range(9)]
    move(9)
    p2 = sum(1 for i in grid.values() if i == '#')
    return p1,p2
print(solve())