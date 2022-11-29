import tkinter as tk
import tkinter.messagebox as tkm
import math


def button_click(event):
    btn = event.widget
    num = btn["text"]
    if num == "=":
        siki = entry.get()
        res = eval(siki)
        entry.delete(0, tk.END)
        entry.insert(tk.END, res)

    elif num == "x":
        num="*"
        entry.insert(tk.END, num)
        
    elif num=="x^2":
        num="**2"
        entry.insert(tk.END,num)
    
    elif num=="√":
        num="**(1/2)"
        entry.insert(tk.END,num)
    
    elif num=="%":
        num="*0.01"
        entry.insert(tk.END,num)
    
    elif num=="÷":
        num="/"
        entry.insert(tk.END,num)

    else:
        # tkm.showinfo("", f"{num}のボタンがクリックされました")
        entry.insert(tk.END, num)


root = tk.Tk()
root.title("tk")
root.geometry("300x500")


entry = tk.Entry(root, justify="right", width=10, font=("", 40))
entry.grid(row=0, column=0, columnspan=4)


r, c = 2, 0

# 電卓表示用リスト
fig_list = [7, 8, 9, 4, 5, 6, 1, 2, 3, 0]

for num in fig_list:
    button = tk.Button(root, text=f"{num}",
                       width=4, height=1, font=("", "30", ""))
    if num == 0:
        button.grid(row=5, column=1)
        button.bind("<1>", button_click)
    else:
        button.grid(row=r, column=c)
        button.bind("<1>", button_click)
    c += 1
    if c % 3 == 0:
        r += 1
        c = 0

c+=1

operators = [".","+", "x","x^2", "√","%","÷","="]
for ope in operators:
    button = tk.Button(root, text=f"{ope}",
                        width=4, height=1, font=("", "30", ""))
    button.grid(row=r, column=c)
    button.bind("<1>", button_click)
    c += 1
    if c % 3 == 0:
        r += 1
        c = 0

root.mainloop()
