import tkinter as tk
from tkinter import messagebox
import random

N = 9  # Grid size

class SudokuGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku Game")
        self.grid = [[0] * N for _ in range(N)]
        self.entries = [[None] * N for _ in range(N)]
        self.create_widgets()
        self.generate_puzzle()

    def create_widgets(self):
        """Creates the Sudoku board with entry fields."""
        frame = tk.Frame(self.root)
        frame.pack()
        
        for row in range(N):
            for col in range(N):
                entry = tk.Entry(frame, width=3, font=("Arial", 18), justify="center")
                entry.grid(row=row, column=col, padx=2, pady=2)
                self.entries[row][col] = entry
                
        button_frame = tk.Frame(self.root)
        button_frame.pack()
        
        tk.Button(button_frame, text="Check", command=self.check_solution).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Hint", command=self.give_hint).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Solve", command=self.solve_and_display).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="New Game", command=self.generate_puzzle).pack(side=tk.LEFT, padx=5)
    
    def generate_puzzle(self):
        """Generates a random Sudoku puzzle."""
        self.grid = [[0] * N for _ in range(N)]
        self.solve_sudoku()  # Generate a solved board
        self.remove_numbers()  # Create the puzzle
        self.fill_board()
    
    def remove_numbers(self):
        """Removes numbers to create a playable puzzle."""
        attempts = 30  # Number of removals
        while attempts > 0:
            row, col = random.randint(0, 8), random.randint(0, 8)
            while self.grid[row][col] == 0:
                row, col = random.randint(0, 8), random.randint(0, 8)
            self.grid[row][col] = 0
            attempts -= 1
    
    def fill_board(self):
        """Fills the GUI board with the generated puzzle."""
        for row in range(N):
            for col in range(N):
                self.entries[row][col].delete(0, tk.END)
                if self.grid[row][col] != 0:
                    self.entries[row][col].insert(0, str(self.grid[row][col]))
                    self.entries[row][col].config(state=tk.DISABLED)
                else:
                    self.entries[row][col].config(state=tk.NORMAL)
    
    def is_safe(self, row, col, num):
        """Checks if a number can be placed in a cell."""
        if num in self.grid[row]:
            return False
        if num in [self.grid[i][col] for i in range(N)]:
            return False
        start_row, start_col = row - row % 3, col - col % 3
        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                if self.grid[i][j] == num:
                    return False
        return True
    
    def solve_sudoku(self, row=0, col=0):
        """Solves the Sudoku using backtracking."""
        if col == N:
            row += 1
            col = 0
        if row == N:
            return True
        if self.grid[row][col] != 0:
            return self.solve_sudoku(row, col + 1)
        
        for num in range(1, 10):
            if self.is_safe(row, col, num):
                self.grid[row][col] = num
                if self.solve_sudoku(row, col + 1):
                    return True
                self.grid[row][col] = 0
        return False
    
    def solve_and_display(self):
        """Solves the Sudoku and displays the solution."""
        if self.solve_sudoku():
            self.fill_board()
        else:
            messagebox.showerror("Error", "No solution exists!")
    
    def check_solution(self):
        """Checks if the user's solution is correct."""
        for row in range(N):
            for col in range(N):
                value = self.entries[row][col].get()
                if not value.isdigit() or int(value) != self.grid[row][col]:
                    messagebox.showerror("Incorrect", "Some numbers are incorrect!")
                    return
        messagebox.showinfo("Success", "Congratulations! You solved it correctly!")
    
    def give_hint(self):
        """Provides a hint by filling in one empty cell."""
        for row in range(N):
            for col in range(N):
                if self.entries[row][col].get() == "":
                    self.entries[row][col].insert(0, str(self.grid[row][col]))
                    return
        messagebox.showinfo("Hint", "No hints available!")

if __name__ == "__main__":
    root = tk.Tk()
    game = SudokuGame(root)
    root.mainloop()
