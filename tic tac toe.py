# Tic Tac Toe Game using Tkinter
# This is a simple implementation of the Tic Tac Toe game using Python's Tkinter library.
import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")
        self.current_player = "X"
        self.board = [""] * 9

        self.status_label = tk.Label(self.window, text="Player X's turn", font=('Arial', 14))
        self.status_label.pack(pady=10)

        self.buttons = []
        self.create_board()

        self.reset_button = tk.Button(self.window, text="Restart", command=self.reset_game, font=('Arial', 12))
        self.reset_button.pack(pady=10)

        self.window.mainloop()

    def create_board(self):
        frame = tk.Frame(self.window)
        frame.pack()
        for i in range(9):
            btn = tk.Button(frame, text="", font=('Arial', 24), width=5, height=2,
                            command=lambda i=i: self.handle_click(i))
            btn.grid(row=i // 3, column=i % 3)
            self.buttons.append(btn)

    def handle_click(self, index):
        if self.board[index] == "" and self.check_winner() is None:
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player)
            winner = self.check_winner()
            if winner:
                self.status_label.config(text=f"Player {winner} wins!")
                messagebox.showinfo("Game Over", f"Player {winner} wins!")
            elif "" not in self.board:
                self.status_label.config(text="It's a draw!")
                messagebox.showinfo("Game Over", "It's a draw!")
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
                self.status_label.config(text=f"Player {self.current_player}'s turn")

    def check_winner(self):
        combos = [
            [0,1,2],[3,4,5],[6,7,8],  # rows
            [0,3,6],[1,4,7],[2,5,8],  # columns
            [0,4,8],[2,4,6]           # diagonals
        ]
        for combo in combos:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != "":
                return self.board[combo[0]]
        return None

    def reset_game(self):
        self.board = [""] * 9
        for btn in self.buttons:
            btn.config(text="")
        self.current_player = "X"
        self.status_label.config(text="Player X's turn")

if __name__ == "__main__":
    TicTacToe()

