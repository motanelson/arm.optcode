import tkinter as tk



class myapps:
    def __init__(self,root:tk.Tk,titles:str,widths:int,heights:int,backgrounds:str,colors:str,divs:int):
        self.root=root
        self.root.title(titles)
        self.root.geometry(str(widths)+"x"+str(heights))
        self.root.configure(background=backgrounds)
        self.canvas=tk.Canvas(background=backgrounds,width=widths,height=heights)
        self.canvas.pack(padx=0,pady=0)
        self.colors=colors
        self.divsx=widths//divs//2
        self.divsy=heights//divs//2
        c=self.canvas
        counter=0
        for a in range(divs):
            aa=a * self.divsx
            aa1=a * self.divsy
            aaa=widths-aa
            aaaa=heights-aa1
            b=self.colors[counter]
            c.create_rectangle(aa,aa1,aaa,aaaa,fill=b)
            counter=counter+1
            if counter>len(self.colors)-1:
                counter=0
    



def starts(titles:str,widths:int,heights:int,backgrounds:str,colors:str,divs:int):
    root=tk.Tk()
    apps=myapps(root,titles,widths,heights,backgrounds,colors,divs)
    root.mainloop()

colors=["white","black"]
titles="rectangles"
widths=640
heights=480
backgrounds="black"
divs=12
starts(titles,widths,heights,backgrounds,colors,divs)