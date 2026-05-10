import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import os

DB, photos, idx = "last_img.txt", [], 0

def tampilkan():
    global idx
    if photos:
        path = photos[idx % len(photos)]
        if os.path.exists(path):
            img = Image.open(path)
            img.thumbnail((300, 300))
            img_tk = ImageTk.PhotoImage(img)
            lbl.config(image=img_tk, text="")
            lbl.image = img_tk
            idx += 1
    root.after(5000, tampilkan) 

def tambah():
    paths = filedialog.askopenfilenames(filetypes=[("Images", "*.png *.jpg *.jpeg")])
    if paths:
        photos.extend(paths)
        with open(DB, "w") as f: f.write(",".join(photos))
        if len(photos) == len(paths): tampilkan()

root = tk.Tk()
root.overrideredirect(True)
root.attributes("-topmost", True, "-transparentcolor", "#121212")
root.config(bg='#121212')

lbl = tk.Label(root, text="Klik Kanan\nTambah Foto", bg="#1e1e1e", fg="white", padx=5, pady=5)
lbl.pack(padx=10, pady=10)
lbl.bind("<ButtonPress-1>", lambda e: setattr(root, 'x', e.x) or setattr(root, 'y', e.y))
lbl.bind("<B1-Motion>", lambda e: root.geometry(f"+{root.winfo_x()+(e.x-root.x)}+{root.winfo_y()+(e.y-root.y)}"))

menu = tk.Menu(root, tearoff=0)
menu.add_command(label="Tambah Foto", command=tambah)
menu.add_command(label="Clear", command=lambda: (photos.clear(), open(DB, 'w').close(), lbl.config(image='', text="Kosong")))
menu.add_command(label="Exit", command=root.destroy)
lbl.bind("<Button-3>", lambda e: menu.post(e.x_root, e.y_root))

if os.path.exists(DB):
    photos = [p for p in open(DB).read().split(",") if os.path.exists(p)]
    tampilkan()

root.mainloop()