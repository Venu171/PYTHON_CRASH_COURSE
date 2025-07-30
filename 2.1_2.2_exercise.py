"""
Write a separate program to accomplish each of these exercises. Save each program
with a filename that follows standard Python conventions, using lowercase letters and
underscores, such as simple_message.py and simple_messages.py.

2-1. Simple Message: Assign a message to a variable, and then print that message.
2-2. Simple Messages: Assign a message to a variable, and print that message. Then
change the value of the variable to a new message, and print the new message.
"""
# 2.1 Simple Message: Assign a message to a variable, and then print that message.


def simple_message():
    message = f"==Exercise 2.1==\nWelcome, to the world of Python🐍!"
    print(message)


def simple_messages():
    message = f"==Exercise 2.2==\nBefore:\nWelcome, to the world of Python🐍!"
    print(message)
    message = f"After:\nHello, Python!"
    print(message)


# we use this to give indication of the function is running from a different file/module.
if __name__ == '__main__':
    print("Running from the same page")
    simple_message()
    simple_messages()
