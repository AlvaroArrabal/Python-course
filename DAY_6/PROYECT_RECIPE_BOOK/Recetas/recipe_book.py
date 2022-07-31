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
def ask_option():
    print('''1. READ RECIPE\n2. WRITE RECIPE\n3. CREATE CATEGORY\n4. DELETE RECIPE\n5. DELETE CATEGORY\n6. EXIT''')
    option = input("Option: ")
    option = int(option)
    os.system("cls")
    return option

def show_categories(recipePath):
    for i in recipePath.iterdir():
        i_str = str(i.name)
        print(f"- {i_str}")

def read_recipe(recipePath):
    show_categories(recipePath)

    category = input("Choose a category: ")
    newPath = Path(recipePath,category)

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
    category = input("Choose a category: ")
    newPath = Path(recipePath,category)
    recipe = input("Name of the new recipe? ")
    recipe = recipe +".txt"
    recipe = Path(newPath,recipe)
    text = input("Write the recipe: ")

    newRecipe = open(recipe,"w")
    newRecipe.write(text)
    newRecipe.close()

def create_category(recipePath):
    newCategory = input("Name of the new category? ")
    newCategory = Path(recipePath,newCategory)
    os.makedirs(newCategory)
    print("New Category created")

def delete_recipe(recipePath):
    category = input("Choose a category: ")
    newPath = Path(recipePath,category)

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
        os.remove(recipe)
        print("Recipe deleted")

def delete_category(recipePath):
    category = input("Name of the category? ")
    category = Path(recipePath, category)

    os.rmdir(category)



#---- BEGIN ----

recipePath = os.getcwd()
recipePath = Path(recipePath,"PROYECT_RECIPE_BOOK","Recetas")
print(f"The recipe in in {recipePath}")

total = 0
for i in Path(recipePath).glob("**/*.txt"):
    total += 1
print(f"Current recipes: {total}")


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