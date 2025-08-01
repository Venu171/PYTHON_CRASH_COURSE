"""
8-1. Message: Write a function called display_message() that prints one sentence
 telling everyone what you are learning about in this chapter. Call the function, and
 make sure the message displays correctly.
 8-2. Favorite Book: Write a function called favorite_book() that accepts one
 parameter, title. The function should print a message, such as One of my favorite
 books is Alice in Wonderland. Call the function, making sure to include a book title as
 an argument in the function call.
"""


def display_message():
    """
    Write a function called display_message() that prints one sentence
    telling everyone what you are learning about in this chapter. Call the function, and
    make sure the message displays correctly.
    """
    return "You are learning about functions in this chapter."


def favorite_book(title):  # params
    """
    Write a function called favorite_book() that accepts one
    parameter, title. The function should print a message, such as One of my favorite
    books is Alice in Wonderland. Call the function, making sure to include a book title as
    an argument in the function call.
    """
    return f"One of my favourite books is {title}."


if __name__ == "__main__":
    print(display_message())
    print(favorite_book("Atomic Habits"))  # argument
