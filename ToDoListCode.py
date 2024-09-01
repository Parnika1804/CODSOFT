import random
import time
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import winsound

class TaskManager:
    def __init__(self, root):
        self.root = root
        self.tasks = []

        # Create two sections
        self.left_frame = tk.Frame(root, bg="palevioletred1")  # 4/5th section
        self.left_frame.place(relx=0, rely=0, relwidth=0.8, relheight=1)

        self.right_frame = tk.Frame(root, bg="yellow")  # 1/5th section
        self.right_frame.place(relx=0.8, rely=0, relwidth=0.2, relheight=1)

        # Add heading in the center of the larger section
        self.left_heading_label = tk.Label(self.left_frame, text="YOUR TASKS", font=("Arial", 24, "bold"), bg="palevioletred1", fg="white")
        self.left_heading_label.place(relx=0.5, rely=0.05, anchor=tk.CENTER)
        self.right_heading_label = tk.Label(self.right_frame, text="MANAGE YOUR TASKS", font=("Arial", 20, "bold"), bg="yellow", fg="orange")
        self.right_heading_label.place(relx=0.5, rely=0.05, anchor=tk.CENTER)

        # Add status option menu
        status_var = tk.StringVar()
        status_var.set("Incomplete")  # default value

        status_option = tk.OptionMenu(self.right_frame, status_var, "Incomplete", "Completed")
        status_option.place(relx=0.5, rely=0.3, anchor=tk.CENTER)
        
        # Add table to the larger section
        self.table_frame = tk.Frame(self.left_frame, bg="pink")
        self.table_frame.place(relx=0.5, rely=0.5, relwidth=0.9, relheight=0.5, anchor=tk.CENTER)

        self.tree = ttk.Treeview(self.table_frame, columns=("Task", "Status", "Start Date", "End Date"), show="headings")
        self.tree.column("Task", width=200)
        self.tree.column("Status", width=150)
        self.tree.column("Start Date", width=100)
        self.tree.column("End Date", width=100)
        self.tree.heading("Task", text="Task")
        self.tree.heading("Status", text="Status")
        self.tree.heading("Start Date", text="Start Date")
        self.tree.heading("End Date", text="End Date")
        self.tree.pack(fill=tk.BOTH, expand=True)

        # Add buttons to the smaller section
        self.button_frame = tk.Frame(self.right_frame, bg="yellow")
        self.button_frame.place(relx=0.5, rely=0.3, anchor=tk.CENTER)

        add_task_button = tk.Button(self.button_frame, text="ADD TASK", font=("Arial", 14, "bold"), bg="green", fg="white", command=self.add_task)
        add_task_button.pack(fill=tk.X, padx=10, pady=15)

        delete_task_button = tk.Button(self.button_frame, text="DELETE TASK", font=("Arial", 14, "bold"), bg="red", fg="white", command=self.delete_task)
        delete_task_button.pack(fill=tk.X, padx=10, pady=15)

        update_task_button = tk.Button(self.button_frame, text="UPDATE TASK", font=("Arial", 14, "bold"), bg="blue", fg="white", command=self.update_task)
        update_task_button.pack(fill=tk.X, padx=10, pady=15)

        pomodoro_timer_button = tk.Button(self.button_frame, text="POMODORO TIMER", font=("Arial", 14, "bold"),
                                          bg="orange", fg="white", command=self.start_pomodoro_timer)
        pomodoro_timer_button.pack(fill=tk.X, padx=10, pady=15)
        motivation_button = tk.Button(self.button_frame, text="MOTIVATION", font=("Arial", 14, "bold"), bg="purple",
                                      fg="white", command=self.show_motivation)
        motivation_button.pack(fill=tk.X, padx=10, pady=15)


        # Add image at the end of the smaller section
        image_path = "ToDoListIMAGE.png"  # replace with your image path
        image = Image.open(image_path)
        image = image.resize((300, 300))  # resize image to fit section
        photo = ImageTk.PhotoImage(image)
        image_label = tk.Label(self.right_frame, image=photo, bg="yellow")
        image_label.image = photo  # keep a reference to prevent garbage collection
        image_label.place(relx=0.5, rely=0.8, anchor=tk.CENTER)

    def add_task(self):
        # Create a new window for adding a task
        self.add_window = tk.Toplevel(self.root)
        self.add_window.title("Add Task")
        self.add_window.geometry("400x300")  # Set the window size
        self.add_window.resizable(False, False)  # Make the window non-resizable
        self.play_sound()

        # Create a main frame to hold all the widgets
        main_frame = tk.Frame(self.add_window, bg="#f0f0f0")  # Set the background color
        main_frame.pack(padx=20, pady=20, fill="both", expand=True)

        # Create labels and entries for the task details
        tk.Label(main_frame, text="Task Name:", font=("Arial", 12), bg="#f0f0f0").grid(row=0, column=0, padx=5, pady=5)
        self.task_name_entry = tk.Entry(main_frame, font=("Arial", 12), width=30)
        self.task_name_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(main_frame, text="Start Date:", font=("Arial", 12), bg="#f0f0f0").grid(row=1, column=0, padx=5, pady=5)
        self.start_date_entry = tk.Entry(main_frame, font=("Arial", 12), width=30)
        self.start_date_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(main_frame, text="End Date:", font=("Arial", 12), bg="#f0f0f0").grid(row=2, column=0, padx=5, pady=5)
        self.end_date_entry = tk.Entry(main_frame, font=("Arial", 12), width=30)
        self.end_date_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(main_frame, text="Task Status:", font=("Arial", 12), bg="#f0f0f0").grid(row=3, column=0, padx=5,
                                                                                         pady=5)
        self.task_status_entry = tk.Entry(main_frame, font=("Arial", 12), width=30)
        self.task_status_entry.grid(row=3, column=1, padx=5, pady=5)

        # Create a button to add the task
        self.add_task_button = tk.Button(main_frame, text="Add Task", command=self.add_task_to_tree, font=("Arial", 12),
                                         bg="#4CAF50", fg="#ffffff")
        self.add_task_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

    def add_task_to_tree(self):
        # Get the task details from the entries
        task_name = self.task_name_entry.get()
        start_date = self.start_date_entry.get()
        end_date = self.end_date_entry.get()
        task_status = self.task_status_entry.get()

        # Get the current number of tasks
        task_number = len(self.tree.get_children()) + 1

        # Insert the task into the tree
        self.tree.insert("", "end", iid=task_number,
                         values=(f"{task_number}. {task_name}", task_status, start_date, end_date))

        # Close the add window
        self.add_window.destroy()

    def delete_task(self):
        # Get the selected task
        selected_task = self.tree.selection()
        self.play_sound()

        # If a task is selected, delete it
        if selected_task:
            self.tree.delete(selected_task)

    def update_task(self):
        # Get the selected task
        selected_task = self.tree.selection()
        self.play_sound()

        # If a task is selected, create a new window to update it
        if selected_task:
            self.update_window = tk.Toplevel(self.root)
            self.update_window.title("Update Task")
            self.update_window.geometry("400x300")  # Set the window size
            self.update_window.resizable(False, False)  # Make the window non-resizable

            # Create a main frame to hold all the widgets
            main_frame = tk.Frame(self.update_window, bg="#f0f0f0")  # Set the background color
            main_frame.pack(padx=20, pady=20, fill="both", expand=True)

            # Get the task details from the tree
            task_name = self.tree.item(selected_task, "values")[0]
            start_date = self.tree.item(selected_task, "values")[1]
            end_date = self.tree.item(selected_task, "values")[2]
            task_status = self.tree.item(selected_task, "values")[3]

            # Create labels and entries for the task details
            tk.Label(main_frame, text="Task Name:", font=("Arial", 12), bg="#f0f0f0").grid(row=0, column=0, padx=5,
                                                                                           pady=5)
            self.task_name_entry = tk.Entry(main_frame, font=("Arial", 12), width=30)
            self.task_name_entry.insert(0, task_name)
            self.task_name_entry.grid(row=0, column=1, padx=5, pady=5)

            tk.Label(main_frame, text="Start Date:", font=("Arial", 12), bg="#f0f0f0").grid(row=1, column=0, padx=5,
                                                                                            pady=5)
            self.start_date_entry = tk.Entry(main_frame, font=("Arial", 12), width=30)
            self.start_date_entry.insert(0, start_date)
            self.start_date_entry.grid(row=1, column=1, padx=5, pady=5)

            tk.Label(main_frame, text="End Date:", font=("Arial", 12), bg="#f0f0f0").grid(row=2, column=0, padx=5,
                                                                                          pady=5)
            self.end_date_entry = tk.Entry(main_frame, font=("Arial", 12), width=30)
            self.end_date_entry.insert(0, end_date)
            self.end_date_entry.grid(row=2, column=1, padx=5, pady=5)

            tk.Label(main_frame, text="Task Status:", font=("Arial", 12), bg="#f0f0f0").grid(row=3, column=0, padx=5,
                                                                                             pady=5)
            self.task_status_entry = tk.Entry(main_frame, font=("Arial", 12), width=30)
            self.task_status_entry.insert(0, task_status)
            self.task_status_entry.grid(row=3, column=1, padx=5, pady=5)

            # Create a button to update the task
            self.update_task_button = tk.Button(main_frame, text="Update Task",
                                                command=lambda: self.update_task_in_tree(selected_task),
                                                font=("Arial", 12), bg="#4CAF50", fg="#ffffff")
            self.update_task_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

    def update_task_in_tree(self, selected_task):
        # Get the task details from the entries
        task_name = self.task_name_entry.get()
        start_date = self.start_date_entry.get()
        end_date = self.end_date_entry.get()
        task_status = self.task_status_entry.get()

        # Update the task in the tree
        self.tree.item(selected_task, values=(task_name, start_date, end_date, task_status))

        # Close the update window
        self.update_window.destroy()

    def start_pomodoro_timer(self):
        self.pomodoro_window = tk.Toplevel(self.root)
        self.pomodoro_window.title("Pomodoro Timer")
        self.play_sound()

        # Create a frame with a rounded corner
        self.frame = tk.Frame(self.pomodoro_window, bg="#f2f2f2", highlightbackground="#adadad", highlightthickness=1)
        self.frame.pack(padx=20, pady=20)

        # Create a label with a font that looks like a digital clock
        self.time_label = tk.Label(self.frame, text="25:00", font=("Helvetica", 48, "bold"), bg="#f2f2f2", fg="#333333")
        self.time_label.pack(pady=20)

        # Create buttons with a modern look
        self.button_frame = tk.Frame(self.frame, bg="#f2f2f2")
        self.button_frame.pack(pady=20)

        self.start_button = tk.Button(self.button_frame, text="Start", command=self.start_timer, bg="#4CAF50",
                                      fg="#ffffff", font=("Helvetica", 14, "bold"), padx=10, pady=5)
        self.start_button.pack(side=tk.LEFT, padx=10)

        self.stop_button = tk.Button(self.button_frame, text="Stop", command=self.stop_timer, bg="#e74c3c",
                                     fg="#ffffff", font=("Helvetica", 14, "bold"), padx=10, pady=5)
        self.stop_button.pack(side=tk.LEFT, padx=10)

        self.reset_button = tk.Button(self.button_frame, text="Reset", command=self.reset_timer, bg="#e74c3c",
                                      fg="#ffffff", font=("Helvetica", 14, "bold"), padx=10, pady=5)
        self.reset_button.pack(side=tk.LEFT, padx=10)

        self.seconds = 1500  # 25 minutes in seconds
        self.running = False

    def start_timer(self):
        self.running = True
        self.start_button.config(state="disabled")
        self.stop_button.config(state="normal")
        self.countdown(self.seconds)

    def stop_timer(self):
        self.running = False
        self.start_button.config(state="normal")
        self.stop_button.config(state="disabled")

    def reset_timer(self):
        self.running = False
        self.start_button.config(state="normal")
        self.stop_button.config(state="disabled")
        self.seconds = 1500
        self.time_label.config(text="25:00")

    def countdown(self, count):
        minutes, seconds = divmod(count, 60)
        self.time_label.config(text=f"{minutes:02d}:{seconds:02d}")
        if count > 0 and self.running:
            self.pomodoro_window.after(1000, self.countdown, count - 1)
        elif count == 0 and self.running:
            self.time_label.config(text="Time's up!")
            self.running = False
            self.start_button.config(state="normal")
            self.stop_button.config(state="disabled")

    def show_motivation(self):
        motivation_messages = [
            "Believe you can and you're halfway there.",
            "It does not matter how slowly you go as long as you do not stop.",
            "Success is not final, failure is not fatal: It is the courage to continue that counts.",
            "Don't watch the clock; do what it does. Keep going.",
            "You miss 100% of the shots you don't take.",
            "I have not failed. I've just found 10,000 ways that won't work.",
            "You are never too old to set another goal or to dream a new dream.",
            "The only way to do great work is to love what you do.",
            "Keep your eyes on the stars, and your feet on the ground.",
            "You don't have to be great to start, but you have to start to be great.",
            "Those who don’t believe in magic will never find it.",
            "Be thankful for what you have; you’ll end up having more. If you concentrate on what you don’t have, you will never, ever have enough.",
            "You are stronger than you seem, braver than you believe, and smarter than you think.",
            "The greatest glory in living lies not in never falling, but in rising every time we fall.",
            "Do something today that your future self will thank you for.",
            "Happiness is not something ready made. It comes from your own actions.",
            "The best way to predict your future is to create it.",
            "You don't have to be perfect to be amazing.",
            "Life is 10% what happens to you and 90% how you react to it.",
            "You are one step closer to your goal with every step you take."
        ]

        motivation_window = tk.Toplevel(self.root)
        motivation_window.title("Motivation")
        self.play_sound()

        # Set a background color for the window
        motivation_window.configure(bg="#f2f2f2")

        # Create a frame to hold the motivation label and button
        frame = tk.Frame(motivation_window, bg="#f2f2f2")
        frame.pack(padx=20, pady=20)

        # Create the motivation label with a random message
        motivation_label = tk.Label(frame, text=random.choice(motivation_messages),
                                    font=("Arial", 18, "bold"), bg="#f2f2f2", fg="#00698f")
        motivation_label.pack(pady=10)

        # Create a separator to add some visual interest
        separator = tk.Frame(frame, bg="#00698f", height=2)
        separator.pack(fill="x", pady=10)

        # Create the OK button
        ok_button = tk.Button(frame, text="OK", command=motivation_window.destroy,
                              font=("Arial", 12, "bold"), bg="#00698f", fg="#ffffff")
        ok_button.pack(pady=10)

    def play_sound(self):
        # Define the frequency and duration of the beep
        frequency = 1500  # 1000 Hz
        duration = 500  # 500 ms

        # Play the beep sound
        winsound.Beep(frequency, duration)


def create_full_screen_window():
    root = tk.Tk()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    root.geometry(f"{screen_width}x{screen_height}+0+0")
    root.title("Full Screen Window")
    root.state("zoomed")  # for Windows and Linux
    # root.attributes("-fullscreen", True)  # for macOS

    task_manager = TaskManager(root)

    return root


if __name__ == "__main__":
    root = create_full_screen_window()
    root.mainloop()