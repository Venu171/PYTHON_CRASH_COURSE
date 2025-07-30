"""
2-9. Number Eight: Write addition, subtraction, multiplication, and division operations
that each result in the number 8. Be sure to enclose your operations in print() calls to
see the results. You should create four lines that look like this:
print(5+3)
Your output should be four lines, with the number 8 appearing once on each line.
2-10. Favorite Number: Use a variable to represent your favorite number. Then, using
that variable, create a message that reveals your favorite number. Print that message.
"""


def number_eight():
    """
    Write addition, subtraction, multiplication, and division operations
    that each result in the number 8. Be sure to enclose your operations in print() calls to
    see the results. You should create four lines that look like this:
    print(5+3)
    """
    return f"==Exercise2.9==\nUsing addition:{6+2}\nUsing subtraction:{10-2}\nUsing multiplication:{2*4}\nUsing float division:{16/2}\nUsing integer division:{16//2}"  # 8


def favourite_number():
    """
    Use a variable to represent your favorite number. Then, using
    that variable, create a message that reveals your favorite number. Print that message.
    """
    fav_num = 9
    return f"==Exercise 2.10==\nMy favourite number is {fav_num}"


if __name__ == '__main__':
    print(number_eight())
    print(favourite_number())
