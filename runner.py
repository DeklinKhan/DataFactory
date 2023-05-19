
from tkinter import *

class stopwatch():



    def close(self):
        self.root.destroy()



    def __init__(self):
        self.root=Tk()
        self.root.title("code runner")
        self.root.geometry("350x250")
        self.bt1 = Button(self.root,text="Start",command=self.start ,font=("Times 12 bold"),bg=("green"),height= 3, width=6)
        self.bt4 = Button(self.root, text="Exit", command=self.close,font=("Times 12 bold"),bg=("yellow"),height= 3, width=6)
        self.bt1.place(x=40,y=100)
        self.bt4.place(x=240,y=100)
        self.label1 = Label(self.root,text="press start after user input has been uploaded",font=("Times 12 bold"),bg='black', fg='white')
        self.label1.place(x=8,y=40)
        self.label2 = Label(self.root,text="please exit after powerbi has updated",font=("Times 12 bold"),bg='black', fg='white')
        self.label2.place(x=30,y=180)
        self.root.configure(bg='black')
        self.root.mainloop()

    def start(self):
        import combineduploader
a=stopwatch()