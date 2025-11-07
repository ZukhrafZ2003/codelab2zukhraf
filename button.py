from tkinter import *

root = Tk ()
root.title("Button Example")

def click_me(): 
    print("Button Clicked!")

mybutton = Button(root, text="Click Me", command=click_me) 
mybutton.grid()

root.mainloop()
