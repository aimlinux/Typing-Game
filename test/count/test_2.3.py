import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.animation as animation

root = tk.Tk()
root.geometry("600x300")

# MatplotlibのFigureを作成
fig = Figure(figsize=(6, 6), dpi=100)
ax = fig.add_subplot(111)
ax.set_aspect('equal')
ax.axis('off')

# 初期フォントサイズ
initial_font_size = 180

# アニメーションの初期化
font_size = initial_font_size
font_name = "Yu Gothic"
font_weight = "bold"
font = (font_name, font_size, font_weight)
num_text = 5

t1 = ax.text(0.5, 0.5, str(num_text), ha='center', va='center', fontdict={'fontname' : font_name, 'fontsize' : font_size, 'fontweight' : font_weight})

def init():
    return t1,

def update(num):
    global font_size
    global num_text
    
    if num_text == 5:
        if font_size == 0:
            num_text = 4
            font_size = initial_font_size
        else:
            font_size = font_size - 2
            t1.set_fontsize(font_size)
            t1.set_text(str(num_text))
            
    elif num_text == 4:
        if font_size == 0:
            num_text = 3
            font_size = initial_font_size
        else:
            font_size = font_size - 2
            t1.set_fontsize(font_size)
            t1.set_text(str(num_text))
            
    elif num_text == 3:
        if font_size == 0:
            num_text = 2
            font_size = initial_font_size
        else:
            font_size = font_size - 2
            t1.set_fontsize(font_size)
            t1.set_text(str(num_text))
            
    elif num_text == 2:
        if font_size == 0:
            num_text = 1
            font_size = initial_font_size
        else:
            font_size = font_size - 2
            t1.set_fontsize(font_size)
            t1.set_text(str(num_text))
            
    elif num_text == 1:
        if font_size == 0:
            num_text = "スタート"
            font_size = initial_font_size
        else:
            font_size = font_size - 2
            t1.set_fontsize(font_size)
            t1.set_text(str(num_text))
        
    elif num_text == "スタート":
        if font_size == 0:
            # カウント終了
            root.after(400, root.destroy)  # 400ミリ秒後にウィンドウを閉じる
        else:
            font_size = font_size - 2
            t1.set_fontsize(font_size)
            t1.set_text(str(num_text))
        
    return t1,

# MatplotlibのFigureをTkinterウィンドウに埋め込む
canvas = FigureCanvasTkAgg(fig, master=root)
canvas_widget = canvas.get_tk_widget()
canvas_widget.pack()

ani = animation.FuncAnimation(fig, update, init_func=init, interval=7, frames=10)

root.mainloop()