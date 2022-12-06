from tkinter import *
import random
import datetime

operator = ""

foodPrices = [1.32, 1.65, 2.31, 3.22, 1.22, 1.99, 2.05, 2.65]
drinksPrices = [0.25, 0.99, 1.21, 1.54, 1.08, 1.10, 2.00, 1.58]
dessertsPrices = [1.54, 1.68, 1.32, 1.97, 2.55, 2.14, 1.94, 1.74]

def press_button(number):
    global operator
    operator = operator + number
    screen.delete(0,END)            # cleans the windows
    screen.insert(END,operator)

def clean():
    global operator
    operator = ""
    screen.delete(0,END)

def result():
    global operator
    res = str(eval(operator))       # Reads the string and returns the operation inside it 
    screen.delete(0,END)
    screen.insert(0,res)
    operator = ""

def check_button():
    cont = 0
    for i in foodQuantity:
        if foodVariables[cont].get() == 1:
            foodQuantity[cont].config(state=NORMAL)
            if foodQuantity[cont].get() == "0":
                foodQuantity[cont].delete(0,END)
                foodQuantity[cont].focus()
        else:
            foodQuantity[cont].config(state=DISABLED)
            foodText[cont].set("0")
        cont += 1

    cont = 0
    for i in drinksQuantity:
        if drinksVariables[cont].get() == 1:
            drinksQuantity[cont].config(state=NORMAL)
            if drinksQuantity[cont].get() == "0":
                drinksQuantity[cont].delete(0,END)
                drinksQuantity[cont].focus()
        else:
            drinksQuantity[cont].config(state=DISABLED)
            drinksText[cont].set("0")
        cont += 1

    cont = 0
    for i in dessertsQuantity:
        if dessertsVariables[cont].get() == 1:
            dessertsQuantity[cont].config(state=NORMAL)
            if dessertsQuantity[cont].get() == "0":
                dessertsQuantity[cont].delete(0,END)
                dessertsQuantity[cont].focus()
        else:
            dessertsQuantity[cont].config(state=DISABLED)
            dessertsText[cont].set("0")
        cont += 1

def calculate_total():
    subtotalFood = 0
    subtotalDrink = 0
    subtotalDessesrt = 0
    cont = 0
    for i in foodText:
        subtotalFood = subtotalFood + (float(i.get()) * foodPrices[cont])
        cont += 1
    
    cont = 0
    for i in drinksText:
        subtotalDrink = subtotalDrink + (float(i.get()) * drinksPrices[cont])
        cont += 1
    
    cont = 0
    for i in dessertsText:
        subtotalDessesrt = subtotalDessesrt + (float(i.get()) * dessertsPrices[cont])
        cont += 1
    
    subtotal = subtotalFood + subtotalDrink + subtotalDessesrt
    taxes = 0.21*subtotal
    total = subtotal + taxes

    costFoodVar.set(f"€ {round(subtotalFood,2)}")
    costDrinksVar.set(f"€ {round(subtotalDrink,2)}")
    costDessertsVar.set(f"€ {round(subtotalDessesrt,2)}")
    subtotalVar.set(f"€ {round(subtotal,2)}")
    taxesVar.set(f"€ {round(taxes,2)}")
    totalVar.set(f"€ {round(total,2)}")

def generate_receipt():
    receiptText.delete(1.0 ,END)
    receiptNumber = f"N# - {random.randint(1000,9999)}"
    date = datetime.datetime.now()
    receiptDate = f"{date.day}/{date.month}/{date.year} - {date.hour}:{date.hour}"
    receiptText.insert(END, f"Data: \t{receiptNumber}\t\t\t{receiptDate}\n")
    receiptText.insert(END,"*"*70 + "\n")
    receiptText.insert(END,"Items\t\t\tNum\t\tCost\n")
    receiptText.insert(END,"-"*87 + "\n")

# Initiating tkinder
app = Tk()

# dimension of the window
app.geometry("1060x600+0+0")
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
costPanel = Frame(leftPanel,bd =1,relief=FLAT,bg="azure4",padx=55)
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
calculatorPanel = Frame(rightPanel,bd =1,relief=FLAT,bg="burlywood")
calculatorPanel.pack()

# receipt panel
receiptPanel = Frame(rightPanel,bd =1,relief=FLAT,bg="burlywood")
receiptPanel.pack()

# buttons panel
buttonsPanel = Frame(rightPanel,bd =1,relief=FLAT,bg="burlywood")
buttonsPanel.pack()

# list of products
foodList = ["chicken","potatoes","salmon","burger","pasta","pizza1","pizza2","pizza3"]
drinksList = ["water","Coca Cola","beer1","beer2","beer3","wine1","wine2","wine3"]
dessertsList = ["ice cream","fruit","brownie","mousse","cake1","cake2","cake3","cake4"]

# Generating food items
foodVariables= []
foodQuantity = []
foodText = []

cont = 0
for food in foodList:
    # Check Buttons
    foodVariables.append("")
    foodVariables[cont] = IntVar()
    food = Checkbutton(foodPanel,text=food.title(),font=("Dosis",19,"bold"),onvalue=1,offvalue=0, variable=foodVariables[cont],command=check_button)
    food.grid(row=cont, column=0, sticky=W)  
    
    # Food Quantity
    foodQuantity.append("")
    foodText.append("")
    foodText[cont] =StringVar()
    foodText[cont].set("0")
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
    drinks = Checkbutton(drinksPanel,text=drinks.title(),font=("Dosis",19,"bold"),onvalue=1,offvalue=0, variable=drinksVariables[cont],command=check_button)
    drinks.grid(row=cont , column=1, sticky=W)  
    
    # drinks Quantity
    drinksQuantity.append("")
    drinksText.append("")
    drinksText[cont] =StringVar()
    drinksText[cont].set("0")
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
    desserts = Checkbutton(dessertsPanel,text=desserts.title(),font=("Dosis",19,"bold"),onvalue=1,offvalue=0, variable=dessertsVariables[cont],command=check_button)
    desserts.grid(row=cont , column=2, sticky=W)  

    # desserts Quantity
    dessertsQuantity.append("")
    dessertsText.append("")
    dessertsText[cont] =StringVar()
    dessertsText[cont].set("0")
    dessertsQuantity[cont] = Entry(dessertsPanel,font=("Dosis",18,"bold"),bd=1,width=6,state=DISABLED,textvariable=dessertsText[cont])
    dessertsQuantity[cont].grid(row=cont,column=3)

    cont +=1

# Total cost
subtotal = StringVar()
taxes = StringVar()
total = StringVar()

# food
foodCost = Label(costPanel,text="Food Cost", font=("Dosis",14,"bold"), bg="azure4",fg="white")
foodCost.grid(row=0,column=0)

costFoodVar = StringVar()

foodCostText = Entry(costPanel,font=("Dosis",14,"bold"),bd=1,width=10,state="readonly",textvariable=costFoodVar)
foodCostText.grid(row=0,column=1, padx=35)

# drinks
drinksCost = Label(costPanel,text="Drinks Cost", font=("Dosis",14,"bold"), bg="azure4",fg="white")
drinksCost.grid(row=1,column=0)

costDrinksVar = StringVar()

drinksCostText = Entry(costPanel,font=("Dosis",14,"bold"),bd=1,width=10,state="readonly",textvariable=costDrinksVar)
drinksCostText.grid(row=1,column=1, padx=35)

# desserts
dessertsCost = Label(costPanel,text="Desserts Cost", font=("Dosis",14,"bold"), bg="azure4",fg="white")
dessertsCost.grid(row=2,column=0)

costDessertsVar = StringVar()

dessertsCostText = Entry(costPanel,font=("Dosis",14,"bold"),bd=1,width=10,state="readonly",textvariable=costDessertsVar)
dessertsCostText.grid(row=2,column=1, padx=35)

# subtotal
subtotal = Label(costPanel,text="Subtotal", font=("Dosis",14,"bold"), bg="azure4",fg="white")
subtotal.grid(row=0,column=2)

subtotalVar = StringVar()

subtotalText = Entry(costPanel,font=("Dosis",14,"bold"),bd=1,width=10,state="readonly",textvariable=subtotalVar)
subtotalText.grid(row=0,column=3, padx=35)

# taxes
taxes = Label(costPanel,text="Taxes", font=("Dosis",14,"bold"), bg="azure4",fg="white")
taxes.grid(row=1,column=2)

taxesVar = StringVar()

taxesText = Entry(costPanel,font=("Dosis",14,"bold"),bd=1,width=10,state="readonly",textvariable=taxesVar)
taxesText.grid(row=1,column=3, padx=35)

# total
total = Label(costPanel,text="Total", font=("Dosis",14,"bold"), bg="azure4",fg="white")
total.grid(row=2,column=2)

totalVar = StringVar()

totalText = Entry(costPanel,font=("Dosis",14,"bold"),bd=1,width=10,state="readonly",textvariable=totalVar)
totalText.grid(row=2,column=3, padx=35)

# Buttons
buttons = ["Total", "Receipt", "Save", "Reset"]
createdButtons = []
columns = 0

for button in buttons:
    button = Button(buttonsPanel, text=button.title(),font=("Dosis",11,"bold"),fg="white",bg="azure4",bd=1,width=9)
    createdButtons.append(button)
    button.grid(row=0,column=columns)
    columns += 1

createdButtons[0].config(command = calculate_total)
createdButtons[1].config(command = generate_receipt)

# Receipt Area
receiptText = Text(receiptPanel,font=("Dosis",10,"bold"),fg="black",bd=1,width=50,height=15)
receiptText.grid(row=0,column=0)

# Calculator
screen = Entry(calculatorPanel,font=("Dosis",14,"bold"),width=31,bd=1)
screen.grid(row=0,column=0,columnspan=4)    # Columns span: how much each column occupies

calculatorButtons = ["7","8","9","+","4",'5','6','-','1','2','3','x',"Reset",'0','=','/']

saveButtons = []

calculatorColumn = 0
calculatorRow = 1

for button in calculatorButtons:
    
    button = Button(calculatorPanel,text=button.title(),font=("Dosis",16,"bold"),fg="black",bg="azure4",bd=1,width=6)
    button.grid(row=calculatorRow,column=calculatorColumn)

    saveButtons.append(button)

    if calculatorColumn >2:
        calculatorRow += 1
        calculatorColumn = 0
    else:
        calculatorColumn +=1

saveButtons[0].config(command=lambda:press_button("7"))
saveButtons[1].config(command=lambda:press_button("8"))
saveButtons[2].config(command=lambda:press_button("9"))
saveButtons[3].config(command=lambda:press_button("+"))
saveButtons[4].config(command=lambda:press_button("4"))
saveButtons[5].config(command=lambda:press_button("5"))
saveButtons[6].config(command=lambda:press_button("6"))
saveButtons[7].config(command=lambda:press_button("-"))
saveButtons[8].config(command=lambda:press_button("1"))
saveButtons[9].config(command=lambda:press_button("2"))
saveButtons[10].config(command=lambda:press_button("3"))
saveButtons[11].config(command=lambda:press_button("*"))
saveButtons[12].config(command=clean)
saveButtons[13].config(command=lambda:press_button("0"))
saveButtons[14].config(command=result)
saveButtons[15].config(command=lambda:press_button("/"))


# The programme doesnt close
app.mainloop() 

