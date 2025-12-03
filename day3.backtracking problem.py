   N = 8

board = [[-1 for _ in range(N)] for _ in range(N)]

moves = [(2,1),(1,2),(-1,2),(-2,1),
         (-2,-1),(-1,-2),(1,-2),(2,-1)]

def safe(x, y):
    return 0 <= x < N and 0 <= y < N and board[x][y] == -1

def solve(x, y, move):
    if move == N * N:
        return True
    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if safe(nx, ny):
            board[nx][ny] = move
            if solve(nx, ny, move + 1):
                return True
            board[nx][ny] = -1
    return False

sx = int(input("Start X (0-7): "))
sy = int(input("Start Y (0-7): "))

board[sx][sy] = 0

if solve(sx, sy, 1):
    print("Knight's Tour Found:")
    for row in board:
        print(row)
else:
    print("No Tour Found.")

