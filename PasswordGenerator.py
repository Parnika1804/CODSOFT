import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    username = username_entry.get()
    birthday = birthday_entry.get()
    difficulty = difficulty_var.get()
    if not username or not birthday:
        messagebox.showerror("Error", "Please enter both username and birthday")
        return
    password = username + birthday
    if difficulty == "Easy":
        password = password[:8]
        password += ''.join(random.choice(string.punctuation) for _ in range(1))  # Add at least one special character
    elif difficulty == "Medium":
        password = password[:12]
        password += ''.join(random.choice(string.ascii_uppercase) for _ in range(2))
        password += ''.join(random.choice(string.punctuation) for _ in range(1))  # Add at least one special character
    elif difficulty == "Hard":
        password = password[:12]
        password += ''.join(random.choice(string.ascii_uppercase) for _ in range(4))
        password += ''.join(random.choice(string.digits) for _ in range(2))
        password += ''.join(random.choice(string.punctuation) for _ in range(2))  # Add at least two special characters
    password_list = list(password)
    random.shuffle(password_list)  # Shuffle the password to ensure randomness
    password = ''.join(password_list)
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

def copy_password():
    root.clipboard_clear()
    root.clipboard_append(password_entry.get())

def exit_application():
    if messagebox.askyesno("Confirm", "Are you sure you want to exit?"):
        root.destroy()

root = tk.Tk()
root.title("Password Generator")
root.attributes("-fullscreen", True)  # Make the window full screen
root.configure(background='#333')  # Change background color to dark gray

# Add heading
heading_label = tk.Label(root, text="Welcome to Password Generator", font=("Arial", 36, "bold"), fg='deeppink2', bg='#333')  # Change text color to white
heading_label.place(relx=0.5, rely=0.05, anchor=tk.CENTER)

# Username
username_label = tk.Label(root, text="Enter your username:", font=("Arial", 24), fg='deeppink2', bg='#333')  # Change text color to white
username_label.place(relx=0.3, rely=0.15, anchor=tk.E)
username_entry = tk.Entry(root, font=("Arial", 24), fg='deeppink2', bg='#333')  # Change text color to white
username_entry.place(relx=0.5, rely=0.15, anchor=tk.W)

# Birthday
birthday_label = tk.Label(root, text="Enter your birthday (MMDD):", font=("Arial", 24), fg='deeppink2', bg='#333')  # Change text color to white
birthday_label.place(relx=0.36, rely=0.25, anchor=tk.E)
birthday_entry = tk.Entry(root, font=("Arial", 24), fg='deeppink2', bg='#333')  # Change text color to white
birthday_entry.place(relx=0.5, rely=0.25, anchor=tk.W)

difficulty_var = tk.StringVar(root)
difficulty_var.set("Easy")  # default value
difficulty_label = tk.Label(root, text="Select difficulty level:", font=("Arial", 24), fg='deeppink2', bg='#333')  # Change text color to white
difficulty_label.place(relx=0.28, rely=0.4, anchor=tk.E)
difficulty_menu = tk.OptionMenu(root, difficulty_var, "Easy", "Medium", "Hard")
difficulty_menu.config(font=("Arial", 24), fg='deeppink2', bg='#333')  # Change text color to white
difficulty_menu.place(relx=0.5, rely=0.4, anchor=tk.W)

generate_button = tk.Button(root, text="Generate Password", command=generate_password, font=("Arial", 24), fg='deeppink2', bg='#333')  # Change text color to white
generate_button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

password_entry = tk.Entry(root, width=40, font=("Arial", 24), fg='deeppink2', bg='#333')  # Change text color to white
password_entry.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

copy_button = tk.Button(root, text="Copy to Clipboard", command=copy_password, font=("Arial", 24), fg='deeppink2', bg='#333')  # Change text color to white
copy_button.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

exit_button = tk.Button(root, text="Exit", command=exit_application, font=("Arial", 24), fg='#fff', bg='red')  # Change text color to white and background color to red
exit_button.place(relx=0.5, rely=0.8, anchor=tk.CENTER)

root.mainloop()