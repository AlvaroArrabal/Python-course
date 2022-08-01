import os
from pathlib import Path

# read
#   category
#   show recipes
#   select one
#   read that recipe
# write
#   category
#   name and recipe
# create category
#   new category?
# delete recipe
#   category
#   show recipes
#   select one
#   delete that recipe
# delete category
#   category
#   show recipes
#   select one
#   delete that category
# end

def opening():
    recipePath = os.getcwd()
    recipePath = Path(recipePath,"DAY_6","PROYECT_RECIPE_BOOK","Recetas")
    os.system("cls")
    print("---------------------------\nWelcome to the RECIPE BOOK!\n---------------------------")
    print(f"The recipe in in {recipePath}")

    total = 0
    for i in Path(recipePath).glob("**/*.txt"):
        total += 1
    print(f"Current recipes: {total}\n---------------------------")
    return recipePath

def ask_option():
    print("   1. READ RECIPE\n   2. WRITE RECIPE\n   3. CREATE CATEGORY\n   4. DELETE RECIPE\n   5. DELETE CATEGORY\n   6. EXIT")
    option = input(" Option: ")
    option = int(option)
    os.system("cls")
    return option

def show_categories(recipePath):
    for i in recipePath.iterdir():
        i_str = str(i.name)
        print(f"- {i_str}")

def exists_category(path):
    if path.exists() == True:
        return True
    else:
        return False
    

def read_recipe(recipePath):
    show_categories(recipePath)
    category = input("Choose a category: ")
    newPath = Path(recipePath,category)

    valid = exists_category(newPath)
    if valid == False:
        os.system("cls")
        print("Category not found...\nBack to the menu\n--------------------")
    else:
        for i in Path(newPath).glob("*.txt"):
            #print(os.path.basename(i).stem)
            print(i.stem)

        recipe = input("Choose a recipe: ")
        recipe = recipe + ".txt"
        recipe = Path(newPath,recipe)

        if not recipe.exists():
            print("File not found")
            print("--------------------")
        else:
            os.system("cls")
            text = open(recipe)
            print(recipe.read_text())
            print("--------------------")
    
def write_recipe(recipePath):
    show_categories(recipePath)
    category = input("Choose a category: ")
    newPath = Path(recipePath,category)

    valid = exists_category(newPath)

    if valid == False:
        print("Category not found")
        answer = input("Do you want to create a new Category? (y/n) ")

        if answer == "y":
            os.system("cls") 
            create_category(recipePath)
        else:
            os.system("cls")
            print("Back to the menu\n--------------------")
    else:
        recipe = input("Name of the new recipe? ")
        recipe = recipe +".txt"
        recipe = Path(newPath,recipe)
        text = input("Write the recipe: ")

        newRecipe = open(recipe,"w")
        newRecipe.write(text)
        newRecipe.close()

def create_category(recipePath):
    show_categories(recipePath)
    newCategory = input("Name of the new category? ")
    newCategory = Path(recipePath,newCategory)
    os.makedirs(newCategory)
    os.system("cls")
    print("New Category created\n--------------------")

def delete_recipe(recipePath):
    show_categories(recipePath)
    category = input("Choose a category: ")
    newPath = Path(recipePath,category)

    for i in Path(newPath).glob("*.txt"):
        print(i.stem)

    recipe = input("Choose a recipe: ")
    recipe = recipe + ".txt"
    recipe = Path(newPath,recipe)
    os.system("cls")
    if not recipe.exists():
        print("File not found\n--------------------")
    else:
        os.remove(recipe)
        print("Recipe deleted\n--------------------")

def delete_category(recipePath):
    show_categories(recipePath)
    category = input("Name of the category? ")
    category = Path(recipePath, category)

    os.rmdir(category)

#---- BEGIN ----

recipePath = opening()

#---- MENU ----
option = ask_option()

while option != 6:
    if option == 1:
        read_recipe(recipePath)
        option = ask_option()
    elif option == 2:
        write_recipe(recipePath)
        option = ask_option()
    elif option == 3:
        create_category(recipePath)
        option = ask_option()
    elif option == 4:
        delete_recipe(recipePath)
        option = ask_option()
    elif option == 5:
        delete_category(recipePath)
        option = ask_option()
    elif option == 6:
        break
    else:
        print("Thats not an option")
        option = ask_option()