import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import random
import string
import pyperclip

class PasswordGeneratorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Secure Password Generator")
        self.master.configure(bg="#EDFBD2")  # Set the background color

        # Heading
        self.label_heading = tk.Label(master, text="🔐 CrypticPassGen 🔐", font=("Helvetica", 18), bg="#EDFBD2")
        self.label_heading.grid(row=0, column=0, columnspan=4, pady=10)

        self.complexity_var = tk.StringVar()
        self.complexity_var.set("Medium")  # Default complexity

        
        self.label_complexity = tk.Label(master, text="Password Complexity:", bg="#EDFBD2", font=("Helvetica", 10, "bold"))
        self.label_complexity.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)

        self.low_radio = tk.Radiobutton(master, text="Low(A-Z & a-z)", variable=self.complexity_var, value="Low",bg="#EDFBD2")
        self.low_radio.grid(row=1, column=1, padx=10, pady=10, sticky=tk.W)

        self.medium_radio = tk.Radiobutton(master, text="Medium(A-Z|a-z & 0-9)", variable=self.complexity_var, value="Medium",bg="#EDFBD2")
        self.medium_radio.grid(row=1, column=2, padx=10, pady=10, sticky=tk.W)

        self.high_radio = tk.Radiobutton(master, text="High(with symbols)", variable=self.complexity_var, value="High",bg="#EDFBD2")
        self.high_radio.grid(row=1, column=3, padx=10, pady=10, sticky=tk.W)

        self.label_length = tk.Label(master, text="📏Desired password length:",bg="#EDFBD2", font=("Helvetica", 10, "bold"))
        self.label_length.grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)

        self.length_var = tk.StringVar()
        self.entry_length = tk.Entry(master, textvariable=self.length_var)
        self.entry_length.grid(row=2, column=1, padx=10, pady=10, sticky=tk.W)

        self.btn_generate = tk.Button(master, text="Generate Password", command=self.generate_password, bg="#A4B97D",font=("Helvetica", 10, "bold"))
        self.btn_generate.grid(row=3, column=1, columnspan=2, pady=10)


        self.label_generated = tk.Label(master, text="✨ Generated password is:",bg="#EDFBD2",font=("Helvetica", 10, "bold"))
        self.label_generated.grid(row=4, column=0, padx=10, pady=10, sticky=tk.W)

        self.text_generated = scrolledtext.ScrolledText(master, height=0.5, width=30, wrap=tk.WORD)
        self.text_generated.grid(row=4, column=1, columnspan=3, padx=10, pady=10, sticky=tk.W)

        # Password complexity rules
        self.complexity_rules = {
            "Low": string.ascii_letters,
            "Medium": string.ascii_letters + string.digits,
            "High": string.ascii_letters + string.digits + string.punctuation
        }

    def generate_password(self):
        try:
            length = int(self.length_var.get())
            if length <= 0:
                messagebox.showerror("Error", "Password length must be greater than 0")
                return

            complexity = self.complexity_var.get()
            characters = self.complexity_rules[complexity]

            password = ''.join(random.choice(characters) for _ in range(length))
            self.copy_to_clipboard(password)

            # Display the generated password in the text widget
            self.text_generated.delete(1.0, tk.END)
            self.text_generated.insert(tk.END, password)
            
            messagebox.showinfo("Success", "Successfully generated a Secure Password and copied to clipboard!")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number for password length")

    def copy_to_clipboard(self, password):
        pyperclip.copy(password)



if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()