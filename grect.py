import tkinter as tk



class myapps:
    def __init__(self,root:tk.Tk):
        self.root=root
        self.root.title("rectangle")
        self.root.geometry("640x480")
        self.root.configure(background="black")
        self.canvas=tk.Canvas(background="black",width=640,height=480)
        self.canvas.pack(padx=0,pady=0)
        self.colors=["white","black"]
        c=self.canvas
        for a in range(12):
            aa=a *20
            aaa=640-aa
            aaaa=480-aa
            b=self.colors[a & 1]
            c.create_rectangle(aa,aa,aaa,aaaa,fill=b)
    




root=tk.Tk()
apps=myapps(root)
root.mainloop()