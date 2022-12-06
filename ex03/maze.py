import tkinter as tk
import maze_maker as mm
import tkinter.messagebox as tkm
import openpyxl as ox


def key_down(event):
    global key
    key = event.keysym


def key_up(event):
    global key
    key = ""


def main_proc():
    global cx, cy, mx, my, ms_count
    if key == "Up":
        my -= 1
    elif key == "Down":
        my += 1
    elif key == "Left":
        mx -= 1
    elif key == "Right":
        mx += 1
    # qまたはtまたはrボタンを押下すると、メッセージが出る。
    elif key == "q":
        tkm.showwarning("開発者からの警告", "ゲームをやめようとしないでください。")
    elif key == "t":
        mx = 13
        my = 7
        tkm.showerror("開発者からのメッセージ", "あなたはズルをしました。\nこのゲームを起動し直してください。")
    elif key == "r":
        mx = 1
        my = 1
        tkm.showinfo("開発者からのメッセージ", "ゲームをやり直します。")
    elif maze_lst[mx][my] == 1:  # 移動先が壁だったら
        if key == "Up":
            my += 1
        if key == "Down":
            my -= 1
        if key == "Left":
            mx += 1
        if key == "Right":
            mx -= 1

    cx, cy = mx*100+50, my*100+50
    canvas.coords("kokaton", cx, cy)
    root.after(100, main_proc)


# 処理部
if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん")
    canvas = tk.Canvas(root, width=1500, height=900, bg="black")
    canvas.pack()

    maze_lst = mm.make_maze(15, 9)
    # print(maze_lst)
    mm.show_maze(canvas, maze_lst)

    mx, my = 1, 1
    cx, cy = mx*100+50, my*100+50
    tori = tk.PhotoImage(file="./6.png")
    if mx == 13 and my == 7:
        tori = tk.PhotoImage(file="./6.png")
    canvas.create_image(cx, cy, image=tori, tag="kokaton")

    key = ""
    root.bind("<KeyPress>", key_down)
    root.bind("<KeyRelease>", key_up)
    main_proc()

    # 以下はエクセルファイル（スコア表）を生成する。
    wb = ox.Workbook()
    ws = wb.active
    wb.save(r"ex03/score.xlsx")

    root.mainloop()
