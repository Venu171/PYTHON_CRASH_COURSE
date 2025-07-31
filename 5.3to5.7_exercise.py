"""
5-3. Alien Colors #1: Imagine an alien was just shot down in a game. Create a
 variable called alien_color and assign it a value of 'green', 'yellow', or 'red'.
 Write an if statement to test whether the alien’s color is green. If it is, print a message
 that the player just earned 5 points.
 Write one version of this program that passes the if test and another that fails. (The
 version that fails will have no output.)
 5-4. Alien Colors #2: Choose a color for an alien as you did in Exercise 5-3, and write
 an if-else chain.
 If the alien’s color is green, print a statement that the player just earned 5 points for
 shooting the alien.
 If the alien’s color isn’t green, print a statement that the player just earned 10 points.
 Write one version of this program that runs the if block and another that runs the else
 block.
 5-5. Alien Colors #3: Turn your if-else chain from Exercise 5-4 into an if-elif-else
 chain.
 If the alien is green, print a message that the player earned 5 points.
 If the alien is yellow, print a message that the player earned 10 points.
 If the alien is red, print a message that the player earned 15 points.
 Write three versions of this program, making sure each message is printed for the
 appropriate color alien.
 5-6. Stages of Life: Write an if-elif-else chain that determines a person’s stage of
 life. Set a value for the variable age, and then:
 If the person is less than 2 years old, print a message that the person is a baby.
 If the person is at least 2 years old but less than 4, print a message that the person is a
 toddler.
 If the person is at least 4 years old but less than 13, print a message that the person is
 a kid.
 If the person is at least 13 years old but less than 20, print a message that the person
 is a teenager.
 If the person is at least 20 years old but less than 65, print a message that the person
 is an adult.
 If the person is age 65 or older, print a message that the person is an elder.
 5-7. Favorite Fruit: Make a list of your favorite fruits, and then write a series of
 independent if statements that check for certain fruits in your list.
 Make a list of your three favorite fruits and call it favorite_fruits.
Write five if statements. Each should check whether a certain kind of fruit is in your
 list. If the fruit is in your list, the if block should print a statement, such as You really
 like bananas!
"""


def alien_colors():
    """
    Imagine an alien was just shot down in a game. Create a
    variable called alien_color and assign it a value of 'green', 'yellow', or 'red'.
    Write an if statement to test whether the alien’s color is green. If it is, print a message
    that the player just earned 5 points.
    Write one version of this program that passes the if test and another that fails. (The
    version that fails will have no output.)
    """
    alien_color = 'green'
    if alien_color == "green":
        print("Player earned 5 points.")
    # the below creates the failed version of the above if conditionals
    # if alien_color=='red':
    #    print("None")
    return f"Alien colors function implemented.\n"


def alien_colors_two():
    """
    Alien Colors #2: Choose a color for an alien as you did in Exercise 5-3, and write
    an if-else chain.
    If the alien’s color is green, print a statement that the player just earned 5 points for
    shooting the alien.
    If the alien’s color isn’t green, print a statement that the player just earned 10 points.
    Write one version of this program that runs the if block and another that runs the else
    block.
    """
    alien_color = "red"
    # The below one executes the `else` blocks.
    if alien_color == "green":
        print("The player earned 5 points.")
    else:
        print("The player earned 10 points")
    # The below executes for the `if` block
    # if alien_color=="red":
    #    print("The player earned 5 points.")
    # else:
    #    print("The player earned 10 points")
    return f"Alien colors function executed.\n"


def alien_colors_three():
    """
    Alien Colors #3: Turn your if-else chain from Exercise 5-4 into an if-elif-else chain.
    If the alien is green, print a message that the player earned 5 points.
    If the alien is yellow, print a message that the player earned 10 points.
    If the alien is red, print a message that the player earned 15 points.
    Write three versions of this program, making sure each message is printed for the
    appropriate color alien.
    """
    alien_color = "green"
    if alien_color == "green":
        print("The player earned 5 points.")
    elif alien_color == "yellow":
        print("The player earned 10 points.")
    else:
        print("The player earned 15 points.")
    return f"Alien colors if-elif-else function executed.\n"


def stages_of_life():
    """
    Stages of Life: Write an if-elif-else chain that determines a person’s stage of
    life. Set a value for the variable age, and then:
    If the person is less than 2 years old, print a message that the person is a baby.
    If the person is at least 2 years old but less than 4, print a message that the person is a
    toddler.
    If the person is at least 4 years old but less than 13, print a message that the person is
    a kid.
    If the person is at least 13 years old but less than 20, print a message that the person
    is a teenager.
    If the person is at least 20 years old but less than 65, print a message that the person
    is an adult.
    If the person is age 65 or older, print a message that the person is an elder.
    """
    age = 28
    if age < 2:
        print("The person is a baby👼.")
    elif age < 4:
        print("The person is a toddler.")
    elif age < 13:
        print("The person is a kid.")
    elif age < 20:
        print("The person is a teenager.")
    elif age < 65:
        print("The person is a adult.")
    else:
        print("The person is an elder.")
    return f"The stages of life function executed.\n"


def favourite_fruits():
    """
    Favorite Fruit: Make a list of your favorite fruits, and then write a series of
    independent if statements that check for certain fruits in your list.
    Make a list of your three favorite fruits and call it favorite_fruits.
    Write five if statements. Each should check whether a certain kind of fruit is in your
    list. If the fruit is in your list, the if block should print a statement, such as You really
    like bananas!
    """
    fav_fruits = ["bananas", "guava", "orange", "water melon", "mango"]
    fruit = "bananas"
    res = ""
    for i in fav_fruits:
        if i == fruit:
            res = i
            break
    if res:
        return f"You really like {res}."
    else:
        return "Fruit not found in the favourite fruits list."


if __name__ == "__main__":
    print(alien_colors())
    print(alien_colors_two())
    print(alien_colors_three())
    print(stages_of_life())
    print(favourite_fruits())
