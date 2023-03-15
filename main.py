import tkinter as tk

root=tk.Tk()
root.geometry("800x500")
root.title("First GUI with tkinter")

label=tk.Label(root,text="Hello World",font=('Calibri',18))
label.pack(padx=20,pady=20)

textbox=tk.Text(root,height=10,font=("Arial",16))
textbox.pack(padx=40,pady=40)

myentry=tk.Entry(root)
myentry.pack(padx=10,pady=10)

button=tk.Button(root,text="Submit",font=("Arial",16))
button.pack(padx=10,pady=10)

root.mainloop()