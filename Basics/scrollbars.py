from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Scrollbar')

list = Listbox(root, height=6, width=15, bg='green')
scroll = Scrollbar(root, command=list.yview)
list.configure(yscrollcommand=scroll.set)
list.pack(side=LEFT)
scroll.pack(side=RIGHT, fill=Y)
for item in range(30):
    list.insert(END, item)

root.mainloop()