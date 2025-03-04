N = 9  # Sudoku grid size

def print_grid(grid):
    """Prints the Sudoku grid in a readable format."""
    for row in grid:
        print(" ".join(map(str, row)))

def is_safe(grid, row, col, num):
    """Checks if placing 'num' in grid[row][col] is valid."""
    if num in grid[row]:  # Row check
        return False
    
    if num in [grid[i][col] for i in range(N)]:  # Column check
        return False

    # 3x3 subgrid check
    start_row, start_col = row - row % 3, col - col % 3
    if any(grid[i][j] == num for i in range(start_row, start_row + 3) for j in range(start_col, start_col + 3)):
        return False

    return True

def solve_sudoku(grid, row=0, col=0):
    """Solves the Sudoku puzzle using backtracking."""
    
    # Move to the next row if col reaches N
    if col == N:
        row += 1
        col = 0

    # If we reach the last row, solution is complete
    if row == N:
        return True

    # Skip already filled cells
    if grid[row][col] != 0:
        return solve_sudoku(grid, row, col + 1)

    for num in range(1, 10):  # Try numbers 1-9
        if is_safe(grid, row, col, num):
            grid[row][col] = num
            if solve_sudoku(grid, row, col + 1):
                return True
            grid[row][col] = 0  # Backtrack

    return False

def main():
    """Main function to run the Sudoku solver."""
    grid = [
        [3, 0, 6, 5, 0, 8, 4, 0, 0],
        [5, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 7, 0, 0, 0, 0, 3, 1],
        [0, 0, 3, 0, 1, 0, 0, 8, 0],
        [9, 0, 0, 8, 6, 3, 0, 0, 5],
        [0, 5, 0, 0, 9, 0, 6, 0, 0],
        [1, 3, 0, 0, 0, 0, 2, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 4],
        [0, 0, 5, 2, 0, 6, 3, 0, 0]
    ]

    if solve_sudoku(grid):
        print("Solved Sudoku Grid:")
        print_grid(grid)
    else:
        print("No solution exists.")

if __name__ == "__main__":
    main()
