import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import csv

class BMIApp:
    def __init__(self, master):
        self.master = master
        self.master.title("BMI Calculator")

        # Check if the CSV file exists, create it if not
        try:
            with open("bmi_history.csv", mode="r"):
                pass
        except FileNotFoundError:
            with open("bmi_history.csv", mode="w", newline=''):
                pass

        self.users_data = []  # List to store user data

        self.label_name = tk.Label(master, text="Name:")
        self.label_name.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)

        self.entry_name = ttk.Entry(master)
        self.entry_name.grid(row=0, column=1, padx=10, pady=10, sticky=tk.W)

        self.label_weight = tk.Label(master, text="Weight (kg):")
        self.label_weight.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)

        self.entry_weight = ttk.Entry(master)
        self.entry_weight.grid(row=1, column=1, padx=10, pady=10, sticky=tk.W)

        self.label_height = tk.Label(master, text="Height (m):")
        self.label_height.grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)

        self.entry_height = ttk.Entry(master)
        self.entry_height.grid(row=2, column=1, padx=10, pady=10, sticky=tk.W)

        self.btn_calculate = tk.Button(master, text="Calculate BMI", command=self.calculate_bmi)
        self.btn_calculate.grid(row=3, column=0, columnspan=2, pady=10)

        # Result Text with Scrollbar
        self.result_text = tk.Text(self.master, wrap=tk.WORD, height=10, width=50)
        self.result_text.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

        # Treeview for displaying user data
        self.tree = ttk.Treeview(master, columns=("Name", "Weight", "Height", "BMI"))
        self.tree.heading("#0", text="User")
        self.tree.heading("Name", text="Name")
        self.tree.heading("Weight", text="Weight (kg)")
        self.tree.heading("Height", text="Height (m)")
        self.tree.heading("BMI", text="BMI")
        self.tree.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

        # Graph
        self.fig, self.ax = plt.subplots(figsize=(8, 3.7))
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.master)
        self.canvas.get_tk_widget().grid(row=6, column=0, columnspan=2, padx=10, pady=10)

        # Button to view history
        self.btn_history = tk.Button(master, text="View History", command=self.view_history)
        self.btn_history.grid(row=7, column=0, pady=10)

        # Button to view graph
        self.btn_graph = tk.Button(master, text="View Graph", command=self.view_graph)
        self.btn_graph.grid(row=7, column=1, pady=10)

    def calculate_bmi(self):
        try:
            name = self.entry_name.get()
            weight = float(self.entry_weight.get())
            height = float(self.entry_height.get())
            bmi = weight / (height ** 2)

            user_data = {"Name": name, "Weight": weight, "Height": height, "BMI": bmi}
            self.users_data.append(user_data)

            # Determine background color for the result text based on BMI category
            bg_color = self.get_background_color(bmi)

            result_text = f"\n{name}, your Body Mass Index is: {bmi:.2f}\n\n"

            if bmi < 18.5:
                result_text += "🌟 Underweight - Have a balanced diet to achieve a healthy weight\n"
            elif 18.5 <= bmi <= 24.9:
                result_text += "🌈 Normal weight - Keep it up!\n"
            elif 25 <= bmi <= 29.9:
                result_text += "🏋️ Overweight - Start an exercise routine\n"
            elif 30 <= bmi <= 34.9:
                result_text += "🍏 Obesity class I - Balance diet, exercise, and seek professional guidance for obesity\n"
            elif 35 <= bmi <= 39.9:
                result_text += "🥗 Obesity class II - Embrace diet, exercise, and professional guidance for obesity class 2 management\n"
            else:
                result_text += "⚠️ Obesity class III - Seek professional guidance promptly for management of obesity through lifestyle changes\n"

            # Insert text with specified background color
            self.result_text.insert(tk.END, result_text, f"{bg_color}_tag")
            self.result_text.tag_configure(f"{bg_color}_tag", background=bg_color)

            # Update treeview
            self.tree.insert("", "end", text=f"User {len(self.users_data)}", values=(name, weight, height, bmi))

            # Update graph with axis titles
            self.ax.clear()
            self.ax.plot(range(1, len(self.users_data) + 1), [user["BMI"] for user in self.users_data], marker='o', linestyle='-')
            self.ax.set_xlabel("User")
            self.ax.set_ylabel("BMI")
            self.ax.set_title("BMI Trend")

            self.canvas.draw()

            # Save user data to CSV file
            with open("bmi_history.csv", mode="a", newline='') as file:
                writer = csv.writer(file)
                writer.writerow([name, weight, height, bmi])

        except ValueError:
            messagebox.showerror("Error", "Please enter valid name, weight, and height.")

    def view_history(self):
        try:
            # Read user data from CSV file
            with open("bmi_history.csv", mode="r", newline='') as file:
                reader = csv.reader(file)
                history_text = "\nUser History:\n"
                for idx, row in enumerate(reader, 1):
                    history_text += f"{idx}. Name: {row[0]}, Weight: {row[1]}, Height: {row[2]}, BMI: {row[3]}\n"

            messagebox.showinfo("User History", history_text)

        except FileNotFoundError:
            messagebox.showinfo("User History", "No history available.")

    def view_graph(self):
        # Display the graph in a new window
        graph_window = tk.Toplevel(self.master)
        graph_window.title("BMI Trend Graph")

        fig, ax = plt.subplots(figsize=(8, 4))
        canvas = FigureCanvasTkAgg(fig, master=graph_window)
        canvas.get_tk_widget().pack()

        ax.plot(range(1, len(self.users_data) + 1), [user["BMI"] for user in self.users_data], marker='o', linestyle='-')
        ax.set_xlabel("User")
        ax.set_ylabel("BMI")
        ax.set_title("BMI Trend")

        canvas.draw()

    def get_background_color(self, bmi):
        # Determine background color based on BMI category
        if bmi < 18.5:
            return "lightblue"
        elif 18.5 <= bmi <= 24.9:
            return "lightgreen"
        elif 25 <= bmi <= 29.9:
            return "lightyellow"
        elif 30 <= bmi <= 34.9:
            return "lightsalmon"
        elif 35 <= bmi <= 39.9:
            return "lightcoral"
        else:
            return "indianred"

if __name__ == "__main__":
    root = tk.Tk()
    app = BMIApp(root)
    root.mainloop()
