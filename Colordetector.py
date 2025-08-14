import tkinter as tk
import pyautogui
import pyperclip
from pynput.keyboard import Listener,Key



def color():
    global x , y
    x, y = pyautogui.position()
    s = pyautogui.pixel(x,y)
    s1 = '#{:02x}{:02x}{:02x}'.format(s[0], s[1], s[2])
    f = f"{s},{s1}"
    l.delete("1.0", tk.END)
    l.insert("1.0", str(f))
    root.after(100, color)
    return s , s1

def copy():
    t = l.get("1.0", tk.END).strip()
    pyperclip.copy(t)
def copy2():
    s,s1 =color()
    t = s
    pyperclip.copy(t)
def copy3():
    s, s1 = color()
    t = s1
    pyperclip.copy(t)

def press(key):
    try:
        if key.char == 'c':
            copy()
        elif key.char == 'a':
            copy2()
        elif key.char == 's':
            copy3()

    except AttributeError:
        if key == Key.esc:
            root.quit()
        pass

root = tk.Tk()
root.title(" ")
width_of_calculator = round(root.winfo_screenwidth()/5.96)
height_of_calculator = round(root.winfo_screenheight()/24.54)
root.geometry(f"{width_of_calculator}x{height_of_calculator}")


l = tk.Text(root,width=20,height=1,bg = 'light grey',font=("Haettenschweiler", 30),fg= '#616060')
l.grid(row = 0 , column=0)


color()

Listener = Listener(on_press=press)
Listener.start()

root.mainloop()