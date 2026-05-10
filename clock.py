import tkinter
from time import strftime

def perbarui():
    string_waktu = strftime('%H:%M:%S %p')
    sh_label.config(text=string_waktu)
    lb_utama.config(text=string_waktu)
    lb_utama.after(1000, perbarui)

def keluar(event):
    menu.post(event.x_root, event.y_root)


def start_move(event):
    root.x = event.x
    root.y = event.y

def do_move(event):
    x = root.winfo_pointerx() - root.x
    y = root.winfo_pointery() - root.y
    root.geometry(f"+{x}+{y}")

root = tkinter.Tk()

root.overrideredirect(True)
root.attributes('-topmost', True)
root.config(bg='#121212')
root.wm_attributes('-transparentcolor', '#121212')

# TAMPILAN
font_style = ('Sagoe UI Variable Display', 25, 'bold')
warna_utama = '#E0E0E0'
shadow = '#252525'

sh_label = tkinter.Label(root, font=font_style, bg='#121212', fg=shadow)
sh_label.place(x=13, y=13)

lb_utama = tkinter.Label(root, font=font_style, bg='#121212', fg=warna_utama)
lb_utama.pack(padx=10, pady=10)

# MENU
menu = tkinter.Menu(root, tearoff=0)
menu.add_command(label="Keluar", command=root.destroy)

lb_utama.bind('<Button-1>', start_move)
lb_utama.bind('<B1-Motion>', do_move)
lb_utama.bind('<Button-3>', keluar)

perbarui()
root.mainloop()