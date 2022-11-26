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
topPanelTitle = Label(topPanel,text="Organisation Programme",fg="azure4",font=("Dosis",47),bg="burlywood", width=27)

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
buttonsPanel = Frame(app,bd =1,relief=FLAT,bg="burlywood")
buttonsPanel.pack(side=RIGHT)

# list of products
foodList = ["chicken","potatoes","salmon","burger","pasta","pizza1","pizza2","pizza3","pizza4"]
drinksList = ["water","Coca Cola","beer1","beer2","beer3","wine1","wine2","wine3","wine4"]
dessertsList = ["ice cream","fruit","brownie","mousse","cake1","cake2","cake3","cake4","cake5"]

# Generating food items
foodVariables= []
foodQuantity = []
foodText = []

cont = 0
for food in foodList:
    # Check Buttons
    foodVariables.append("")
    foodVariables[cont] = IntVar()
    food = Checkbutton(foodPanel,text=food.title(),font=("Dosis",19,"bold"),onvalue=1,offvalue=0, variable=foodVariables[cont])
    food.grid(row=cont, column=0, sticky=W)  
    
    # Food Quantity
    foodQuantity.append("")
    foodText.append("")
    foodQuantity[cont] = Entry(foodPanel,font=("Dosis",18,"bold"),bd=1,width=6,state=DISABLED,textvariable=foodText[cont])
    foodQuantity[cont].grid(row=cont,column=1)

    cont +=1


# Generating drinks items
drinksVariables= []
drinksQuantity = []
drinksText = []

cont = 0
for drinks in drinksList:
    # Check Buttons
    drinksVariables.append("")
    drinksVariables[cont] = IntVar()
    drinks = Checkbutton(drinksPanel,text=drinks.title(),font=("Dosis",19,"bold"),onvalue=1,offvalue=0, variable=drinksVariables[cont])
    drinks.grid(row=cont , column=1, sticky=W)  
    
    # drinks Quantity
    drinksQuantity.append("")
    drinksText.append("")
    drinksQuantity[cont] = Entry(drinksPanel,font=("Dosis",18,"bold"),bd=1,width=6,state=DISABLED,textvariable=drinksText[cont])
    drinksQuantity[cont].grid(row=cont,column=2)

    cont +=1


# Generating desserts items
dessertsVariables= []
dessertsQuantity = []
dessertsText = []

cont = 0
for desserts in dessertsList:
    # Check Buttons
    dessertsVariables.append("")
    dessertsVariables[cont] = IntVar()
    desserts = Checkbutton(dessertsPanel,text=desserts.title(),font=("Dosis",19,"bold"),onvalue=1,offvalue=0, variable=dessertsVariables[cont])
    desserts.grid(row=cont , column=2, sticky=W)  

    # desserts Quantity
    dessertsQuantity.append("")
    dessertsText.append("")
    dessertsQuantity[cont] = Entry(dessertsPanel,font=("Dosis",18,"bold"),bd=1,width=6,state=DISABLED,textvariable=dessertsText[cont])
    dessertsQuantity[cont].grid(row=cont,column=3)

    cont +=1
# The programme doesnt close
app.mainloop() 

