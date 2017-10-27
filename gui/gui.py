from tkinter import *

def doSome():
	print("Hello")

root = Tk()
root.title("Privacy Preservation")
root.geometry("1080x640")
menu = Menu(root)
root.config(menu = menu)

subMenu = Menu(menu)
menu.add_cascade(label = "File", menu = subMenu)
subMenu.add_command(label = "New node file", command = doSome)
subMenu.add_command(label = "New edge file", command = doSome)
subMenu.add_separator()
subMenu.add_command(label = "Exit", command = doSome)


editMenu = Menu(menu)
menu.add_cascade(label = "Edit", menu = editMenu)
editMenu.add_command(label = "Remove selected files", command = doSome)

helpMenu = Menu(menu)
menu.add_cascade(label = "Help", menu = helpMenu)
helpMenu.add_command(label = "Documentation", command = doSome)
helpMenu.add_command(label = "About", command = doSome)

leftFrame = Frame(root)
leftFrame.pack(fill = Y, side = LEFT)

rightFrame = Frame(root)
rightFrame.pack(fill = Y, side = LEFT)

ltopFrame = Frame(leftFrame)
ltopFrame.grid(row = 0, column = 0)

lmiddleFrame = Frame(leftFrame)
lmiddleFrame.grid(row = 1, column = 0, rowspan = 2)

lbottomFrame = Frame(leftFrame)
lbottomFrame.grid(row = 3, column = 0, rowspan = 2)

titleLeft = Label(ltopFrame, text = "k-annonymizer", font = 100, fg = "red")
applyButton = Button(lmiddleFrame, text = "Apply")
slider = Scale(lmiddleFrame, label = "k value", from_= 0, to = 16, tickinterval = 2, orient = "horizontal", resolution = 1, length = 300)
statLabel = Label(lbottomFrame, text = "Stats")
statNodes = Label(lbottomFrame, text = "Number of Nodes : ")
statEdges = Label(lbottomFrame, text = "NUmber of Edges : ")

titleLeft.pack(padx = 10, pady = 10)

slider.pack(fill = X, padx = 10, pady = 10)
applyButton.pack(side = RIGHT, pady = 10, padx = 10)

statLabel.grid(row = 0, column = 0)
statNodes.grid(row = 1, column = 0, sticky = NW)
statEdges.grid(row = 2, column = 0)

title = Label(rightFrame, text = "Graphical Representation", font = 100)
img = PhotoImage(file = "plot.png")
panel = Label(rightFrame, image = img)

title.pack(fill = X)
panel.pack(padx = 10, ipadx = 10, fill = "none", expand = "yes")

root.mainloop()