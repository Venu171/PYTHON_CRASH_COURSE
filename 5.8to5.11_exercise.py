def hello_admin():
    """
    Make a list of five or more usernames, including the name 'admin'.
    Imagine you are writing code that will print a greeting to each user after they log in to a
    website. Loop through the list, and print a greeting to each user.
    If the username is 'admin', print a special greeting, such as Hello admin, would you like
    to see a status report?
    Otherwise, print a generic greeting, such as Hello Jaden, thank you for logging in
    again.
    """
    usernames = ["admin", "venu", "jack", "john", "james"]
    for i in usernames:
        if i == "admin":
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {i}, thank you for logging in again.")
    return f"\n===Hello admin function executed.===\n"


def no_users():
    """
    Add an if test to hello_admin.py to make sure the list of users is not
    empty.
    If the list is empty, print the message We need to find some users!
    Remove all of the usernames from your list, and make sure the correct message is
    printed.
    """
    # usernames = ["admin", "venu", "jack", "john", "james"]
    usernames = []
    if len(usernames):
        for i in usernames:
            if i == "admin":
                print("Hello admin, would you like to see a status report?")
            else:
                print(f"Hello {i}, thank you for logging in again.")
    else:
        print("We need to find some users.")
    return f"\n===No users function executed.===\n"


def checking_usernames():
    """
    Do the following to create a program that simulates how
    websites ensure that everyone has a unique username.
    Make a list of five or more usernames called current_users.
    Make another list of five usernames called new_users. Make sure one or two of the new
    usernames are also in the current_users list.
    Loop through the new_users list to see if each new username has already been used. If
    it has, print a message that the person will need to enter a new username. If a
    username has not been used, print a message saying that the username is available.
    Make sure your comparison is case insensitive. If 'John' has been used, 'JOHN' should
    not be accepted. (To do this, you’ll need to make a copy of current_users containing
    the lowercase versions of all existing users.)
    """
    # usernames = ["admin", "venu", "jack", "john", "james"]
    current_users = ["venu", "messi", "roberto", "xavi", "james"]
    new_users = ["fernandes", "rooney", "roberto", "xavi", "hakinmi"]
    for user in new_users:
        if user in current_users:
            print(f"`{user}` username is not available.")
        else:
            print(f"`{user}` username is available.")
    return f"\n===Checking users function executed.===\n"

# Ordinal numbers are numbers that indicate the position or rank of an object
# in a sequence, such as 1st, 2nd, 3rd, 4th, and so on


def ordinal_numbers():
    """
    Ordinal numbers indicate their position in a list, such as 1st or
    2nd. Most ordinal numbers end in th, except 1, 2, and 3.
    Store the numbers 1 through 9 in a list.Loop through the list.
    Use an if-elif-else chain inside the loop to print the proper ordinal ending for each
    number. Your output should read "1st 2nd 3rd 4th 5th 6th 7th 8th 9th", and each
    result should be on a separate line.
    """
    ordinal_nums = list(range(1, 10))
    for i in ordinal_nums:
        if i == 1:
            print("1st")
        elif i == 2:
            print("2nd")
        elif i == 3:
            print("3rd")
        else:
            print(f"{i}th")
    return f"\n===Ordinal Numbers function executed.===\n"


if __name__ == "__main__":
    print(hello_admin())
    print(no_users())
    print(checking_usernames())
    print(ordinal_numbers())
