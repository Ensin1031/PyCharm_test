'''
Вычисление Дискриминанта
'''

from math import *
from tkinter import *


def setwindow(root):
    root.title('Окно программы')
    root.resizable(False, False)
    w = 800
    h = 600
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    x = int(ws / 2 - w / 2)
    y = int(hs / 2 - h / 2)
    root.geometry('{0}x{1}+{2}+{3}'.format(w, h, x, y))


def resbt(event=False):
    global ena
    global enb
    global enc
    global lr0
    global lr
    try:
        d = (float(enb.get()) ** 2 - 4 * float(ena.get()) * float(enc.get()))
        lr0.config(text=('Дискриминант =' + str(d)))
        if d > 0:
            x1 = (-float(enb.get()) + sqrt(d)) / (2 * float(ena.get()))
            x2 = (-float(enb.get()) - sqrt(d)) / (2 * float(ena.get()))
            lr.config(text=('x1 =' + str(x1) + '\nx2 =' + str(x2)))
        elif d == 0:
            x = -float(enb.get()) / 2 * float(ena.get())
            lr.config(text=('x =' + str(x)))
        else:
            lr.config(text='Корней нет')
    except ValueError:
        lr.config(text='Введите корректные значения!')


tr = Tk()
setwindow(tr)
l0 = Label(tr, text='Вычисление квадратных корней\nax^2 + bx + c = 0', font='Arial 20')
la = Label(tr, text='Введите a:', font='Arial 20')
lb = Label(tr, text='Введите b:', font='Arial 20')
lc = Label(tr, text='Введите c:', font='Arial 20')
ena = Entry(tr, font='Arial 20')
enb = Entry(tr, font='Arial 20')
enc = Entry(tr, font='Arial 20')
bt = Button(tr, font='Arial 20', text='Вычислить корни', command=resbt)
lr0 = Label(tr, font='Arial 20')
lr = Label(tr, font='Arial 20')

ena.bind('<Return>', resbt)
enb.bind('<Return>', resbt)
enc.bind('<Return>', resbt)

l0.place(relx=0.5, rely=0.01, anchor='n')
la.place(relx=0.4, rely=0.2, anchor='ne')
ena.place(relx=0.4, rely=0.2, anchor='nw')
lb.place(relx=0.4, rely=0.3, anchor='ne')
enb.place(relx=0.4, rely=0.3, anchor='nw')
lc.place(relx=0.4, rely=0.4, anchor='ne')
enc.place(relx=0.4, rely=0.4, anchor='nw')
bt.place(relx=0.5, rely=0.5, anchor='n')
lr0.place(relx=0.5, rely=0.6, anchor='n')
lr.place(relx=0.5, rely=0.7, anchor='n')

tr.mainloop()
