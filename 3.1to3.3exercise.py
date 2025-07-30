"""
Try these short programs to get some firsthand experience with Python’s lists. You
might want to create a new folder for each chapter’s exercises, to keep them
organized.

3-1. Names: Store the names of a few of your friends in a list called names. Print each
person’s name by accessing each element in the list, one at a time.

3-2. Greetings: Start with the list you used in Exercise 3-1, but instead of just printing
each person’s name, print a message to them. The text of each message should be the
same, but each message should be personalized with the person’s name.

3-3. Your Own List: Think of your favorite mode of transportation, such as a
motorcycle or a car, and make a list that stores several examples. Use your list to print
a series of statements about these items, such as “I would like to own a Honda
motorcycle.”
"""


def names():
    """
    Store the names of a few of your friends in a list called names. Print each
    person’s name by accessing each element in the list, one at a time.
    """
    names = ["Jack", "John", "Abrahim"]
    return f"{names[0]}\n{names[1]}\n{names[2]}\n"


def greetings():
    """
    Start with the list you used in Exercise 3-1, but instead of just printing
    each person’s name, print a message to them. The text of each message should be the
    same, but each message should be personalized with the person’s name.
    """
    names = ["Jack", "John", "Abrahim"]
    return f"Hello {names[0]}, How are you?\nHello {names[1]}, How are you?\nHello {names[2]}, How are you?"


def your_own_list():
    """
    Think of your favorite mode of transportation, such as a
    motorcycle or a car, and make a list that stores several examples. Use your list to print
    a series of statements about these items, such as “I would like to own a Honda
    motorcycle.” 
    """
    motorcylcles = ["Honda", "Royal Enfield", "Suzuki"]
    return f"I would like to own a {motorcylcles[0]} motorcycle.\nI would like to own a {motorcylcles[1]} motorcycle.\nI would like to own a {motorcylcles[2]} motorcycle."


if __name__ == "__main__":
    print(names())
    print(greetings())
    print(your_own_list())
