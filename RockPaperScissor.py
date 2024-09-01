import tkinter as tk
from random import choice

class RockPaperScissors:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Rock Paper Scissors")
        self.window.attributes("-fullscreen", True)  # Set window to full screen

        self.window.configure(background="#f0f0f0")  # Set background color

        self.player_score = 0
        self.computer_score = 0
        self.max_points = 0
        self.max_rounds = 0

        self.header_frame = tk.Frame(self.window, bg="#333", height=100)
        self.header_frame.pack(fill=tk.X)

        self.title_label = tk.Label(self.header_frame, text="Rock Paper Scissors", font=("Arial", 36, "bold"), bg="#333", fg="#fff")
        self.title_label.pack(pady=20)

        self.config_frame = tk.Frame(self.window, bg="#f0f0f0")
        self.config_frame.pack(fill=tk.X, pady=20)

        self.max_points_label = tk.Label(self.config_frame, text="Enter max points per round:", font=("Arial", 24), bg="#f0f0f0")
        self.max_points_label.pack(side=tk.LEFT, padx=20)

        self.max_points_entry = tk.Entry(self.config_frame, font=("Arial", 24), width=5)
        self.max_points_entry.pack(side=tk.LEFT, padx=20)

        self.max_rounds_label = tk.Label(self.config_frame, text="Enter max number of rounds:", font=("Arial", 24), bg="#f0f0f0")
        self.max_rounds_label.pack(side=tk.LEFT, padx=20)

        self.max_rounds_entry = tk.Entry(self.config_frame, font=("Arial", 24), width=5)
        self.max_rounds_entry.pack(side=tk.LEFT, padx=20)

        self.start_button = tk.Button(self.config_frame, text="Start", command=self.start_game, font=("Arial", 24), bg="#4CAF50", fg="#fff")
        self.start_button.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=10, pady=10)

        self.score_frame = tk.Frame(self.window, bg="#f0f0f0")
        self.score_frame.pack(fill=tk.X, pady=20)

        self.player_score_label = tk.Label(self.score_frame, text="Player Score: 0", font=("Arial", 24), bg="#f0f0f0")
        self.player_score_label.pack(side=tk.LEFT, padx=20)

        self.computer_score_label = tk.Label(self.score_frame, text="Computer Score: 0", font=("Arial", 24), bg="#f0f0f0")
        self.computer_score_label.pack(side=tk.RIGHT, padx=20)

        self.total_score_frame = tk.Frame(self.window, bg="#f0f0f0")
        self.total_score_frame.pack(fill=tk.X, pady=20)

        self.total_player_score_label = tk.Label(self.total_score_frame, text="Total Player Score: 0", font=("Arial", 24), bg="#f0f0f0")
        self.total_player_score_label.pack(side=tk.LEFT, padx=20)

        self.total_computer_score_label = tk.Label(self.total_score_frame, text="Total Computer Score: 0", font=("Arial", 24), bg="#f0f0f0")
        self.total_computer_score_label.pack(side=tk.RIGHT, padx=20)

        self.result_frame = tk.Frame(self.window, bg="#f0f0f0")
        self.result_frame.pack(fill=tk.X, pady=20)

        self.result_label = tk.Label(self.result_frame, text="", font=("Arial", 24), bg="#f0f0f0", wraplength=800)
        self.result_label.pack(pady=20)

        self.button_frame = tk.Frame(self.window, bg="#f0f0f0")
        self.button_frame.pack(fill=tk.X, pady=20)

        self.rock_button = tk.Button(self.button_frame, text="Rock", command=lambda: self.play("rock"), font=("Arial", 24), bg="#4CAF50", fg="#fff", state=tk.DISABLED)
        self.rock_button.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=10, pady=10)

        self.paper_button = tk.Button(self.button_frame, text="Paper", command=lambda: self.play("paper"), font=("Arial", 24), bg="#4CAF50", fg="#fff", state=tk.DISABLED)
        self.paper_button.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=10, pady=10)

        self.scissors_button = tk.Button(self.button_frame, text="Scissors", command=lambda: self.play("scissors"),
                                         font=("Arial", 24), bg="#4CAF50", fg="#fff", state=tk.DISABLED)
        self.scissors_button.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=10, pady=10)

        self.exit_button = tk.Button(self.button_frame, text="Exit", command=self.window.destroy, font=("Arial", 24),
                                     bg="#4CAF50", fg="#fff")
        self.exit_button.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=10, pady=10)

        self.total_rounds = 0
        self.total_player_score = 0
        self.total_computer_score = 0

    def start_game(self):
        self.max_points = int(self.max_points_entry.get())
        self.max_rounds = int(self.max_rounds_entry.get())
        self.player_score = 0
        self.computer_score = 0
        self.player_score_label.config(text="Player Score: 0")
        self.computer_score_label.config(text="Computer Score: 0")
        self.rock_button.config(state=tk.NORMAL)
        self.paper_button.config(state=tk.NORMAL)
        self.scissors_button.config(state=tk.NORMAL)

    def play(self, player_choice):
        choices = ["rock", "paper", "scissors"]
        computer_choice = choice(choices)

        if player_choice == computer_choice:
            result = "It's a tie!"
        elif (player_choice == "rock" and computer_choice == "scissors") or \
                (player_choice == "paper" and computer_choice == "rock") or \
                (player_choice == "scissors" and computer_choice == "paper"):
            result = "Player wins this round!"
            self.player_score += 1
        else:
            result = "Computer wins this round!"
            self.computer_score += 1

        self.result_label.config(text=f"Player: {player_choice}, Computer: {computer_choice}, {result}")
        self.player_score_label.config(text=f"Player Score: {self.player_score}")
        self.computer_score_label.config(text=f"Computer Score: {self.computer_score}")

        if self.player_score == self.max_points or self.computer_score == self.max_points:
            self.total_rounds += 1
            self.total_player_score += self.player_score
            self.total_computer_score += self.computer_score
            self.total_player_score_label.config(
                text=f"Total Player Score: {self.total_player_score} ({self.total_rounds} rounds)")
            self.total_computer_score_label.config(
                text=f"Total Computer Score: {self.total_computer_score} ({self.total_rounds} rounds)")
            self.rock_button.config(state=tk.DISABLED)
            self.paper_button.config(state=tk.DISABLED)
            self.scissors_button.config(state=tk.DISABLED)

        if self.total_rounds == self.max_rounds:
            if self.total_player_score > self.total_computer_score:
                self.result_label.config(text="Player wins the game!")
            elif self.total_player_score < self.total_computer_score:
                self.result_label.config(text="Computer wins the game!")
            else:
                self.result_label.config(text="It's a tie game!")

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    game = RockPaperScissors()
    game.run()