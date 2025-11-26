from tkinter import *
from tkinter.ttk import Combobox
from tkinter import ttk
from tkinter import messagebox
win = Tk();
win.title("ФИО автора")
win.geometry("400x300")

def clickRd():
    messagebox.showinfo("чекбоксик", "выбран чекбокс " + str(select.get()));
    
def readFile():
   file =  open('file').read()
   messagebox.showinfo("файл открыт", file)


def click():
    numget1 = int(num1.get())
    numget2 = int(num2.get())
    if znak.get() == "+":
        lbl.configure(text = numget1 + numget2)
    elif znak.get() == "-":
        lbl.configure(text = numget1 - numget2)
    elif znak.get() == "/":
        if numget2 == 0:
            lbl.configure(text="не")
        else:
            lbl.configure(text = numget1/numget2)
    elif znak.get() == "*":
        lbl.configure(text = numget1 * numget2)


lbl1 = Label()

notebook = ttk.Notebook(win)
notebook.pack(expand=True, fill='both', anchor='n')
tab1 = ttk.Frame(notebook)

tab2 = ttk.Frame(notebook)
tab3 = ttk.Frame(notebook)


notebook.add(tab1, text='         КАЛЬКУЛЯТОР               ')
notebook.add(tab2, text='           ЧЕКБОКСЫ             ')
notebook.add(tab3, text='               ФАЙЛ              ')
  

choices = ["+", "-", "*", "/"]
znak = Combobox(tab1, values=choices)
znak.place(x = 90, y = 20)
z = znak.get()

select = IntVar()

num1 = Entry(tab1, width=10)
num1.place(x = 10, y = 20)

num2 = Entry(tab1, width=10)
num2.place(x = 250, y = 20)

knopka = Button(tab1, width=15, text='Посчитать', command=click)
knopka.place(x = 200, y = 200, anchor='center')

knopka2 = Button(tab3, width=10, height=10, text='читать', command=readFile)
knopka2.place(x = 200, y=150, anchor='c')


lbl = Label(tab1, text="результат")
lbl.place(x = 200, y = 150, anchor='center')

rd1 = Radiobutton(tab2, text="первый", value=1, variable=select)
rd2 = Radiobutton(tab2, text="Второй", value=2, variable=select)
rd3 = Radiobutton(tab2, text="третий", value=3, variable=select)
rd1.grid(column=0, row=0)
rd2.grid(column=1, row=0)
rd3.grid(column=2, row=0)



knopka1 = Button(tab2, width=15, text="выбрать", command=clickRd)
knopka1.place(x=140, y=140)



win.mainloop()
