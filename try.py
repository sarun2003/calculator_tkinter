#################################################################
# Name: Sandip Thapa, Sarun Shrestha, Issac
# Date: November 3, 2023
# Description: The Recknor
#################################################################
from tkinter import *
# the main GUI
class MainGUI(Frame):

    # the constructor
    def __init__(self, parent):
        Frame.__init__(self, parent, bg="white")
        parent.attributes("-fullscreen", True)
        self.setupGUI()
    # sets up the GUI
    def setupGUI(self):
        # configure the rows and columns of the Frame to adjust to
        # the window
        # there are 6 rows (0 through 5)
        for row in range(6):
            Grid.rowconfigure(self, row, weight=1)
        # there are 4 columns (0 through 3)
        for col in range(4):
            Grid.columnconfigure(self, col, weight=1)
        self.display = Label(self, text="", anchor=E, bg="white", height=2, width=15, font=("TexGyreAdventor", 50))
        self.display.grid(row= 0, column = 0, columnspan = 4)
        #(
        img = PhotoImage(file="images-gif/lpr.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, activebackground="white", command= lambda:self.process("("))
        button.img = img
        button.grid(row=1, column=0, sticky=N+S+E+W)
        #(
        img = PhotoImage(file="images-gif/rpr.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, activebackground="white", command= lambda:self.process(")") )
        button.img = img
        button.grid(row=1, column=1, sticky=N+S+E+W)
        #AC
        img = PhotoImage(file="images-gif/clr.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, activebackground="white", command= lambda:self.process("AC") )
        button.img = img
        button.grid(row=1, column=2, sticky=N+S+E+W)
        # **
        img = PhotoImage(file="images-gif/pow.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, activebackground="white", command= lambda:self.process("**"))
        button.img = img
        button.grid(row=1, column=3, sticky=N+S+E+W)
        #7
        img = PhotoImage(file="images-gif/7.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, activebackground="white", command= lambda:self.process("7") )
        button.img = img
        button.grid(row=2, column=0, sticky=N+S+E+W)
        #8
        img = PhotoImage(file="images-gif/8.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, activebackground="white", command= lambda:self.process("8") )
        button.img = img
        button.grid(row=2, column=1, sticky=N+S+E+W)
        #9
        img = PhotoImage(file="images-gif/9.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, activebackground="white", command= lambda:self.process("9"))
        button.img = img
        button.grid(row=2, column=2, sticky=N+S+E+W)
        # /
        img = PhotoImage(file="images-gif/div.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, activebackground="white", command= lambda:self.process("/"))
        button.img = img
        button.grid(row=2, column=3, sticky=N+S+E+W)
        # 4 
        img = PhotoImage(file="images-gif/4.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, activebackground="white", command= lambda:self.process("4"))
        button.img = img
        button.grid(row=3, column=0, sticky=N+S+E+W)
        # 5
        img = PhotoImage(file="images-gif/5.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, activebackground="white", command= lambda:self.process("5"))
        button.img = img
        button.grid(row=3, column=1, sticky=N+S+E+W)
        # 6
        img = PhotoImage(file="images-gif/6.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, activebackground="white", command= lambda:self.process("6"))
        button.img = img
        button.grid(row=3, column=2, sticky=N+S+E+W)
        # *
        img = PhotoImage(file="images-gif/mul.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, activebackground="white", command= lambda:self.process("*"))
        button.img = img
        button.grid(row=3, column=3, sticky=N+S+E+W)
        # 1 
        img = PhotoImage(file="images-gif/1.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, activebackground="white", command= lambda:self.process("1"))
        button.img = img
        button.grid(row=4, column=0, sticky=N+S+E+W)
        # 2
        img = PhotoImage(file="images-gif/2.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, activebackground="white", command= lambda:self.process("2"))
        button.img = img
        button.grid(row=4, column=1, sticky=N+S+E+W)
        # 3 
        img = PhotoImage(file="images-gif/3.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, activebackground="white", command= lambda:self.process("3"))
        button.img = img
        button.grid(row=4, column=2, sticky=N+S+E+W)
        # -
        img = PhotoImage(file="images-gif/sub.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, activebackground="white", command= lambda:self.process("-"))
        button.img = img
        button.grid(row=4, column=3, sticky=N+S+E+W)
        # 0
        img = PhotoImage(file="images-gif/0.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, activebackground="white", command= lambda:self.process("0"))
        button.img = img
        button.grid(row=5, column=0, sticky=N+S+E+W)
        # .
        img = PhotoImage(file="images-gif/dot.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, activebackground="white", command= lambda:self.process("."))
        button.img = img
        button.grid(row=5, column=1, sticky=N+S+E+W)
        # = 
        img = PhotoImage(file="images-gif/eql.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, activebackground="white", command= lambda:self.process("="))
        button.img = img
        button.grid(row=5, column=2, sticky=N+S+E+W)
        # +
        img = PhotoImage(file="images-gif/add.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, activebackground="white", command= lambda:self.process("+"))
        button.img = img
        button.grid(row=5, column=3, sticky=N+S+E+W)
        
        self.pack(fill=BOTH, expand=1)
    
    # processor 
    def process(self,button):
        if (button == "AC"):
            print(self.display["text"])
            self.display["text"] = ""
        elif (button == "="):
            expr = self.display["text"]
            # evaluate the expression
            # the evalution may return an error!
            try:
                result = eval(expr)
                # store the result to the display
                self.display["text"] = str(result)
            except:
                self.display["text"] = "ERROR"
        else:
            self.display["text"] += button
##############################
# the main part of the program
##############################

# create the window
window = Tk()

# set the Window title 
window.title("The Reckoner")

#generate the GUI
p = MainGUI(window)

#display the GUI and wait for user interaction
window.mainloop()
