from tkinter import *
from tkinter import messagebox


def clicked():
 messagebox.showinfo('Я открылся', 'Привет, исправьте н/а пожалуйста:) И проверьте лекции:)')


window = Tk()
window.title("")
window.geometry('600x400')
btn = Button(window, text='Нажмите для продолжения', command=clicked)
btn.grid(column=0, row=0)
window.mainloop()