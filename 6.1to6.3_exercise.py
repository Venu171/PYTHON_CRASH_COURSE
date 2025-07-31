def person():
    """
    Use a dictionary to store information about a person you know. Store their
    first name, last name, age, and the city in which they live. You should have keys such
    as first_name, last_name, age, and city. Print each piece of information stored in your
    dictionary.
    """
    personal_info = {"first_name": "Venu",
                     "last_name": "Pelluru", "age": 28, "city": "Srikalahasti"}
    return personal_info


def favourite_numbers():
    """
    Use a dictionary to store people’s favorite numbers. Think of
    five names, and use them as keys in your dictionary. Think of a favorite number for
    each person, and store each as a value in your dictionary. Print each person’s name
    and their favorite number. For even more fun, poll a few friends and get some actual
    data for your program.
    """
    print("")
    people_fav_nums = {"venu": 9, "messi": 10,
                       "rdp": 14, "ronaldo": 7, "lukamodric": 30}
    for i in people_fav_nums.keys():
        print(f"{i} : {people_fav_nums[i]}")
    return f"\n==Favourite Numbers function executed.==\n"


def glossary():
    """
    A Python dictionary can be used to model an actual dictionary.
    However, to avoid confusion, let’s call it a glossary.
    Think of five programming words you’ve learned about in the previous chapters. Use
    these words as the keys in your glossary, and store their meanings as values.
    Print each word and its meaning as neatly formatted output. You might print the word
    followed by a colon and then its meaning, or print the word on one line and then print
    its meaning indented on a second line. Use the newline character (\n) to insert a blank
    line between each word-meaning pair in your output.
    """
    glossary_dict = dict()
    glossary_dict["print"] = "used for printing the output to terminal"
    glossary_dict["list"] = "used for storing the different data types as collectives"
    glossary_dict["dictionary"] = "used for storing the relatable info as keys and values"
    glossary_dict["tuple"] = "used for storing the different data types as collectives but immutable"
    glossary_dict["if-elif-else"] = "used for making decisions with different conditions."
    for i in glossary_dict.keys():
        print(f"{i} : {glossary_dict[i]}")
    return f"\n==Glossary function executed.\n"


if __name__ == "__main__":
    print(person())
    print(favourite_numbers())
    print(glossary())
