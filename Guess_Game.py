import tkinter as tk
import random

def start_game():
    global number_to_guess, attempts, result_label
    number_to_guess = random.randint(1, 100)
    attempts = 0
    result_label.config(text="I have chosen a number between 1 and 100. Start guessing!")

def check_guess():
    global attempts
    try:
        user_guess = int(guess_entry.get())
        attempts += 1

        if user_guess < number_to_guess:
            result_label.config(text="Too low! Try again.")
        elif user_guess > number_to_guess:
            result_label.config(text="Too high! Try again.")
        else:
            result_label.config(text=f"Congratulations! You've guessed the number {number_to_guess} correctly in {attempts} attempts.")
    except ValueError:
        result_label.config(text="Invalid input. Please enter a valid number.")


root = tk.Tk()
root.title("Number Guessing Game")


welcome_label = tk.Label(root, text="Welcome to the Number Guessing Game!", font=("Helvetica", 14))
welcome_label.pack(pady=10)

instructions_label = tk.Label(root, text="Click 'Start Game' to begin.", font=("Helvetica", 12))
instructions_label.pack(pady=5)

guess_entry = tk.Entry(root, width=10, font=("Helvetica", 12))
guess_entry.pack(pady=5)

check_button = tk.Button(root, text="Check Guess", command=check_guess, font=("Helvetica", 12))
check_button.pack(pady=5)

start_button = tk.Button(root, text="Start Game", command=start_game, font=("Helvetica", 12))
start_button.pack(pady=5)

result_label = tk.Label(root, text="", font=("Helvetica", 12), fg="blue")
result_label.pack(pady=10)


root.mainloop()
