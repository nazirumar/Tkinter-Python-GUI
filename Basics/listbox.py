from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('List Box')

list = Listbox(root, width=15)
list.pack()
for i in range (20):
    list.insert("end", "Item "+str(i))


root.mainloop()