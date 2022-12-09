def solve():
    with open(filename) as f:
        # t = f.read().split('\n')
        # l = len(t)
        # res = 0 
        # grid = dic(lambda : 0)
        # for i,p in enumerate(t):
        #     for i2,j in enumerate(p):
        #         grid[i,i2] = int(j)
        # for o in grid.items():
        #     if o[0][0] in (0,l-1) or o[0][1] in (0,l-1):
        #         res += 1
        #     else:
        #         a,d,w,s = max(grid[o[0][0],i] for i in range(o[0][1])),max(grid[o[0][0],i] for i in range(o[0][1]+1,l)),max(grid[i,o[0][1]] for i in range(o[0][0])),max(grid[i,o[0][1]] for i in range(o[0][0]+1,l))
        #         if any(o[1] > k for k in (a,d,w,s)):
        #             res += 1 
        t = f.read().split('\n')
        l = len(t)
        res = 0 
        grid = dic(lambda : 0)
        for i,p in enumerate(t):
            for i2,j in enumerate(p):
                grid[i,i2] = int(j)
        for o in dict(grid).items():
            if o[0][0] in (0,l-1) or o[0][1] in (0,l-1):
                continue
            ls,rs,ws,ss = 0,0,0,0
            for i in range(o[0][1]-1,-1,-1):
                if grid[o[0][0],i] < o[1]:
                    ls += 1
                else:
                    ls += 1
                    break
            for i in range(o[0][1]+1,l):
                if grid[o[0][0],i] < o[1]:
                    rs += 1
                else:
                    rs += 1
                    break
            for i in range(o[0][0]-1,-1,-1):
                if grid[i,o[0][1]] < o[1]:
                    ws += 1
                else:
                    ws += 1
                    break
            for i in range(o[0][0]+1,l):
                if grid[i,o[0][1]] < o[1]:
                    ss += 1
                else:
                    ss += 1
                    break
            if (e:=ls*rs*ws*ss) > res:
                res = e
            
        return res

