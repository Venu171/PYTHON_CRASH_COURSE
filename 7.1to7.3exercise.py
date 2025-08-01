""" 
7-1. Rental Car: Write a program that asks the user what kind of rental car they would
 like. Print a message about that car, such as “Let me see if I can find you a Subaru.”
 7-2. Restaurant Seating: Write a program that asks the user how many people are in
 their dinner group. If the answer is more than eight, print a message saying they’ll have
 to wait for a table. Otherwise, report that their table is ready.
 7-3. Multiples of Ten: Ask the user for a number, and then report whether the number
 is a multiple of 10 or not.
 """


def rental_car():
    """
    Write a program that asks the user what kind of rental car they would
    like. Print a message about that car, such as “Let me see if I can find you a Subaru.
    """
    car = input("What kind of car do you like? ")
    return f"Let me see if I can find you a {car}"


def restaurant_seating():
    """
    Write a program that asks the user how many people are in
    their dinner group. If the answer is more than eight, 
    print a message saying they’ll have to wait for a table. Otherwise, report that their table is ready.
    """
    dinner_group = input("How many people are there in your dinner group?")
    return f"The table is ready for the {dinner_group} memebers."


def multiples():
    """
    Ask the user for a number, and then report whether the number
    is a multiple of 10 or not.
    """
    number = int(
        input("Enter anumber to check if number is multiple of 10 or not: "))
    if number % 10 == 0:
        return f"{number} is multiple of 10."
    else:
        return f"{number} is not a multiple of 10."


if __name__ == "__main__":
    print(rental_car())
    print(restaurant_seating())
    print(multiples())
