import tkinter as tk
from tkinter import messagebox

class MyGUI:
    def __init__(self):
        self.root=tk.Tk()
        self.root.title("cVc")
        self.root.geometry("800x500")
        self.menu=tk.Menu(self.root)

        self.filemenu=tk.Menu(self.menu,tearoff=0)
        self.filemenu.add_command(label="New Project",command=exit)
        self.filemenu.add_command(label="New...",command=exit)
        self.filemenu.add_command(label="New Scratch File",command=exit)
        self.filemenu.add_command(label="Open...",command=exit)
        self.filemenu.add_command(label="Save...",command=exit)

        self.filemenu.add_command(label="Save As",command=exit)
        self.filemenu.add_command(label="Open Recent",command=exit)
        self.filemenu.add_command(label="Settings",command=exit)
        self.filemenu.add_command(label="Export...",command=exit)
        self.filemenu.add_command(label="Print...",command=exit)
        self.filemenu.add_command(label="close without question",command=exit)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Exit",command=self.on_close)
        self.menu.add_cascade(menu=self.filemenu,label="File")

        self.editmenu=tk.Menu(self.menu,tearoff=0)
        self.editmenu.add_command(label="Undo...",command=exit)
        self.editmenu.add_command(label="Redo...",command=exit)
        self.editmenu.add_command(label="Cut...",command=exit)
        self.editmenu.add_command(label="Copy",command=exit)
        self.editmenu.add_command(label="Paste",command=exit)
        self.editmenu.add_command(label="Delete",command=exit)
        self.editmenu.add_command(label="Find",command=exit)
        self.editmenu.add_command(label="Select All",command=exit)
        self.menu.add_cascade(menu=self.editmenu,label="Edit")

        self.viewmenu=tk.Menu(self.menu,tearoff=0)
        self.menu.add_cascade(menu=self.viewmenu,label="View")
        self.viewmenu.add_command(label="Window",command=exit)







        self.root.config(menu=self.menu)

        self.label=tk.Label(self.root,text="your canvas",font=("Arial",16))
        self.label.pack(padx=10,pady=10)

        self.textbox=tk.Text(self.root,height=20,font=("Arial",16))
        self.textbox.pack(padx=20,pady=20)



        self.root.protocol("WM_DELETE_WINDOW",self.on_close)

        self.root.mainloop()

    def show_message(self):
        # print("hello world")
        # print(self.check_state.get())
        if self.check_state.get()==0:
            print(self.textbox.get('1.0',tk.END))
        else:
            messagebox.showinfo(title="Message",message=self.textbox.get('1.0',tk.END))

    def on_close(self):
        # print("bye")
        if messagebox.askyesno(title="Quit?",message="Are you sure you want to exit?"):

            self.root.destroy()


MyGUI()