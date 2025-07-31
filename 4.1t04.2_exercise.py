"""
4-1. Pizzas: Think of at least three kinds of your favorite pizza. Store these pizza
names in a list, and then use a for loop to print the name of each pizza.
Modify your for loop to print a sentence using the name of the pizza, instead of printing
just the name of the pizza. For each pizza, you should have one line of output
containing a simple statement like I like pepperoni pizza.
Add a line at the end of your program, outside the for loop, that states how much you
like pizza. The output should consist of three or more lines about the kinds of pizza you
like and then an additional sentence, such as I really love pizza!
4-2. Animals: Think of at least three different animals that have a common
characteristic. Store the names of these animals in a list, and then use a for loop to
print out the name of each animal.
Modify your program to print a statement about each animal, such as A dog would
make a great pet.
Add a line at the end of your program, stating what these animals have in common.
You could print a sentence, such as Any of these animals would make a great pet!
"""


def think_pizzas():
    """
    Think of at least three kinds of your favorite pizza. Store these pizza
    names in a list, and then use a for loop to print the name of each pizza.
    Modify your for loop to print a sentence using the name of the pizza, instead of printing
    just the name of the pizza. For each pizza, you should have one line of output
    containing a simple statement like I like pepperoni pizza.
    Add a line at the end of your program, outside the for loop, that states how much you
    like pizza. The output should consist of three or more lines about the kinds of pizza you
    like and then an additional sentence, such as I really love pizza!
    """
    print("==Exercise 4.1==")
    pizzas = ["veg_mushroom", "chicken", "beef"]
    for pizza in pizzas:
        print(pizza.title())
        print(f"I like {pizza} pizza.I really love pizza.")
    return "How much do you like pizza?\n"


def animals():
    """
    Think of at least three different animals that have a common
    characteristic. Store the names of these animals in a list, and then use a for loop to
    print out the name of each animal.
    Modify your program to print a statement about each animal, such as A dog would
    make a great pet.
    Add a line at the end of your program, stating what these animals have in common.
    You could print a sentence, such as Any of these animals would make a great pet!
    """
    print("==Exercise 4.2==")
    animals = ["cat", "dog", "squirrel"]
    for animal in animals:
        print(f"A {animal} would make a great pet.")
    return f"These are human friendly pets.Any animal would make a great pet!"


if __name__ == "__main__":
    print(think_pizzas())
    print(animals())
