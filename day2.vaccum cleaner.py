from collections import deque

grid = [
    [0,1,0,0,1],
    [1,0,0,1,0],
    [0,0,'V',0,0],
    [0,1,0,1,1],
    [0,0,1,0,0]
]

rows, cols = len(grid), len(grid[0])

def print_grid():
    for row in grid: print(row)
    print()

def find_v():
    for r in range(rows):
        for c in range(cols):
            if grid[r][c]=='V': return r,c

def bfs(s,t):
    r0,c0=s; r1,c1=t
    vis=set(); q=deque([((r0,c0),[])])
    while q:
        (r,c),p=q.popleft()
        if (r,c)==(r1,c1): return p+[(r,c)]
        for dr,dc in [(1,0),(-1,0),(0,1),(0,-1)]:
            nr,nc=r+dr,c+dc
            if 0<=nr<rows and 0<=nc<cols and (nr,nc) not in vis:
                vis.add((nr,nc)); q.append(((nr,nc),p+[(r,c)]))

def dirt():
    d=[]
    for r in range(rows):
        for c in range(cols):
            if grid[r][c]==1: d.append((r,c))
    return d

def run():
    m=0
