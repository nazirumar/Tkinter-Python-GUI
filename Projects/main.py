from tkinter import *
import cv2 as cv
from tkinter import filedialog
from PIL import ImageTk, Image

def openfile():
        filename = filedialog.askopenfilename(title ='"pen')
        print(filename)
        return filename

def open_img():
    x = openfile()
    img = Image.open(x)
    img = img.resize((250, 250))
    img = ImageTk.PhotoImage(img)
    panel = Label(image=img)
    panel.image = img
    panel.pack()

class ImageEdit():
    def __init__(self):
        self.root = Tk()
        self.root.geometry("700x500")
        self.root.title("Image Editor")
        self.root.configure(bg='')
        f = Frame(self.root, relief=RAISED, borderwidth=2, bg='red', padx=10, pady=10)
        Label(f,  text="Nazbeen Photo Editor", font=("Arial Bold", 27)).pack()
        Message(f, text="The Message widget provides a convenient way to present multi-line text.You can use onefont and one foreground background color combination for the complete message. An example using this widget is shown in figure 4.17.The widget has the standard widget methods").pack(ipadx=30)
        f.pack(fill=X)
        Button(f, text='Upload', command=open_img).pack(pady=10, side=LEFT) 


if __name__ == '__main__':
    
    ImageEdit().root.mainloop()
        
    