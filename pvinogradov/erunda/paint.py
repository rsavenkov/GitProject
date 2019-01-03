from tkinter import *
from tkinter import ttk

canvas_width = 700
canvas_heigth = 500
brush_size = 3
color = 'black'

def paint(event):
    global brush_size
    global color
    x1 = event.x - brush_size
    x2 = event.x + brush_size
    y1 = event.y - brush_size
    y2 = event.y + brush_size
    w.create_oval(x1, y1, x2, y2,
                   fill=color, outline=color )

def brush_size_change(new_size):
    global brush_size
    brush_size = new_size

def color_change(new_color):
    global color
    color = new_color 
    
 
root = Tk()
root.title('Paint на  Python')

w = Canvas(root, width=canvas_width,
            height=canvas_heigth, bg='white')
w.bind('<B1-Motion>', paint)
red_btn = ttk.Button(text='красный', width=10,
                    command=lambda:color_change('red'))
red_btn1 = ttk.Button(text='green', width=10,
                    command=lambda:color_change('green'))
red_btn2 = ttk.Button(text='ластик', width=10,
                    command=lambda:color_change('white'))
red_btn3 = ttk.Button(text='Удалить все', width=20,
                    command=lambda:w.delete('all'))


five_btn = ttk.Button(text="2", width=10,
            command=lambda: brush_size_change(2))
five_btn1 = ttk.Button(text="5", width=10,
            command=lambda: brush_size_change(5))
five_btn2 = ttk.Button(text="8", width=10,
            command=lambda: brush_size_change(8))
five_btn3 = ttk.Button(text="12", width=20,
            command=lambda: brush_size_change(15))

w.grid(row=2, column=0, columnspan=7, 
padx=5, pady=5, sticky=E+W+S+N)
w.columnconfigure(6, weight=1) 
w.rowconfigure(2,weight=1)
red_btn.grid(row=0, column=1)
red_btn1.grid(row=0, column=2)
red_btn2.grid(row=0, column=3)
red_btn3.grid(row=0, column=4)
five_btn.grid(row=1, column=1)
five_btn1.grid(row=1, column=2)
five_btn2.grid(row=1, column=3)
five_btn3.grid(row=1, column=4)

root.mainloop()
