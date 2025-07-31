import pyautogui as pg
import tkinter as tk
import pyperclip
from pynput.keyboard import Listener,Key

def update():
    global a1,a2
    x, y = pg.position()
    if x != a1 or y != a2:
        print(f"{x}, {y}")
        s = f" {x}, {y}"
        l.delete("1.0", tk.END)
        l.insert("1.0", s)
        a1, a2 = x, y
    root.after(100, update)
    return x , y
def copy():
    t = l.get("1.0", tk.END).strip()
    pyperclip.copy(t)

def press(key):
    try:
        if key.char == 'c':
            copy()

    except AttributeError:
        if key == Key.esc:
            root.quit()
        pass

root = tk.Tk()

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

width = round(screen_width/12.01)
height = round(screen_height/22.5)

root.geometry(f"{width}x{height}")
root.resizable(False,False)
root.title(" ")
l = tk.Text(root,width=10,height=1,bg = 'light grey',font=("Haettenschweiler", 30),fg= '#616060')
l.grid(row = 0 , column=0)

a1 , a2 = -1 , -1

update()

Listener = Listener(on_press=press)
Listener.start()

root.mainloop()