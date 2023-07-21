from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.geometry('500x300')
root.title('Text')

f = Frame(root,  height=100, width=200, background='red')

text = Text(f)

# Scrollbar
scroll = Scrollbar(root, command=text.yview)
text.configure(yscrollcommand=scroll.set)

text.tag_configure('bold_italics', font=('Verdana', 12, 'bold', 'italic'))
text.tag_configure('big', font=('Verdana', 24, 'bold'))
text.tag_configure('color', foreground='blue', font=('Tempus Sans ITC', 14))
text.tag_configure('groove', relief=GROOVE, borderwidth=2)

text.insert(END, "markings makes implementation easy. The widget is complex and has many options and methods, so please refer to the full documentation for precise details. Some of the possible styles and embedded objects are shown in figure 4.18.")
text.tag_bind('bite', '<1>',
lambda e, t=text: t.insert(END, "I'll bite your legs off!"))
text.insert(END, 'Something up with my banter, chaps?\n')
text.insert(END, 'Four hours to bury a cat?\n', 'bold_italics')
text.insert(END, 'Can I call you "Frank"?\n', 'big')
text.insert(END, "What's happening Thursday then?\n", 'color')
text.insert(END, 'Did you write this symphony in the shed?\n', 'groove')
button = Button(text, text='I do live at 46 Horton terrace')
text.window_create(END, window=button)

# IMage Load
photo = PhotoImage(file='cfe0b14f4ad727b8ffe054c296339d17.png')
photo = photo.subsample(2, 2)
text.image_create(END, image=photo)
text.pack(side=RIGHT)
scroll.pack(side=RIGHT, fill=Y)
f.pack()


root.mainloop()