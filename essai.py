import tkinter
def bomm():
    a.geometry("400x500")
    c=tkinter.Label(text="ok ok")
    a.config(bg="red")
    c.pack()
    

bg="cadetblue"
a=tkinter.Tk()
b=tkinter.Label(text="salut les nazes")
c=tkinter.Button(text="clik ici",command=bomm)
a.config(bg=bg)
c.pack()
b.pack()

a.mainloop()