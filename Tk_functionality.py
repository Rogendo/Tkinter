import tkinter as tk
from tkinter import messagebox

class MyGUI:
    def __init__(self):
        self.root=tk.Tk()

        self.menu=tk.Menu(self.root)

        self.filemenu=tk.Menu(self.menu,tearoff=0)
        self.filemenu.add_command(label="close without question",command=exit)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Exit",command=self.on_close)
        self.menu.add_cascade(menu=self.filemenu,label="File")
        self.root.config(menu=self.menu)

        self.label=tk.Label(self.root,text="your message",font=("Arial",16))
        self.label.pack(padx=10,pady=10)

        self.textbox=tk.Text(self.root,height=5,font=("Arial",16))
        self.textbox.pack(padx=10,pady=10)

        self.check_state=tk.IntVar()

        self.checkbx=tk.Checkbutton(self.root,text="show message box",font=("Arial",16),variable=self.check_state)
        self.checkbx.pack(padx=10,pady=10)

        self.button=tk.Button(self.root,text="show message",font=("Arial",16),command=self.show_message)
        self.button.pack(padx=10,pady=10)

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