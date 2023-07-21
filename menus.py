from tkinter import *

root = Tk()
root.geometry('500x300')
root.title('Menu')
f = Frame(root, relief=RAISED, borderwidth=2)
f.pack(fill=X)


def  makeCommandMenu():
    CmdBtn = Menubutton(f, text='menu', underline=0)
    CmdBtn.pack(side=LEFT, padx='2m')
    CmdBtn.menu = Menu(CmdBtn)
    CmdBtn.menu.add_command(label="Undo")
    CmdBtn.menu.entryconfig(0, state=DISABLED)
    CmdBtn.menu.add_command(label='New...', underline=0, )
    CmdBtn.menu.add_command(label='Open...', underline=0,)
    CmdBtn.menu.add_command(label='Wild Font', underline=0,
    font=('Tempus Sans ITC', 14))
    # CmdBtn.menu.add_command(bitmap="@bitmaps/RotateLeft")
    CmdBtn.menu.add('separator')
    CmdBtn.menu.add_command(label='Quit', underline=0,
    background='white', activebackground='green',
    command=CmdBtn.quit)
    CmdBtn['menu'] = CmdBtn.menu
    return CmdBtn
    
def  makeCascadeMenu():
    pass
def  makeCheckbuttonMenu():
    pass
def  makeRadiobuttonMenu():
    pass
def  makeDisabledMenu():
    pass

CmdBtn = makeCommandMenu()
# CasBtn = makeCascadeMenu()
# ChkBtn = makeCheckbuttonMenu()
# RadBtn = makeRadiobuttonMenu()
# NoMenu = makeDisabledMenu()
menubar = Menu()
# Insert the menubar in the main window.
root.config(menu=menubar)
root.mainloop()