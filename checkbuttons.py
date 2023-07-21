from tkinter import *

root = Tk()
root.geometry('500x300')
root.title('Radiobutton')
f = Frame(root, width=400, height=210, pady=20, padx=20, background='blue',)


var = IntVar()
for castmember, row, col, status in [
    ('John Cleese', 0,0,NORMAL), ('Eric Idle', 0,1,NORMAL),
    ('Graham Chapman', 1,0,DISABLED), ('Terry Jones', 1,1,NORMAL),
    ('Michael Palin',2,0,NORMAL), ('Terry Gilliam', 2,1,NORMAL)]:
        setattr(var, castmember, IntVar())
        Checkbutton(f, text=castmember, state=status, anchor=W,
        variable = getattr(var, castmember)).grid(row=row, column=col, sticky=W,)

f.pack()


root.mainloop()