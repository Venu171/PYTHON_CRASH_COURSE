"""
 7-8. Deli: Make a list called sandwich_orders and fill it with the names of various
 sandwiches. Then make an empty list called finished_sandwiches. Loop through the list
 of sandwich orders and print a message for each order, such as I made your tuna
 sandwich. As each sandwich is made, move it to the list of finished sandwiches. After all
 the sandwiches have been made, print a message listing each sandwich that was
 made.
 7-9. No Pastrami: Using the list sandwich_orders from Exercise 7-8, make sure the
 sandwich 'pastrami' appears in the list at least three times. Add code near the
 beginning of your program to print a message saying the deli has run out of pastrami,
 and then use a while loop to remove all occurrences of 'pastrami' from
 sandwich_orders. Make sure no pastrami sandwiches end up in finished_sandwiches.
 7-10. Dream Vacation: Write a program that polls users about their dream vacation.
 Write a prompt similar to If you could visit one place in the world, where would you go?
 Include a block of code that prints the results of the poll.
"""


def deli():
    """
    Make a list called sandwich_orders and fill it with the names of various
    sandwiches. Then make an empty list called finished_sandwiches. Loop through the list
    of sandwich orders and print a message for each order, such as I made your tuna
    sandwich. As each sandwich is made, move it to the list of finished sandwiches. After all
    the sandwiches have been made, print a message listing each sandwich that was
    made.
    """
    sandwich_orders = ["veg", "chicken", "mushroom"]
    finished_sandwiches = []
    while sandwich_orders:
        finished_one = sandwich_orders.pop()
        print(f"I made your {finished_one} sandwich.")
        finished_sandwiches.append(finished_one)
    print(finished_sandwiches)
    return f"\n==Sandwiches function finished.==\n"


def no_pastrami():
    """
    Using the list sandwich_orders from Exercise 7-8, make sure the
    sandwich 'pastrami' appears in the list at least three times. Add code near the
    beginning of your program to print a message saying the deli has run out of pastrami,
    and then use a while loop to remove all occurrences of 'pastrami' from
    sandwich_orders. Make sure no pastrami sandwiches end up in finished_sandwiches.
    """
    sandwich_orders = ["pastrami", "veg", "pastrami",
                       "chicken", "pastrami", "mushroom", "pastrami"]
    finished_sandwiches = []
    while sandwich_orders:
        finished_one = sandwich_orders.pop()
        if finished_one == 'pastrami':
            print("Deli has run out of pastrami.")
        else:
            finished_sandwiches.append(finished_one)
    print("Finished Sandwiches:", finished_sandwiches)
    print("Sandwich Orders:", sandwich_orders)
    return f"\n==Finished no pastrami sandwiches.==\n"


def dream_vacation():
    """
    Write a program that polls users about their dream vacation.
    Write a prompt similar to If you could visit one place in the world, where would you go?
    Include a block of code that prints the results of the poll.
    """
    dream_vacations = []
    while len(dream_vacations) <= 10:
        dream_vacation = input(
            "If you could visit one place in the world, where would you go?")
        dream_vacations.append(dream_vacation)
    return dream_vacations


if __name__ == "__main__":
    print(deli())
    print(no_pastrami())
    print(dream_vacation())
