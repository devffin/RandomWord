"""RandomWord: display exactly one randomly selected entry per launch."""

import random
import sys
import tkinter as tk
from pathlib import Path
from tkinter import messagebox, ttk

__version__ = "1.0.1"


def get_words_path():
    """Resolve the external word list independently of the working directory."""
    if getattr(sys, "frozen", False):
        return Path(sys.executable).resolve().parent / "words.txt"
    return Path(__file__).resolve().parent / "words.txt"


def load_words(path):
    """Read UTF-8 (with or without BOM), ignoring whitespace-only lines."""
    with Path(path).open("r", encoding="utf-8-sig") as file:
        words = [word for line in file if (word := line.strip())]
    if not words:
        raise ValueError("The word list contains no non-empty entries.")
    return words


def main():
    window = tk.Tk()
    window.withdraw()
    window.title("RandomWord")
    path = get_words_path()

    try:
        words = load_words(path)
    except (OSError, UnicodeError, ValueError) as error:
        if isinstance(error, UnicodeError):
            reason = "Save words.txt as UTF-8 and try again."
        elif isinstance(error, ValueError):
            reason = "Add at least one non-empty entry to words.txt."
        elif isinstance(error, FileNotFoundError):
            reason = "Keep words.txt beside main.py or RandomWord.exe."
        else:
            reason = "Check that the file is readable and is not a folder."
        try:
            messagebox.showerror(
                "RandomWord - Unable to load words",
                f"The word list could not be loaded.\n\n{reason}\n\nFile: {path}",
                parent=window,
            )
        finally:
            window.destroy()
        return 1

    # Choose once: resizing, keyboard input and closing never draw another word.
    word = random.choice(words)
    del words

    width = min(480, max(240, window.winfo_screenwidth() - 40))
    window.geometry(f"{width}x200")
    window.minsize(min(320, width), 200)
    window.columnconfigure(0, weight=1)
    window.rowconfigure(0, weight=1)

    content = ttk.Frame(window, padding=20)
    content.grid(row=0, column=0, sticky="nsew")
    content.columnconfigure(0, weight=1)
    content.rowconfigure(1, weight=1)

    ttk.Label(content, text="Random word:").grid(row=0, column=0, pady=(0, 8))
    word_label = ttk.Label(
        content,
        text=word,
        font=("Segoe UI", 18),
        anchor="center",
        justify="center",
        wraplength=width - 40,
    )
    word_label.grid(row=1, column=0, sticky="nsew", pady=(0, 12))
    content.bind(
        "<Configure>",
        lambda event: word_label.configure(wraplength=max(100, event.width - 40)),
    )

    ok_button = ttk.Button(content, text="OK", command=window.destroy)
    ok_button.grid(row=2, column=0)
    window.bind("<Return>", lambda event: window.destroy())
    window.bind("<Escape>", lambda event: window.destroy())
    window.protocol("WM_DELETE_WINDOW", window.destroy)
    window.deiconify()
    ok_button.focus_set()
    window.mainloop()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
