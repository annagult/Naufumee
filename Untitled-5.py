from tkinter import *
from tkinter.ttk import Radiobutton


def clicked():
 lbl.configure(text=selected.get())


window = Tk()
window.title("А я не окно")
window.geometry('600x400')
selected = IntVar()

rad1 = Radiobutton(window,text='Первый', value=1, variable=selected)
rad1.grid(column=0, row=0)

rad2 = Radiobutton(window,text='Второй', value=2, variable=selected)
rad2.grid(column=1, row=0)

rad3 = Radiobutton(window,text='Третий', value=3, variable=selected)
rad3.grid(column=2, row=0)

btn = Button(window, text="Клик", command=clicked)
btn.grid(column=3, row=0)

lbl = Label(window)
lbl.grid(column=0, row=1)

window.mainloop()
