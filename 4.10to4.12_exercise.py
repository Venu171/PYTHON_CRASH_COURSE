"""
4-10. Slices: Using one of the programs you wrote in this chapter, add several lines to
the end of the program that do the following:
Print the message The first three items in the list are:. Then use a slice to print the first
three items from that program’s list.
Print the message Three items from the middle of the list are:. Then use a slice to print
three items from the middle of the list.
Print the message The last three items in the list are:. Then use a slice to print the last
three items in the list.
4-11. My Pizzas, Your Pizzas: Start with your program from Exercise 4-1 (page 56).
Make a copy of the list of pizzas, and call it friend_pizzas. Then, do the following:
Add a new pizza to the original list.
Add a different pizza to the list friend_pizzas.
Prove that you have two separate lists. Print the message My favorite pizzas are:, and
then use a for loop to print the first list. Print the message My friend’s favorite pizzas
are:, and then use a for loop to print the second list. Make sure each new pizza is
stored in the appropriate list.
4-12. More Loops: All versions of foods.py in this section have avoided using for
loops when printing, to save space. Choose a version of foods.py, and write two for
loops to print each list of foods.
"""


def slices():
    """
    Using one of the programs you wrote in this chapter, add several lines to
    the end of the program that do the following:
    Print the message The first three items in the list are:. Then use a slice to print the first
    three items from that program’s list.
    Print the message Three items from the middle of the list are:. Then use a slice to print
    three items from the middle of the list.
    Print the message The last three items in the list are:. Then use a slice to print the last
    three items in the list.
    """
    items = ["apple", "bat", "cat", "dog", "elephant", "frog", "god"]
    print(
        f"The first three elements from the beginning:{items[0:3]}.\nThree items from the middle of the list are:{items[len(items)//2:len(items)//2+3]}.\nThe last three items in the list are:{items[-3:]}")
    return f"Slice function completed.\n"


def pizzas():
    """
    Start with your program from Exercise 4-1 (page 56).
    Make a copy of the list of pizzas, and call it friend_pizzas. Then, do the following:
    Add a new pizza to the original list.
    Add a different pizza to the list friend_pizzas.
    Prove that you have two separate lists. Print the message My favorite pizzas are:, and
    then use a for loop to print the first list. Print the message My friend’s favorite pizzas
    are:, and then use a for loop to print the second list. Make sure each new pizza is
    stored in the appropriate list.
    """
    pizzas = ["veg_mushroom", "chicken", "beef"]
    friend_pizzas = pizzas[:]
    friend_pizzas.append('Mixup')
    print(f"Original list:{pizzas}\nCopied List:{friend_pizzas}")
    print(f"My favourite pizzas are:")
    for i in pizzas:
        print(i)
    print("My friend’s favorite pizzas are:")
    for i in friend_pizzas:
        print(i)
    return f"Pizza function completed.\n"


def more_loops():
    """
    All versions of foods.py in this section have avoided using for
    loops when printing, to save space. Choose a version of foods.py, and write two for
    loops to print each list of foods.
    """
    my_foods = ['pizza', 'falafel', 'carrot cake']
    friend_foods = my_foods
    friend_foods.append("ice cream")
    print("My favourite foods are:")
    for i in my_foods:
        print(i)
    print("My favourite foods are:")
    for i in friend_foods:
        print(i)
    return "More loops function implemented."


if __name__ == "__main__":
    print(slices())
    print(pizzas())
    print(more_loops())
