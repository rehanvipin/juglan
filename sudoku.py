class Sudoku:
    def __init__(self, n):
        self.grid = [[0 for _ in range(n)] for _ in range(n)]
        self.n = n
        self.s_x = 0
        self.s_y = 0
    
    def set_grid(self, grid):
        for i in range(n):
            for j in range(n):
                self.grid[i][j] = grid[i][j]
        self.fixed = []
        for i in range(n):
            for j in range(n):
                if self.grid[i][j]:
                    self.fixed.append((i,j))
    
    def get_grid(self):
        return self.grid
    
    def isvalid(self, debug=False):
        n = self.n
        for row in self.grid:
            chk = []
            for i in row:
                if i in chk:
                    return False
                if i:
                    chk.append(i)
            if debug:
                print("row",row)
        
        transpose = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                transpose[i][j] = self.grid[j][i]

        for row in transpose:
            chk = []
            for i in row:
                if i in chk:
                    return False
                if i:
                    chk.append(i)
            if debug:
                print("row",row)

        base = int(n**0.5)  # For the smaller squares
        for i in range(0, n, base):
            for j in range(0, n, base):
                square = []
                for a in range(i, i+base):
                    for b in range(j, j+base):
                        if self.grid[a][b] in square:
                            return False
                        if self.grid[a][b]:
                            square.append(self.grid[a][b])

        return True
    
    def next_cell(self, i, j):
        n = self.n
        if j+1 == n:
            if i+1 == n:
                return n, n
            else:
                return (i+1, 0)
        return (i, j+1)

    def solve(self, s_x=0, s_y=0):
        n = self.n
        if not self.isvalid():
            return False

        if (s_x, s_y) in self.fixed:
            new_x, new_y = self.next_cell(s_x, s_y)
            if (new_x < n) and (new_y < n):
                #print("Skipping",s_x, s_y)
                return self.solve( new_x, new_y)
            else:
                return True

        for i in range(1,n+1):
            # print("Trying out", i, "for", s_x, s_y)
            self.grid[s_x][s_y] = i
            new_x, new_y = self.next_cell(s_x, s_y)
            # print("Next of ",(s_x, s_y), "is", (new_x, new_y))
            if (new_x < n) and (new_y < n):
                if self.solve(new_x, new_y):
                    return True
            else:
                if self.isvalid():
                    return True
        
        # Failed all the guesses, retrace one step back
        self.grid[s_x][s_y] = 0
        return False

n = int(input())

grid = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    grid[i] = [int(x) for x in input().split()]

game = Sudoku(n)
game.set_grid(grid)

print("The grid")
for row in grid:
    print(*row)


if game.solve():
    print("="*(n*2-1))
    grid = game.get_grid()
    for row in grid:
        print(*row)
    # print(isvalid(grid, n, True))
else:
    print("Cannot solve the sudoku grid")
    grid = game.get_grid()
    for row in grid:
        print(*row)
    
