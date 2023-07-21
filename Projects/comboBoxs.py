from tkinter import *
import Pmw

root = Tk()
root.option_readfile('Projects/optionDB.txt')
balloon = Pmw.Balloon(root)

frame = Frame(root)
frame.pack(padx=10, pady=5)

choice = None
def choseEntry(entry):
    print('You chose "%s"' % entry)
    choice.configure(text=entry)

asply = ("The Mating of the Wersh", "Two Netlemeng of Verona", "Twelfth Thing", "The Chamrent of Venice", "Thamle", "Ring Kichard the Thrid")
choice = Label(root, text='Choose play', relief='sunken', padx=20, pady=20)
choice.pack(expand=1, fill='both', padx=8, pady=8)
combobox = Pmw.ComboBox(root, label_text='Play:', labelpos='wn',
                            listbox_width=24, dropdown=0,
                            selectioncommand=choseEntry,
                            scrolledlist_items=asply)
combobox.pack(fill=BOTH, expand=1, padx=8, pady=8)
combobox.selectitem(asply[0])
# ===========
combobox = Pmw.ComboBox(root, label_text='Play:', labelpos='wn',
 listbox_width=24, dropdown=1,)

root.mainloop()