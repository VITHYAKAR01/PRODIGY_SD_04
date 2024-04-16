def printsudoku(grid):
    for i in range(9):
        for j in range(9):
            print("\t", grid[i][j], end="")
        print()

def isvalid(grid, row, col, num):
    for c in range(9):
        if grid[row][c] == num:
            return False
    for r in range(9):
        if grid[r][col] == num:
            return False
    row -= row % 3
    col -= col % 3
    for i in range(row, row + 3):
        for j in range(col, col + 3):
            if grid[i][j] == num:
                return False
    return True

def solver(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                for n in range(1, 10):
                    if isvalid(grid, i, j, n):
                        grid[i][j] = n
                        if solver(grid):
                            return True
                        grid[i][j] = 0
                return False
    return True

if __name__ == "__main__":
    grid = [
        [9,0,0,3,0,2,6,0,0],
        [4,0,7,0,0,8,9,1,3],
        [6,0,3,1,0,0,0,5,4],
        [0,3,0,0,8,0,4,7,0],
        [0,0,8,0,3,0,1,6,0],
        [0,0,4,2,0,0,5,0,0],
        [8,7,1,9,0,6,0,4,5],
        [3,0,0,0,5,0,0,0,0],
        [2,0,0,4,0,0,0,0,1]
    ]

    print("The Given Sudoku:")
    printsudoku(grid)

    if solver(grid):
        print("\nThe Solution:")
        printsudoku(grid)
    else:
        print("\nNo solution exists.")
