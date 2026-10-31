import tkinter as tk
from tkinter import ttk


def reverse_integer(number: int) -> int:
    """Return the digits of an integer in reverse order, preserving its sign."""
    sign = -1 if number < 0 else 1
    reversed_digits = int(str(abs(number))[::-1])
    return sign * reversed_digits


def is_palindrome(number: int) -> bool:
    """Return whether a non-negative integer reads the same in both directions."""
    return number >= 0 and number == reverse_integer(number)


class NumberToolsApp:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("Number Tools")
        self.root.resizable(False, False)

        frame = ttk.Frame(root, padding=20)
        frame.grid()

        ttk.Label(frame, text="Enter an integer").grid(row=0, column=0, sticky="w")
        self.number_entry = ttk.Entry(frame, width=24)
        self.number_entry.grid(row=1, column=0, pady=(6, 10), sticky="ew")
        self.number_entry.bind("<Return>", self.check_number)

        ttk.Button(frame, text="Check", command=self.check_number).grid(
            row=1, column=1, padx=(8, 0), pady=(6, 10)
        )

        self.result_label = ttk.Label(frame, text="", justify="left")
        self.result_label.grid(row=2, column=0, columnspan=2, sticky="w")
        self.number_entry.focus_set()

    def check_number(self, _event: tk.Event | None = None) -> None:
        text = self.number_entry.get().strip()
        try:
            number = int(text)
        except ValueError:
            self.result_label.configure(text="Please enter a valid integer.")
            return

        reversed_number = reverse_integer(number)
        palindrome = "Yes" if is_palindrome(number) else "No"
        self.result_label.configure(
            text=f"Reversed: {reversed_number}\nPalindrome: {palindrome}"
        )


if __name__ == "__main__":
    root = tk.Tk()
    NumberToolsApp(root)
    root.mainloop()