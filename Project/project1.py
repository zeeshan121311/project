import tkinter as tk
from tkinter import messagebox
import random

class RockPaperScissorsGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock, Paper, Scissors")
        self.root.geometry("300x200")

        self.player_score = 0
        self.computer_score = 0
        self.rounds_played = 0

        self.label = tk.Label(root, text="Choose Rock, Paper, or Scissors!", font=("Arial", 12))
        self.label.pack(pady=10)

        self.rock_button = tk.Button(root, text="Rock", font=("Arial", 12), command=lambda: self.play("Rock"))
        self.rock_button.pack(pady=5)

        self.paper_button = tk.Button(root, text="Paper", font=("Arial", 12), command=lambda: self.play("Paper"))
        self.paper_button.pack(pady=5)

        self.scissors_button = tk.Button(root, text="Scissors", font=("Arial", 12), command=lambda: self.play("Scissors"))
        self.scissors_button.pack(pady=5)

        self.score_label = tk.Label(root, text=f"Player: {self.player_score}  Computer: {self.computer_score}", font=("Arial", 12))
        self.score_label.pack(pady=10)

    def play(self, player_choice):
        choices = ["Rock", "Paper", "Scissors"]
        computer_choice = random.choice(choices)

        result = self.determine_winner(player_choice, computer_choice)

        self.rounds_played += 1
        if result == "Player":
            self.player_score += 1
        elif result == "Computer":
            self.computer_score += 1

        self.score_label.config(text=f"Player: {self.player_score}  Computer: {self.computer_score}")

        if self.rounds_played == 3:
            self.end_game()
        else:
            messagebox.showinfo("Result", f"Computer chose {computer_choice}. {result} wins this round!")

    def determine_winner(self, player_choice, computer_choice):
        if player_choice == computer_choice:
            return "Tie"
        elif (player_choice == "Rock" and computer_choice == "Scissors") or \
             (player_choice == "Scissors" and computer_choice == "Paper") or \
             (player_choice == "Paper" and computer_choice == "Rock"):
            return "Player"
        else:
            return "Computer"

    def end_game(self):
        if self.player_score > self.computer_score:
            messagebox.showinfo("Game Over", "Congratulations! You won the game!")
        elif self.player_score < self.computer_score:
            messagebox.showinfo("Game Over", "Sorry! The computer won the game.")
        else:
            messagebox.showinfo("Game Over", "It's a tie!")

        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    game = RockPaperScissorsGame(root)
    root.mainloop()