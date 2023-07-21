from tkinter import *


root = Tk()

Label(root, text="I mean, it's a little confusing for me when you say dog kennel if you want a mattres. why not just mattress ?", wraplength=300, justify=LEFT).pack(pady=10)


f1 = Frame(root)
Label(f1, text="it's not working, we need more!", relief=RAISED).pack(side=LEFT, padx=5)
Label(f1, text="I'm note coming out!", relief=SUNKEN).pack(side=LEFT, padx=5)
f1.pack()


f2 = Frame(root)
for bitmap, rlf in [ ('woman',RAISED),('mensetmanus',SOLID), ('terminal',SUNKEN), ('escherknot',FLAT),('calculator',GROOVE),('letters',RIDGE)]:
    Label(f2, bitmap='@bitmaps/%s' % bitmap, relief=rlf).pack(side=LEFT, padx=5)

f2.pack()


root.mainloop()