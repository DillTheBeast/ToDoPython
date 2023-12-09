import tkinter as tk
from tkinter import messagebox

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")
        root.geometry("800x600")  # Set the initial size of the window (width x height)

        self.tasks = []

        # Task Entry
        self.task_entry = tk.Entry(root, width=70)
        self.task_entry.grid(row=0, column=0, padx=10, pady=10)

        # Add Task Button
        add_button = tk.Button(root, text="Add Task", command=self.add_task)
        add_button.grid(row=0, column=1, padx=10, pady=10)

        # Task List
        self.task_listbox = tk.Listbox(root, selectmode=tk.SINGLE, width=85, height=28)
        self.task_listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        # Remove Task Button
        remove_button = tk.Button(root, text="Remove Task", command=self.remove_task)
        remove_button.grid(row=2, column=0, columnspan=2, pady=10)

        # Load tasks from file
        self.load_tasks()

        # Bind double-click to remove task
        self.task_listbox.bind("<Double-Button-1>", lambda event: self.show_task_window(self.task_listbox.get(tk.ACTIVE)))

        # Add buttons for each task
        for task in self.tasks:
            button = tk.Button(root, text=task, command=lambda t=task: self.show_task_window(t))
            button.grid(row=self.tasks.index(task) + 3, column=0, columnspan=2, pady=5)


    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.task_listbox.insert(tk.END, task)
            self.save_tasks()
            self.task_entry.delete(0, tk.END)

            # Add button for the new task
            button = tk.Button(self.root, text=task, command=lambda t=task: self.show_task_window(t))
            button.grid(row=len(self.tasks) + 2, column=0, columnspan=2, pady=5)

    def show_task_window(self, task):
        # Create a new window for the task
        task_window = tk.Toplevel(self.root)
        task_window.title(task)

        # Add a label to the new window to display content
        label = tk.Label(task_window, text=f"This is the window for task: {task}")
        label.pack(padx=20, pady=20)


    def remove_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            task = self.tasks[selected_index[0]]
            confirmation = messagebox.askyesno("Remove Task", f"Do you want to remove the task:\n'{task}'?")
            if confirmation:
                self.tasks.pop(selected_index[0])
                self.task_listbox.delete(selected_index)
                self.save_tasks()

    def load_tasks(self):
        try:
            with open("todolist.txt", "r") as file:
                self.tasks = [line.strip() for line in file.readlines()]
                for task in self.tasks:
                    self.task_listbox.insert(tk.END, task)
        except FileNotFoundError:
            pass

    def save_tasks(self):
        with open("todolist.txt", "w") as file:
            for task in self.tasks:
                file.write(f"{task}\n")

def main():
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
