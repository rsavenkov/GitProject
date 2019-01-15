from tkinter import  *


def exitPressButton():
    print("окей окей...")
    root.quit()

def pressAnyOtherMenuItem():
    print('Print any other menu item!')

root=Tk()

menu=Menu(root)
root.config(menu=menu)

subMenu = Menu(menu)
menu.add_cascade(label="Файл", menu=subMenu)
subMenu.add_command(label="Новый проект...", command=doNothing)
subMenu.add_command(label="Новый...",command=doNothing)
subMenu.add_separator()
subMenu.add_command(label="Выход", command=exitPressButton)

editMenu= Menu(menu)
menu.add_cascade(label="Изменить ",menu=editMenu)
editMenu.add_command(label="Готово",command=doNothing)

editMenu==Menu(menu)
menu.add_cascade(label="Вырезать",menu=editMenu)


root.mainloop()