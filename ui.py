# where tkinter code should be
import tkinter as tk
from tkinter import ttk, messagebox
import utils.operators as op


def calculate():
    a = entry_a.get()
    b = entry_b.get()
    operation = operation_var.get()

    try:
        if operation == "Add":
            result = op.add(a, b)
        elif operation == "Multiply":
            result = op.multiply(a, b)
        elif operation == "Modulus":
            result = op.modulus(a, b)
        else:
            raise ValueError("Invalid operation")

        result_label.config(text=f"Result: {result}", fg="green")

    except ZeroDivisionError:
        messagebox.showerror("Error", "Cannot divide by zero!")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers!")
    except TypeError:
        messagebox.showerror("Error", "Unsupported input type!")


root = tk.Tk()
root.title("Math Operations")
root.geometry("350x250")
root.resizable(False, False)

# Inputs
tk.Label(root, text="Enter first number:").pack(pady=4)
entry_a = tk.Entry(root)
entry_a.pack()

tk.Label(root, text="Enter second number:").pack(pady=4)
entry_b = tk.Entry(root)
entry_b.pack()

# Dropdown operations menu
operation_var = tk.StringVar(value="Add")
options = ["Add", "Multiply", "Modulus"]
ttk.OptionMenu(root, operation_var, options[0], *options).pack(pady=10)

# Calculate button
tk.Button(root, text="Calculate", command=calculate).pack(pady=8)

# Result label
result_label = tk.Label(root, text="Result: ", font=("Arial", 14))
result_label.pack(pady=10)

root.mainloop()
