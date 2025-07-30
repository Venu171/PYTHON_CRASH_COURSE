"""
Save each of the following exercises as a separate file, with a name like
name_cases.py. If you get stuck, take a break or see the suggestions in Appendix C.

2-3. Personal Message: Use a variable to represent a person’s name, and print a
message to that person. Your message should be simple, such as, “Hello Eric, would
you like to learn some Python today?”

2-4. Name Cases: Use a variable to represent a person’s name, and then print that
person’s name in lowercase, uppercase, and title case.

2-5. Famous Quote: Find a quote from a famous person you admire. Print the quote
and the name of its author. Your output should look something like the following,
including the quotation marks:
Albert Einstein once said, “A person who never made a mistake never tried
anything new.”

2-6. Famous Quote 2: Repeat Exercise 2-5, but this time, represent the famous
person’s name using a variable called famous_person. Then compose your message
and represent it with a new variable called message. Print your message.

2-7. Stripping Names: Use a variable to represent a person’s name, and include some
whitespace characters at the beginning and end of the name. Make sure you use each
character combination, "\t" and "\n", at least once.
Print the name once, so the whitespace around the name is displayed. Then print the
name using each of the three stripping functions, lstrip(), rstrip(), and strip().

2-8. File Extensions: Python has a removesuffix() method that works exactly like
removeprefix(). Assign the value 'python_notes.txt' to a variable called filename.
Then use the removesuffix() method to display the filename without the file extension,
like some file browsers do.
"""


def personal_message():
    """Use a variable to represent a person’s name, and print a
    message to that person. Your message should be simple, such as, “Hello Eric, would
    you like to learn some Python today?"""
    person_name = "Venu"
    message = f"==Exercise:2.3==\nHello {person_name}, would you like to learn some Python today?"
    return message


def name_cases():
    """
    Use a variable to represent a person’s name, and then print that
    person’s name in lowercase, uppercase, and title case.
    """
    person_name = "Venu Pelluru"
    result = f"==Exercise:2.4==\nThe result of person's name({person_name})) in \nLowercase:{person_name.lower()}\nUppercase:{person_name.upper()}\nTitlecase:{person_name.title()}"
    return result


def famous_quote():
    """
    Find a quote from a famous person you admire. Print the quote
    and the name of its author. Your output should look something like the following,
    including the quotation marks:
    Albert Einstein once said, “A person who never made a mistake never tried
    anything new.
    """
    person_name = ""
    person_quote = "If you want to shine like a sun, first burn like a sun."
    return f"==Exercise:2.5==\nAPJ Abdul Kalam once said, \"{person_quote}\""


def famous_quote_two():
    """
    Repeat Exercise 2-5, but this time, represent the famous
    person’s name using a variable called famous_person. Then compose your message
    and represent it with a new variable called message. Print your message.
    """
    person_name = "APJ Abdul Kalam"
    person_quote = "If you want to shine like a sun, first burn like a sun."
    return f"==Exercise:2.6==\n{person_name} once said, \"{person_quote}\""


def strip_names():
    """
    Use a variable to represent a person’s name, and include some
    whitespace characters at the beginning and end of the name. Make sure you use each
    character combination, "\t" and "\n", at least once.
    Print the name once, so the whitespace around the name is displayed. Then print the
    name using each of the three stripping functions, lstrip(), rstrip(), and strip().
    """
    person_name = " Pelluru\n Venu\t Pelluru "
    print("==Exercise 2.7==")
    print(person_name)
    print(f"Using the lstrip():{person_name.lstrip()}")
    print(f"Using the rstrip():{person_name.rstrip()}")
    print(f"Using the strip():{person_name.strip()}")


def file_extensions():
    """
    Python has a removesuffix() method that works exactly like
    removeprefix(). Assign the value 'python_notes.txt' to a variable called filename.
    Then use the removesuffix() method to display the filename without the file extension,
    like some file browsers do.
    """
    filename = "python_notes.txt"
    return f"==Exercise 2.8==\nThe file name after removing the suffix:\n{filename.removesuffix(".txt")}"


if __name__ == '__main__':
    print(personal_message())
    print(name_cases())
    print(famous_quote())
    print(famous_quote_two())
    print(strip_names())
    print(file_extensions())
