from tkinter import *

root = Tk()
root.geometry('500x300')
root.title('Message')



Message(root, text="Exactly. It's my belief that these sheep are laborin' "
"under the misapprehension that they're birds. Observe their "
"be'avior. Take for a start the sheeps' tendency to 'op about "
"the field on their 'ind legs. Now witness their attempts to "
"fly from tree to tree. Notice that they do not so much fly "
"as...plummet.", bg='royalblue', fg='ivory', padx=20, pady=20,
relief=GROOVE).pack(padx=10, pady=10)


root.mainloop()