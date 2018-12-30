 from tkinter import * # 
from tkinter import messagebox #
from tkinter import ttk #
 
root = Tk()
root.title('калькулятор')  
# логика
def calc(key):
    global memory
    if key == "=":
# проверка на ввод
        str1 = "//%-+1234567890./*"
        if calc_entry.get()[0] not in str1:
            calc_entry.insert(END, " Первый символ не число")
            messagebox.showerror("Ошибка!!! вы ввели не число")
#счет
        try:
            result = eval(calc_entry.get())
            calc_entry.delete(0, END)
            calc_entry.insert(END, str(result))
        except:
            calc_entry.insert(END, " Ошибка!")
            messagebox.showerror('Ошибка', 'проверь правельность данных')
# оцистка поля вывода если нажато 'c'
    elif key == "c": 
        calc_entry.delete(0, END)
# смена -+
    elif key == '-/+':
        if '=' in calc_entry.get():
            calc_entry.delete(0, END)
        try :
            if calc_entry.get()[0] == '-':
                calc_entry.delete(0)
            else:
                calc_entry.insert(0, '-')
        except IndexError:
            pass
    else:
        if '=' in calc_entry.get():
            calc_entry.delete(0, END)
        calc_entry.insert(END, key)                 

# наши кнопки
bttn_list = [
    '7', '8', '9', '+', '-',
    '4', '5', '6', '*', '/',
    '1', '2', '3', '-/+', '=',
    '0', '.', 'c', '//', '%',
]
r = 1
c = 0
for i in bttn_list: 
    cmd=lambda x = i:calc(x)
    ttk.Button(root, text=i, command=cmd    ).grid(row=r, column=c, sticky=E)
    c += 1
# расстановка окон по 4 в строке
    if c > 4: 
        c = 0
        r += 1
# создание окна вывода 
calc_entry = Entry(root, width = 50, borderwidth = 5   )
 # его длинна ( width = 50) и рамка (borderwidth = 5)   
calc_entry.grid(row=0, column=0, columnspan=5)
root.mainloop()