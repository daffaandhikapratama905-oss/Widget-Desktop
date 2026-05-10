import tkinter as tk
from tkinter import filedialog
import os

def auto_save(event=None):
    with open("autosave.txt", "w") as f:
        f.write(text_area.get(1.0, tk.END).strip())

def start_move(event):
    root.x, root.y = event.x, event.y

def do_move(event):
    root.geometry(f"+{root.winfo_x() + (event.x - root.x)}+{root.winfo_y() + (event.y - root.y)}")

def munculkan_menu(event):
    menu.post(event.x_root, event.y_root)

root = tk.Tk()
root.overrideredirect(True)
root.attributes("-topmost", True)
root.config(bg='#121212')
root.wm_attributes("-transparentcolor", "#121212")
root.geometry("300x350")

text_area = tk.Text(root, font=("Segoe UI", 11), bg='#1e1e1e', fg='#E0E0E0', 
                    insertbackground='white', relief='flat', padx=10, pady=10)
text_area.pack(fill='both', expand=True, padx=10, pady=10)

if os.path.exists("autosave.txt"):
    with open("autosave.txt", "r") as f:
        text_area.insert(tk.END, f.read())

menu = tk.Menu(root, tearoff=0)
menu.add_command(label="Clear", command=lambda: text_area.delete(1.0, tk.END))
menu.add_command(label="Exit", command=root.destroy)

text_area.bind("<KeyRelease>", auto_save)
text_area.bind("<ButtonPress-1>", start_move)
text_area.bind("<B1-Motion>", do_move)
text_area.bind("<Button-3>", munculkan_menu)

root.mainloop()