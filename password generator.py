import tkinter as tk
from tkinter import ttk, messagebox
import random
import string

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")

        self.length_label = ttk.Label(root, text="Password Length:")
        self.length_label.grid(row=0, column=0, pady=10, padx=10)

        self.length_entry = ttk.Entry(root, width=5)
        self.length_entry.grid(row=0, column=1, pady=10)

        self.include_digits_var = tk.BooleanVar()
        self.include_digits_var.set(True)
        self.include_digits_check = ttk.Checkbutton(root, text="Include Digits", variable=self.include_digits_var)
        self.include_digits_check.grid(row=1, column=0, columnspan=2, pady=5, padx=10, sticky=tk.W)

        self.include_special_chars_var = tk.BooleanVar()
        self.include_special_chars_var.set(True)
        self.include_special_chars_check = ttk.Checkbutton(root, text="Include Special Characters", variable=self.include_special_chars_var)
        self.include_special_chars_check.grid(row=2, column=0, columnspan=2, pady=5, padx=10, sticky=tk.W)

        self.generate_button = ttk.Button(root, text="Generate Password", command=self.generate_password)
        self.generate_button.grid(row=3, column=0, columnspan=2, pady=10)

    def generate_password(self):
        try:
            length = int(self.length_entry.get())
            include_digits = self.include_digits_var.get()
            include_special_chars = self.include_special_chars_var.get()

            chars = string.ascii_letters
            if include_digits:
                chars += string.digits
            if include_special_chars:
                chars += string.punctuation

            password = ''.join(random.choice(chars) for _ in range(length))

            messagebox.showinfo("Generated Password", f"Generated Password: {password}")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid numeric password length.")

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
