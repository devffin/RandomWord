import random
import tkinter as tk

with open("words.txt", "r", encoding="utf-8") as file:
    words = file.readlines()

word = random.choice(words).strip()

window = tk.Tk()
window.title("WordRandom")
window.geometry("300x100")

sayWord = tk.Label(
    text=f"Random word: {word}",
    font=("Arial", 12)
)
sayWord.pack(pady=10)

okButton = tk.Button(
    text="OK",
    command=window.destroy
)
okButton.pack(pady=10)

window.mainloop()