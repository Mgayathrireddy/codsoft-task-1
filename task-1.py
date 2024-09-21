import tkinter as tk
from tkinter import messagebox
import pickle
from datetime import datetime

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")
        
        self.tasks = self.load_tasks()
        
        self.frame = tk.Frame(root)
        self.frame.pack(pady=10)
        
        self.task_listbox = tk.Listbox(self.frame, width=50, height=10)
        self.task_listbox.pack(side=tk.LEFT, fill=tk.BOTH)
        
        self.scrollbar = tk.Scrollbar(self.frame, orient=tk.VERTICAL)
        self.scrollbar.config(command=self.task_listbox.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.task_listbox.config(yscrollcommand=self.scrollbar.set)
        
        self.entry = tk.Entry(root, width=50)
        self.entry.pack(pady=5)
        
        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.pack(pady=5)
        
        self.mark_done_button = tk.Button(root, text="Mark Task as Done", command=self.mark_done)
        self.mark_done_button.pack(pady=5)
        
        self.delete_button = tk.Button(root, text="Delete Task", command=self.delete_task)
        self.delete_button.pack(pady=5)
        
        self.load_tasks()
        self.update_listbox()
    
    def load_tasks(self):
        try:
            with open('tasks.pkl', 'rb') as f:
                return pickle.load(f)
        except FileNotFoundError:
            return []
    
    def save_tasks(self):
        with open('tasks.pkl', 'wb') as f:
            pickle.dump(self.tasks, f)
    
    def update_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for idx, task in enumerate(self.tasks):
            status = "Done" if task['done'] else "Pending"
            self.task_listbox.insert(tk.END, f"{idx+1}. {task['description']} [{status}]")
    
    def add_task(self):
        description = self.entry.get()
        if description:
            task = {'description': description, 'done': False, 'created_at': datetime.now()}
            self.tasks.append(task)
            self.save_tasks()
            self.update_listbox()
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Task description cannot be empty.")
    
    def mark_done(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            self.tasks[selected_index]['done'] = True
            self.save_tasks()
            self.update_listbox()
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to mark as done.")
    
    def delete_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            self.tasks.pop(selected_index)
            self.save_tasks()
            self.update_listbox()
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to delete.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()
