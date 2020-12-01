from tkinter import Tk,Button,PhotoImage,Toplevel
window=Tk()
window.geometry("200x100")
window.resizable(False,False)


def tu():
    img=Toplevel(window)
    img.title("ex")
    img.geometry("100x100")
    img.resizable(False,False)
    Button(img,image=a).pack(side="left")


def td():
    img=Toplevel(window)
    img.title("ex")
    img.geometry("100x100")
    img.resizable(False,False)
    Button(img,image=b).pack(side="left")

a=PhotoImage(file="./a.png")
Button(window,image=a,command=tu).pack(side="left")

b=PhotoImage(file="./b.png")
Button(window,image=b,command=td).pack(side="right")

window.mainloop()
