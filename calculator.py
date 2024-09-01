import tkinter as tk
from tkinter import messagebox, colorchooser
import winsound

# Create the main window
root = tk.Tk()
root.title("Calculator")
root.geometry("700x700")  # Set the size of the window
root.config(background="black")
# Global variable to store the current math expression
expression = ""

# Function to update the expression variable
def change_background_color():
    color = colorchooser.askcolor(title="Choose a background color")
    if color[1]:  # Check if a color was selected
        root.config(background=color[1])

def change_button_color():
    color = colorchooser.askcolor(title="Choose a button color")
    if color[1]:  # Check if a color was selected
        button_1.config(bg=color[1])
        button_2.config(bg=color[1])
        button_3.config(bg=color[1])
        button_4.config(bg=color[1])
        button_5.config(bg=color[1])
        button_6.config(bg=color[1])
        button_7.config(bg=color[1])
        button_8.config(bg=color[1])
        button_9.config(bg=color[1])
        button_0.config(bg=color[1])
        button_add.config(bg=color[1])
        button_subtract.config(bg=color[1])
        button_multiply.config(bg=color[1])
        button_divide.config(bg=color[1])
        button_equal.config(bg=color[1])
        button_clear.config(bg=color[1])
        change_background_button.config(bg=color[1])
        change_button_color_button.config(bg=color[1])

change_background_button = tk.Button(root, bg = "deeppink1",fg = "white",text="Change Background Color", width=20, height=3, font=('Arial', 18), command=change_background_color,relief="raised", bd=5)
change_background_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

change_button_color_button = tk.Button(root, bg = "deeppink1",fg = "white",text="Change Button Color", width=20, height=3, font=('Arial', 18), command=change_button_color,relief="raised", bd=5)
change_button_color_button.grid(row=5, column=2, columnspan=2, padx=5, pady=5)
def update_expression(num):
    global expression
    expression += str(num)
    equation.set(expression)

def calculate():
    try:
        global expression
        result = eval(expression)
        equation.set(result)
        expression = str(result)
    except Exception as e:
        messagebox.showerror("Error", str(e))
        expression = ""
        equation.set(expression)
def clear():
    global expression
    expression = ""
    equation.set(expression)

# Create a entry field to display the current math expression
equation = tk.StringVar()
expression_field = tk.Entry(root, textvariable=equation, width=20, font=('Arial', 24))
expression_field.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Create number buttons
button_1 = tk.Button(root, bg = "orange", fg = "white",text="1", width=10, height=3, font=('Arial', 18), command=lambda: [update_expression(1),winsound.Beep(1500, 500)],relief="raised", bd=5)
button_1.grid(row=1, column=0, padx=5, pady=5)
button_2 = tk.Button(root, bg = "orange", fg = "white",text="2", width=10, height=3, font=('Arial', 18), command=lambda: [update_expression(2),winsound.Beep(1500, 500)],relief="raised", bd=5)
button_2.grid(row=1, column=1, padx=5, pady=5)
button_3 = tk.Button(root, bg = "orange", fg = "white", text="3", width=10, height=3, font=('Arial', 18), command=lambda: [update_expression(3),winsound.Beep(1500, 500)],relief="raised", bd=5)
button_3.grid(row=1, column=2, padx=5, pady=5)

button_4 = tk.Button(root, bg = "orange",fg = "white", text="4", width=10, height=3, font=('Arial', 18), command=lambda: [update_expression(4),winsound.Beep(1500, 500)],relief="raised", bd=5)
button_4.grid(row=2, column=0, padx=5, pady=5)
button_5 = tk.Button(root, bg="orange", fg="white", text="5", width=10, height=3, font=('Arial', 18),
                     command=lambda: [update_expression(5), winsound.Beep(1500, 500)],
                     relief="raised", bd=5)
button_5.grid(row=2, column=1, padx=5, pady=5)
button_6 = tk.Button(root, bg = "orange",fg = "white", text="6", width=10, height=3, font=('Arial', 18), command=lambda:[ update_expression(6),winsound.Beep(1500, 500)],relief="raised", bd=5)
button_6.grid(row=2, column=2, padx=5, pady=5)

button_7 = tk.Button(root,bg = "orange",fg = "white", text="7", width=10, height=3, font=('Arial', 18), command=lambda: [update_expression(7),winsound.Beep(1500, 500)],relief="raised", bd=5)
button_7.grid(row=3, column=0, padx=5, pady=5)
button_8 = tk.Button(root,bg = "orange",fg = "white", text="8", width=10, height=3, font=('Arial', 18), command=lambda: [update_expression(8),winsound.Beep(1500, 500)],relief="raised", bd=5)
button_8.grid(row=3, column=1, padx=5, pady=5)
button_9 = tk.Button(root,bg = "orange",fg = "white", text="9", width=10, height=3, font=('Arial', 18), command=lambda: [update_expression(9),winsound.Beep(1500, 500)],relief="raised", bd=5)
button_9.grid(row=3, column=2, padx=5, pady=5)

button_0 = tk.Button(root,bg = "orange",fg = "white", text="0", width=10, height=3, font=('Arial', 18), command=lambda: [update_expression(0),winsound.Beep(1500, 500)],relief="raised", bd=5)
button_0.grid(row=4, column=0, padx=5, pady=5)

# Create operator buttons
button_add = tk.Button(root, bg = "#00C957",fg = "white",text="+", width=10, height=3, font=('Arial', 18), command=lambda: [update_expression("+"),winsound.Beep(1500, 500)],relief="raised", bd=5)
button_add.grid(row=1, column=3, padx=5, pady=5)
button_subtract = tk.Button(root, bg = "#00C957",fg = "white", text="-", width=10, height=3, font=('Arial', 18), command=lambda: [update_expression("-"),winsound.Beep(1500, 500)],relief="raised", bd=5)
button_subtract.grid(row=2, column=3, padx=5, pady=5)
button_multiply = tk.Button(root, bg = "#00C957",fg = "white", text="*", width=10, height=3, font=('Arial', 18), command=lambda: [update_expression("*"),winsound.Beep(1500, 500)],relief="raised", bd=5)
button_multiply.grid(row=3, column=3, padx=5, pady=5)
button_divide = tk.Button(root, bg = "#00C957",fg = "white", text="/", width=10, height=3, font=('Arial', 18), command=lambda: [update_expression("/"),winsound.Beep(1500, 500)],relief="raised", bd=5)
button_divide.grid(row=4, column=3, padx=5, pady=5)

button_equal = tk.Button(root, bg = "#00C957",fg = "white",text="=", width=10, height=3, font=('Arial', 18), command=calculate,relief="raised", bd=5)
button_equal.grid(row=4, column=2, padx=5, pady=5)
button_clear = tk.Button(root, bg = "darkolivegreen1",fg = "red",text="Clear", width=10, height=3, font=('Arial', 18), command=clear,relief="raised", bd=5)
button_clear.grid(row=4, column=1, padx=5, pady=5)

root.mainloop()