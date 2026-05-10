import tkinter as tk
import calendar
from datetime import datetime

def start_move(e): root.x, root.y = e.x, e.y
def do_move(e): root.geometry(f"+{root.winfo_x()+(e.x-root.x)}+{root.winfo_y()+(e.y-root.y)}")

root = tk.Tk()
root.overrideredirect(True)
root.attributes("-topmost", True, "-transparentcolor", "#121212")
root.config(bg='#121212')

f = tk.Frame(root, bg='#1e1e1e', padx=15, pady=15)
f.pack(padx=10, pady=10)

now = datetime.now()

tk.Label(f, text=now.strftime("%B %Y"), fg="#AFF7A4", bg="#1e1e1e", font=("Segoe UI", 12, "bold")).grid(row=0, columnspan=7, pady=5)

for i, h in enumerate(["Mo", "Tu", "We", "Th", "Fr", "Sa", "Su"]):
    tk.Label(f, text=h, fg="#E0E0E0" if i<5 else "#ff758c", bg="#1e1e1e", font=("Segoe UI", 10, "bold")).grid(row=1, column=i, padx=5)

for r, mgu in enumerate(calendar.monthcalendar(now.year, now.month)):
    for c, tgl in enumerate(mgu):
        if tgl:
            is_today = (tgl == now.day)
            tk.Label(f, text=tgl, fg="#AFF7A4" if is_today else "#E0E0E0", 
                     bg="#333333" if is_today else "#1e1e1e", font=("Segoe UI", 10), width=3).grid(row=r+2, column=c, pady=2)

m = tk.Menu(root, tearoff=0)
m.add_command(label="Exit", command=root.destroy)

def bind_all(w):
    w.bind("<ButtonPress-1>", start_move)
    w.bind("<B1-Motion>", do_move)
    w.bind("<Button-3>", lambda e: m.post(e.x_root, e.y_root))
    for child in w.winfo_children(): bind_all(child)

bind_all(f)
root.mainloop()