
cookbook = {"milk and cereal": "A simple breakfast meal"}

def create_recipe(name, description):
    cookbook[name] = description
    print(f"Created a new recipe: {name}")

def read_recipe(name):
    description = cookbook.get(name)
    if description:
        print(f"Recipe: {name}\nDescription: {description}")
    else:
        print(f"Recipe '{name}' not found.")

def update_recipe(name, new_description):
    if name in cookbook:
        cookbook[name] = new_description
        print(f"Updated the recipe: {name}")
    else:
        print(f"Recipe '{name}' not found.")

def destroy_recipe(name):
    if name in cookbook:
        del cookbook[name]
        print(f"Destroyed the recipe: {name}")
    else:
        print(f"Recipe '{name}' not found.")

def list_all_recipes():
    if not cookbook:
        print("No recipes in the cookbook.")
    else:
        print("All Recipes:")
        for name, description in cookbook.items():
            print(f"- {name}: {description}")
                
def main():
    while True:
        print("\nCookbook Menu:")
        print("1. Create a new recipe")
        print("2. Read a recipe")
        print("3. Update a recipe")
        print("4. Delete a recipe")
        print("5. List all recipes")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            name = input("Enter the name of the recipe: ")
            description = input("Enter the description of the recipe: ")
            create_recipe(name, description)
        elif choice == "2":
            name = input("Enter the name of the recipe to read: ")
            read_recipe(name)
        elif choice == "3":
            name = input("Enter the name of the recipe to update: ")
            new_description = input("Enter the new description: ")
            update_recipe(name, new_description)
        elif choice == "4":
            name = input("Enter the name of the recipe to delete: ")
            destroy_recipe(name)
        elif choice == "5":
            list_all_recipes()
        elif choice == "6":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()