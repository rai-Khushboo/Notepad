from tkinter import*
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os

def newFile():
    global file
    root.title("Untitled-Notepad")
    file = None
    TextArea.delete(1.0 , END)

def openFile():
    global file
    file = askopenfilename(defaultextension=".txt" , filetypes=[("All Files", "*.*"),("Text Documents" , "*.txt")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + "-Notepad")
        TextArea.delete(1.0, END)
        f = open(file , "r")
        TextArea.insert(1.0 , f.read())
        f.close()


def saveFile():
    global file 
    if file == None:
        file = asksaveasfilename(initialfile="Untitled.txt" , defaultextension=".txt" , filetypes=[("All Files", "*.*"),("Text Documents" , "*.txt")])
        if file == "":
            file = None
        else:
            #save as a new file
            f = open(file , "w")
            f.write(TextArea.get(1.0 , END))
            f.close()

            root.title(os.path.basename(file) + "-Notepad")
            print("File Saved")
    else:
        #save the file
        f = open(file , "w")
        f.write(TextArea.get(1.0 , END))
        f.close()


def quitApp():
    root.destroy()

def cut():
    TextArea.event_generate("<<Cut>>")

def copy():
    TextArea.event_generate("<<Copy>>")

def paste():
    TextArea.event_generate("<<Paste>>")

def about():
    showinfo("Notepad","Notepad created by Khushboo")


if __name__ == '__main__':
    #basic tkinter setup
    root = Tk()
    root.title("Untitled - Notepad")
    # root.wm_iconbitmap("khusbu.ico")#for changing the feather icon
    root.geometry("644x788")


    #add text area of the notepad
    TextArea = Text(root, font="lucida 13")
    file = None
    TextArea.pack(expand=True ,fill=BOTH)

#FileMenu starts from here....:))
    #create a menu bar for the same
    MenuBar = Menu(root)#created horizontal menu
    FileMenu = Menu(MenuBar , tearoff=0)

    #To open new file
    FileMenu.add_command(label="New" , command=newFile)

    #to open already existing file
    FileMenu.add_command(label="Open" , command=openFile)

    #To save the current file
    FileMenu.add_command(label="Save" , command=saveFile)

    FileMenu.add_separator()
    FileMenu.add_command(label="Exit", command=quitApp)

    MenuBar.add_cascade(label="File" , menu=FileMenu)#placing all the menu into the file

#Edit menu starts from here
    EditMenu = Menu(MenuBar, tearoff=0)
    #adding feature of cut , copy and paste
    EditMenu.add_command(label="Cut" ,command=cut)
    EditMenu.add_command(label="Copy" ,command=copy)
    EditMenu.add_command(label="Paste" ,command=paste)

    MenuBar.add_cascade(label="Edit" , menu=EditMenu)

#Help menu
    HelpMenu = Menu(MenuBar , tearoff=0)
    HelpMenu.add_command(label="About Notepad" , command=about)
    MenuBar.add_cascade(label="Help" , menu=HelpMenu)

    root.config(menu=MenuBar)


    #adding scroll bar
    Scroll = Scrollbar(TextArea)
    Scroll.pack(side=RIGHT , fill=Y )
    Scroll.config(command=TextArea.yview)
    TextArea.config(yscrollcommand=Scroll.set)


root.mainloop()
