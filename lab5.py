# Lab 5 Diana Veliz

def cat_greeting(word):
    print(f'Cat says {word}')
    print('Cat says purr')

print(cat_greeting("hiss"))

def generate_superhero_power():
    name = "Milo"
    power = "super strength"
    print(f"{name}'s power is {power}")
    power = "flying"
    return power

print(generate_superhero_power())

def generate_superhero_power2(user_name, super_power):
    message = user_name + " has the power of " + super_power + "!"
    return message

print(generate_superhero_power2("milo", "teleportation"))

def cat_greeting_loops(greeting):
    for i in range(5):
        print(f'The cat says {greeting}')

cat_greeting_loops("meow")

def generate_multiple_powers():
    list = ["invisibility", "super strength", "telekenisis"]
    for i in range(5):
        print(f"milo has {range}")