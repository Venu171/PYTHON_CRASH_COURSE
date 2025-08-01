"""
 7-4. Pizza Toppings: Write a loop that prompts the user to enter a series of pizza
 toppings until they enter a 'quit' value. As they enter each topping, print a message
 saying you’ll add that topping to their pizza.
 7-5. Movie Tickets: A movie theater charges different ticket prices depending on a
 person’s age. If a person is under the age of 3, the ticket is free; if they are between 3
 and 12, the ticket is $10; and if they are over age 12, the ticket is $15. Write a loop in
 which you ask users their age, and then tell them the cost of their movie ticket.
 7-6. Three Exits: Write different versions of either Exercise 7-4 or 7-5 that do each of
 the following at least once:
 Use a conditional test in the while statement to stop the loop.
 Use an active variable to control how long the loop runs.
 Use a break statement to exit the loop when the user enters a 'quit' value.
 7-7. Infinity: Write a loop that never ends, and run it. (To end the loop, press CTRL-C
 or close the window displaying the output.)
 """


def pizza_toppings():
    """
    Write a loop that prompts the user to enter a series of pizza
    toppings until they enter a 'quit' value. As they enter each topping, print a message
    saying you’ll add that topping to their pizza.
    """
    flag = True
    while flag:
        tooping_choice = input("Enter the toppings to be used in pizza: ")
        if tooping_choice.lower() == "quit":
            flag = False
        print(f"You’ll add {tooping_choice} topping to their pizza.")
    return f"\n==Pizza Toppingd function executed.==\n"


def movie_tickets():
    """
    A movie theater charges different ticket prices depending on a
    person’s age. If a person is under the age of 3, the ticket is free; if they are between 3
    and 12, the ticket is $10; and if they are over age 12, the ticket is $15. Write a loop in
    which you ask users their age, and then tell them the cost of their movie ticket.
    """
    ticket_prize_below_3 = 0
    ticket_prize_below_12 = 10
    ticket_prize_above_12 = 15
    flag = True
    while flag:
        age = input("Enter your age: ")
        if age.isnumeric():
            if int(age) < 3:
                print(
                    f"The cost of the movie ticket for your age {age} is ${ticket_prize_below_3}")
            elif int(age) <= 12:
                print(
                    f"The cost of the movie ticket for your age {age} is ${ticket_prize_below_12}")
            elif int(age) > 15:
                print(
                    f"The cost of the movie ticket for your age {age} is ${ticket_prize_above_12}")
        else:
            flag = False
    return f"\n==Movie Tickets function ececuted.==\n"

# Actually, I wrote this problem before only.


def three_exists():
    """
    Write different versions of either Exercise 7-4 or 7-5 that do each of
    the following at least once:
    Use a conditional test in the while statement to stop the loop.
    Use an active variable to control how long the loop runs.
    Use a break statement to exit the loop when the user enters a 'quit' value.
    """
    pass


if __name__ == "__main__":
    # print(pizza_toppings())
    # print(movie_tickets())
    print(three_exists())
