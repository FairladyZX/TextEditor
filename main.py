import os
from tkinter import*
from tkinter import filedialog,colorchooser,font
from tkinter .messagebox import *
from tkinter.filedialog import *


def openFile():
    fileOpen=filedialog.askopenfile(defaultextension=(".txt"))

    try:
        window.title(os.path.basename(fileOpen.name))
        textArea.delete(1.0,END)
        textArea.insert(1.0,fileOpen.read())

    except Exception:
        print("File did not open")

    finally:
        fileOpen.close()

def saveFile():
    fileSave=filedialog.asksaveasfile(defaultextension=(".txt"))

    if fileSave is None:
        return
    fileText=str(textArea.get(1.0,END))
    fileSave.write(fileText)
    fileSave.close()

def newFile():
    window.title("untitled")
    textArea.delete(1.0,END)

def print():
    showwarning("You are about to print something")

def closeFile():
    window.destroy()

def copy():
    textArea.event_generate("<<Copy>>")

def paste():
    textArea.event_generate("<<Paste>>")

def cut():
    textArea.event_generate("<<Cut>>")

def about():
    showinfo("My cat Goku just took a big shit!")

def fontType(*args):
    textArea.config(font=(fontName.get(),fontSizeSelection.get()))

def color():
    color=colorchooser.askcolor()
    textArea.config(fg=color[1])

window=Tk()
window.title("Text Program")


file=None
windowHeight=500
windowWidth=700

screenHeight=window.winfo_screenheight()
screenWidth=window.winfo_screenwidth()
x=int((screenHeight/2)-(windowHeight/2))
y=int((screenWidth/2)-(windowWidth/2))
window.geometry("{}x{}+{}+{}".format(windowWidth,windowHeight,y,x))

fontName=StringVar(window)
fontName.set("arial")
fontSize=StringVar(window)
fontSize.set("25")
textArea=Text(window, font=(fontName.get(), fontSize.get()))
scrollbar=Scrollbar(textArea)

window.grid_columnconfigure(0,weight=1)
window.grid_rowconfigure(0,weight=1)
textArea.grid(sticky=N+S+W+E)
scrollbar.pack(side=RIGHT,fill=Y)
textArea.config(yscrollcommand=scrollbar.set)

frame=Frame(window)
frame.grid()

colorButton=Button(frame, text="Color", command=color)
colorButton.grid(row=0,column=0)

fontNameSelection=OptionMenu(frame, fontName,*font.families(), command=fontType)
fontNameSelection.grid(row=0,column=1)

fontSizeSelection=Spinbox(frame, textvariable=fontSize, from_=1, to=100, command=fontType)
fontSizeSelection.grid(row=0,column=2)

menubar=Menu(window)
window.config(menu=menubar)

fileMenu=Menu(menubar)
menubar.add_cascade(label="File", menu=fileMenu)
fileMenu.add_command(label="Open", command=openFile)
fileMenu.add_command(label="Save", command=saveFile)
fileMenu.add_command(label="New", command=newFile)
fileMenu.add_command(label="Print", command=print)
fileMenu.add_separator()
fileMenu.add_command(label="Close", command=closeFile)

editMenu=Menu(menubar)
menubar.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Copy", command=copy)
editMenu.add_command(label="Cut", command=cut)
editMenu.add_command(label="Paste", command=paste)

aboutMenu=Menu(menubar)
menubar.add_cascade(label="About", menu=aboutMenu)
aboutMenu.add_command(label="Info", command=about)


window.mainloop()