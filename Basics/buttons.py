from tkinter import *


root = Tk()


def callme():
    print('Hello Dear')

root.title("Frame")
f = Frame(root, width=300, height=110,  background='lime')
xf = Frame(f, relief=GROOVE, borderwidth=2)
Label(xf, text='You shot him', background='pink').pack(pady=10)
Button(xf, text="He's deed", cursor='hand2', border=5, borderwidth=5, background='green', command=callme).pack(side=LEFT, padx=5, pady=8)
Button(xf, text="He's completely dead", command=root.quit).pack(side=RIGHT, padx=5, pady=8)
xf.place(relx=0.01, rely=0.125, anchor=NW)
Label(f, text='self-defence agains fruit').place(relx=.06, rely=0.125, anchor=W)
f.pack()


root.mainloop()