from tkinter import *

# Initiating tkinder
app = Tk()

# dimension of the window
app.geometry("1020x630+0+0")
app.resizable(0,0) # The user cant change the dimension if the window

# change the name of the window
app.title("My restaurant") 

# change the color of the background
app.config(bg="burlywood") 

# top panel
topPanel = Frame(app,bd=2,relief=FLAT)              # relief = FLAT / RAISED / SUNKEN / GROOVE / RIDGE
topPanel.pack(side=TOP)

# Title top panel
topPanelTitle = Label(topPanel,text="Organisation programme",fg="azure4",font=("Dosis",47),bg="burlywood", width=27)

topPanelTitle.grid(row=0,column=0)

# Left panel
leftPanel = Frame(app,bd =1,relief=FLAT)
leftPanel.pack(side=LEFT)

# Cost panel
costPanel = Frame(app,bd =1,relief=FLAT)
costPanel.pack(side=BOTTOM)

# Food panel
foodPanel = LabelFrame(leftPanel,text="Food", font=("Dosis",19,"bold"),bd=1,relief=FLAT,fg="azure4")
foodPanel.pack(side=LEFT)

# Drinks panel
drinksPanel = LabelFrame(leftPanel,text="Drinks", font=("Dosis",19,"bold"),bd=1,relief=FLAT,fg="azure4")
drinksPanel.pack(side=LEFT)

# Desserts panel
dessertsPanel = LabelFrame(leftPanel,text="Desserts", font=("Dosis",19,"bold"),bd=1,relief=FLAT,fg="azure4")
dessertsPanel.pack(side=LEFT)

# Right panel
rightPanel = Frame(app,bd =1,relief=FLAT)
rightPanel.pack(side=RIGHT)

# Calculator panel
calculatorPanel = Frame(app,bd =1,relief=FLAT,bg="burlywood")
calculatorPanel.pack(side=RIGHT)

# receipt panel
receiptPanel = Frame(app,bd =1,relief=FLAT,bg="burlywood")
receiptPanel.pack(side=RIGHT)

# buttons panel

# The programme doesnt close
app.mainloop() 

