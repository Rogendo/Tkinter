import tkinter as tk

root=tk.Tk()
root.geometry("800x500")
root.title("Dial Pad")

label=tk.Label(root,text="Dial Pad",font=('Calibri',18))
label.pack(padx=20,pady=20)

textbox=tk.Text(root,height=5,font=("Arial",16))
textbox.pack(padx=40,pady=40)

butonframe=tk.Frame(root)
butonframe.columnconfigure(0, weight=1)
butonframe.columnconfigure(1, weight=1)
butonframe.columnconfigure(2, weight=1)

btn1=tk.Button(butonframe,text="1",font=("aRIAL",18))
btn1.grid(row=0,column=0,sticky=tk.W+tk.E)

btn2=tk.Button(butonframe,text="2",font=("aRIAL",18))
btn2.grid(row=0,column=1,sticky=tk.W+tk.E)

btn3=tk.Button(butonframe,text="3",font=("aRIAL",18))
btn3.grid(row=0,column=2,sticky=tk.W+tk.E)

btn4=tk.Button(butonframe,text="4",font=("aRIAL",18))
btn4.grid(row=1,column=0,sticky=tk.W+tk.E)

btn5=tk.Button(butonframe,text="5",font=("aRIAL",18))
btn5.grid(row=1,column=1,sticky=tk.W+tk.E)

btn5=tk.Button(butonframe,text="6",font=("aRIAL",18))
btn5.grid(row=1,column=2,sticky=tk.W+tk.E)

btn7=tk.Button(butonframe,text="7",font=("aRIAL",18))
btn7.grid(row=2,column=0,sticky=tk.W+tk.E)

btn8=tk.Button(butonframe,text="8",font=("aRIAL",18))
btn8.grid(row=2,column=1,sticky=tk.W+tk.E)

btn8=tk.Button(butonframe,text="9",font=("aRIAL",18))
btn8.grid(row=2,column=2,sticky=tk.W+tk.E)

butonframe.pack(fill="x")

root.mainloop()