from Tkinter import *
import ttk
from tkFileDialog import askopenfile, asksaveasfile
from PIL import Image, ImageTk
import cv2
from ImageFilters import ImageFilters as IFil
import argparse as ap
import os

parser = ap.ArgumentParser()
parser.add_argument("-c", type = int, help ="App height", default = 768)
parser.add_argument("-w", type = int, help ="App width", default = 1366)
args = parser.parse_args()

app_height = args.c
app_width = args.w

src=  ''
dst = ''
global src
global dst

def Resize(image_addr):
    try:
        image = cv2.imread(image_addr)
        height, width = image.shape[:2]

        while height >= app_height:
            height = height/2.0
        while width >= app_width:
            width = width/2.0

        img = Image.open(image_addr)
        img = img.resize((int(width), int(height)), Image.ANTIALIAS)
        return img

    except AttributeError:
        return None

class Page(Frame):
    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)

    def show(self):
        self.lift()


home_font = ("arial", 12)

class HOMEPage(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        self.imageL = Label(self, text = 'Source Image', font = home_font, fg = "Red")
        self.imageL.pack(pady =5)

        self.image = Label(self, text = '', font = home_font, fg = "blue")
        self.image.pack(pady = 5)

        self.targetL = Label(self, text = 'Target', font = home_font, fg = "Red")
        self.targetL.pack(pady =5)

        self.target = Label(self, text = '', font = home_font, fg = "green")
        self.target.pack(pady =5)

        self.chooseButton = ttk.Button(self, text = "Choose Image", command = self.let_them_choose, width = 20)
        self.chooseButton.pack(pady =5)

        self.dest = ttk.Button(self, text = "Destination File", command = self.destfile, width = 20)
        self.dest.pack(pady =5)

        self.confirm = ttk.Button(self, text = "Confirm", command = self.finalise, width = 20)
        self.confirm.pack(pady =5)

        self.logo = ImageTk.PhotoImage(Resize("technicolor-logo.jpg"))
        self.LOGO = Label(self, image = self.logo)
        self.LOGO.pack(pady = 10)

        self.check_state()


    def check_state(self):
        if self.image['text'] == '' or self.target['text'] == '':
            self.confirm.config(state = 'disabled')
        else:
            self.confirm.config(state = 'normal')

    def let_them_choose(self):
        f = askopenfile()

        self.image['text'] = f.name
        self.check_state()

    def destfile(self):
        destination = asksaveasfile()
        self.target['text'] = destination.name
        self.check_state()

    def updateWorkSpace(self, origin):
        newImg = Resize(origin)
        workspace.photoimg = ImageTk.PhotoImage(newImg)
        workspace.panel['image'] = workspace.photoimg

    def finalise(self):
        workspace.enable_menu()
        src = self.image['text']
        dst = self.target['text']
        self.updateWorkSpace(src)
        workspace.show()

class workPage(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        self.menubar = Menu()
        self.test1Menu = Menu()

        self.menubar.add_cascade(label="More Filters", menu=self.test1Menu)
        self.test1Menu.add_command(label="RGV", command=self.testRGV)
        self.test1Menu.add_command(label="CMV", command=self.testCMV)
        self.test1Menu.add_command(label="Go Home", command=self.gobacknow)

        root.configure(menu=self.menubar)

        # Load the image in proper scale.
        self.intermediate = Image.open("sample.jpgtemp.png")
        self.photoimg = ImageTk.PhotoImage(self.intermediate)
        self.panel = Label(self, image = self.photoimg)
        self.panel.pack(pady = 20)

        self.alabel = Label(self, text = "Enter a floating point number (Only for Technicolor 1).")
        self.alabel.pack(pady = 10)
        self.scale = ttk.Entry(self)
        self.scale.pack(pady = 10)

        self.convert = ttk.Button(self, text = "Test", command = self.testnow)
        self.convert.pack(pady = 10)

        self.goback = ttk.Button(self, text = "<----", command = self.gobacknow)
        self.goback.pack(pady = 10)
        self.goback.place(x = 10, y = 10)

        self.enable_menu()

    def gobacknow(self):
        self.disable_menu()
        home.show()

    def enable_menu(self):
        self.menubar.entryconfig("More Filters", state="normal")
        #self.menubar.entryconfig(2, state="normal")

    def disable_menu(self):
        self.menubar.entryconfig("More Filters", state="disabled")
        #self.menubar.entryconfig(2, state="disabled")

    def testRGV(self):
        dst = home.target['text']
        src = home.image['text']
        IFil(src, dst).recolor_to_RGV()
        home.updateWorkSpace(dst)

    def testCMV(self):
        dst = home.target['text']
        src = home.image['text']
        IFil(src, dst).recolor_to_CMV()
        home.updateWorkSpace(dst)

    def testnow(self):
        dst = home.target['text']
        src = home.image['text']
        IFil(src, dst).recolor_to_RC(float(self.scale.get()))
        home.updateWorkSpace(dst)


class MainView(Frame):
    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)

        home = HOMEPage()
        workspace = workPage()

        global workspace
        global home

        self.container = Frame(self)
        self.container.pack(side = 'top', fill = 'both', expand = True)

        home.place(in_ = self.container, x = 0, y = 0, relwidth = 1, relheight = 1)
        workspace.place(in_ = self.container, x = 0, y = 0, relwidth = 1, relheight = 1)

        workspace.disable_menu()
        home.show()


if __name__ == '__main__':
    root = Tk()

    main = MainView(root)
    main.pack(side = 'top', fill = 'both', expand = True)

    root.wm_geometry(str(app_width)+'x'+str(app_height))
#    root.resizable(height = 0, width = 0)

    root.title('Technicolor')
    root.mainloop()
