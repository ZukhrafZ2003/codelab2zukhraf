import tkinter as tk
from tkinter import messagebox

# Create main window
root = tk.Tk()
root.title("To-Do List")
root.geometry("450x500")
root.configure(bg="#1e3d59")  # deep navy teal background

# ===== Functions =====
def add_task():
    task = task_entry.get().strip()
    if task:
        listbox.insert(tk.END, f"• {task}")
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task!")

def delete_task():
    try:
        selected_task = listbox.curselection()[0]
        listbox.delete(selected_task)
    except:
        messagebox.showwarning("Warning", "Please select a task to delete!")

def clear_all():
    if listbox.size() > 0:
        confirm = messagebox.askyesno("Clear All", "Are you sure you want to delete all tasks?")
        if confirm:
            listbox.delete(0, tk.END)

# ===== Title =====
title_label = tk.Label(root,
                       text=" My To-Do List ",
                       font=("Arial Rounded MT Bold", 22),
                       bg="#7eb8eb",
                       fg="#090908")  # golden peach
title_label.pack(pady=15)

# ===== Entry box =====
task_entry = tk.Entry(root,
                      font=("Arial", 14),
                      width=30,
                      bd=3,
                      relief="solid",
                      justify="center",
                      bg="#91c2df",       # darker teal
                      fg="#f5f0e1",       # light beige text
                      insertbackground="#f5af19")  # cursor color
task_entry.pack(pady=10)

# ===== Buttons Frame =====
btn_frame = tk.Frame(root, bg="#72a0c9")
btn_frame.pack(pady=10)

add_btn = tk.Button(btn_frame, text="Add Task",
                    font=("Arial", 12, "bold"),
                    bg="#16a085", fg="#040404",
                    activebackground="#16a085", activeforeground="#ab934a",
                    width=12, relief="flat", command=add_task)
add_btn.grid(row=0, column=0, padx=5, pady=5)

del_btn = tk.Button(btn_frame, text="Delete Task",
                    font=("Arial", 12, "bold"),
                    bg="#c0392b", fg="#0b0b0a",
                    activebackground="#c0392b", activeforeground="#a1905d",
                    width=12, relief="flat", command=delete_task)
del_btn.grid(row=0, column=1, padx=5, pady=5)

clear_btn = tk.Button(btn_frame, text="Clear All",
                      font=("Arial", 12, "bold"),
                      bg="#34495e", fg="#040404",
                      activebackground="#34495e", activeforeground="#a79766",
                      width=12, relief="flat", command=clear_all)
clear_btn.grid(row=0, column=2, padx=5, pady=5)

# ===== Listbox Frame =====
list_frame = tk.Frame(root, bg="#1e3d59")
list_frame.pack(pady=10)

scrollbar = tk.Scrollbar(list_frame, bg="#1e3d59", troughcolor="#1e3d59")
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

listbox = tk.Listbox(list_frame,
                     font=("Arial", 14),
                     width=38, height=12,
                     bd=3, relief="sunken",
                     bg="#9dcae4", fg="#f5f0e1",
                     selectbackground="#fdfcf9",
                     activestyle="dotbox",
                     yscrollcommand=scrollbar.set)
listbox.pack()

scrollbar.config(command=listbox.yview)

# ===== Footer =====
footer = tk.Label(root, text=" Stay focused & slay your day ",
                  font=("Arial", 10, "italic"),
                  bg="#87b9e4", fg="#0A0909")
footer.pack(pady=10)

# Run app
root.mainloop()

