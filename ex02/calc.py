import tkinter as tk
import tkinter.messagebox as tkm


def button_click(event):
    btn = event.widget
    num = btn["text"]
    tkm.showinfo("", f"{num}のボタンがクリックされました")


root = tk.Tk()
root.title("tk")
root.geometry("300x500")

"""
button0 = tk.Button(root, text="0", width=4, height=2, font=("", "30", ""))
button1 = tk.Button(root, text="1", width=4, height=2, font=("", "30", ""))
button2 = tk.Button(root, text="2", width=4, height=2, font=("", "30", ""))
button3 = tk.Button(root, text="3", width=4, height=2, font=("", "30", ""))
button4 = tk.Button(root, text="4", width=4, height=2, font=("", "30", ""))
button5 = tk.Button(root, text="5", width=4, height=2, font=("", "30", ""))
button6 = tk.Button(root, text="6", width=4, height=2, font=("", "30", ""))
button7 = tk.Button(root, text="7", width=4, height=2, font=("", "30", ""))
button8 = tk.Button(root, text="8", width=4, height=2, font=("", "30", ""))
button9 = tk.Button(root, text="9", width=4, height=2, font=("", "30", ""))
"""

r, c = 0, 0

for num in range(9, -1, -1):
    button = tk.Button(root, text=f"{num}",
                       width=4, height=2, font=("", "30", ""))
    button.grid(row=r, column=c)
    button.bind("<1>", button_click)
    c += 1
    if c % 3 == 0:
        r += 1
        c = 0


root.mainloop()
