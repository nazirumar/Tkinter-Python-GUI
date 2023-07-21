from tkinter import *
import Pmw

root = Tk()
root.option_readfile('Projects/optionDB.txt')
balloon = Pmw.Balloon(root)

frame = Frame(root)
frame.pack(padx=10, pady=5)

def buttonPress(btn):
 print('The "%s" button was pressed' % btn)
 
def defaultKey(event):
    buttonBox.invoke()

buttonBox = Pmw.ButtonBox(root, labelpos='nw', label_text='ButtonBox:')
buttonBox.pack(fill=BOTH, expand=1, padx=10, pady=10)
buttonBox.add('OK', command = lambda b='ok': buttonPress(b))
buttonBox.add('Apply', command = lambda b='apply': buttonPress(b))
buttonBox.add('Cancel', command = lambda b='cancel': buttonPress(b))
buttonBox.add('Info', command = lambda b='info': buttonPress(b))
buttonBox.setdefault('OK')
root.bind('<Return>', defaultKey)
root.focus_set()
buttonBox.alignbuttons()

root.mainloop()