import tkinter as tk
import random

words = ["python", "java", "kotlin", "javascript", "ruby"]
secret_word = random.choice(words)

guessed_letters = []
attempts_left = 6

root = tk.Tk()
root.title("✨ Word Guess Game ✨")
root.geometry("400x300")
root.config(bg="#ffe4e1")  # pastel pink background

word_var = tk.StringVar()
word_var.set("_ " * len(secret_word))

word_label = tk.Label(root, textvariable=word_var, font=("Comic Sans MS", 28, "bold"), bg="#ffe4e1", fg="#ff69b4")
word_label.pack(pady=20)

message_var = tk.StringVar()
message_label = tk.Label(root, textvariable=message_var, font=("Comic Sans MS", 14, "italic"), bg="#ffe4e1", fg="#ff1493")
message_label.pack(pady=10)

guess_entry = tk.Entry(root, font=("Comic Sans MS", 18), width=3, justify='center', bg="#fff0f5", fg="#c71585", bd=3, relief=tk.RIDGE)
guess_entry.pack(pady=10)
guess_entry.focus()

def check_guess():
    global attempts_left
    guess = guess_entry.get().lower()
    guess_entry.delete(0, tk.END)

    if len(guess) != 1 or not guess.isalpha():
        message_var.set("❌ Please enter one letter!")
        return
    if guess in guessed_letters:
        message_var.set("🔁 Already guessed this letter!")
        return

    guessed_letters.append(guess)

    if guess in secret_word:
        message_var.set("🎉 Yay! You got it!")
    else:
        attempts_left -= 1
        message_var.set(f"❌ Nope! Attempts left: {attempts_left}")

    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter.upper() + " "
        else:
            display_word += "• "  # cute dot instead of underscore
    word_var.set(display_word)

    if "•" not in display_word:
        message_var.set(f"🌟 Congrats! You guessed: {secret_word.upper()} 🌟")
        guess_button.config(state=tk.DISABLED)
        guess_entry.config(state=tk.DISABLED)

    if attempts_left <= 0:
        message_var.set(f"💔 Game over! Word was {secret_word.upper()}.")
        word_var.set(" ".join(secret_word.upper()))
        guess_button.config(state=tk.DISABLED)
        guess_entry.config(state=tk.DISABLED)

guess_button = tk.Button(root, text="Guess 💖", font=("Comic Sans MS", 16, "bold"), bg="#ff69b4", fg="white", activebackground="#ff1493", relief=tk.RAISED, bd=4, command=check_guess)
guess_button.pack(pady=10)

root.mainloop()
