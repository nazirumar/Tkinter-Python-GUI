from tkinter import *

root = Tk()
root.geometry('500x300')
root.title('Radiobutton')
var = IntVar()
f = Frame(root, width=400, height=210, pady=20, padx=20, background='blue')

for text, value in [('Passion fruit', 1), ('Loganberries', 2),
        ('Mangoes in syrup', 3), ('Oranges', 4),
        ('Apples', 5),('Grapefruit', 6)]:
    Radiobutton(f, text=text, variable=var, selectcolor='green',  cursor='hand2', indicatoron=0, value=value).pack(anchor=W, fill=X, ipadx=30)
var.set(3)
f.place(relx=0.01, rely=0.125, anchor=NW)
Button(f, cursor='hand2', 
       background='red',  text='Quit', command=root.quit).pack(side=RIGHT, padx=5, pady=8)

f.pack()

root.mainloop()