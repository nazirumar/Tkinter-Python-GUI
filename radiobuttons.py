from tkinter import *

root = Tk()
root.geometry('500x300')
root.title('Radiobutton')
var = IntVar()
f = Frame(root, width=300, height=110, pady=10)

for text, value in [('Passion fruit', 1), ('Loganberries', 2),
        ('Mangoes in syrup', 3), ('Oranges', 4),
        ('Apples', 5),('Grapefruit', 6)]:
    Radiobutton(f, text=text, variable=var, value=value).pack(anchor=W)
var.set(3)
f.pack()


root.mainloop()