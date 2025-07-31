def glossary_two():
    """
    Now that you know how to loop through a dictionary, clean up the
    code from Exercise 6-3 (page 99) by replacing your series of print() calls with a loop
    that runs through the dictionary’s keys and values. When you’re sure that your loop
    works, add five more Python terms to your glossary. When you run your program again,
    these new words and meanings should automatically be included in the output.
    """
    glossary_dict = dict()
    glossary_dict = dict()
    glossary_dict["print"] = "used for printing the output to terminal"
    glossary_dict["list"] = "used for storing the different data types as collectives"
    glossary_dict["dictionary"] = "used for storing the relatable info as keys and values"
    glossary_dict["tuple"] = "used for storing the different data types as collectives but immutable"
    glossary_dict["if-elif-else"] = "used for making decisions with different conditions."
    for i, j in glossary_dict.items():
        print(f"{i} : {j}")
    return f"\n==Glossary function  two executed.\n"


def rivers():
    """
    Make a dictionary containing three major rivers and the country each river
    runs through. One key-value pair might be 'nile': 'egypt'.
    Use a loop to print a sentence about each river, such as The Nile runs through Egypt.
    Use a loop to print the name of each river included in the dictionary.
    Use a loop to print the name of each country included in the dictionary.
    """
    rivers = {"nile": "egypt", "bramhaputra": "india", "nebel": "germany"}
    for i, j in rivers.items():
        print(f"The {i.title()} runs through {j}.")
    print()
    for i in rivers.keys():
        print(i)
    print()
    for i in rivers.values():
        print(i)
    return f"\nRivers function executed.\n"


def polling():
    """
    Use the code in favorite_languages.py (page 96).
    Make a list of people who should take the favorite languages poll. Include some names
    that are already in the dictionary and some that are not.
    Loop through the list of people who should take the poll. If they have already taken the
    poll, print a message thanking them for responding. If they have not yet taken the poll,
    print a message inviting them to take the poll.
    """
    favorite_languages = {
        'jen': 'python',
        'sarah': 'c',
        'edward': 'rust',
        'phil': 'python',
    }
    peoples = ["jen", "sarah", "edward", "phil", "John", "Jerry"]
    for i in peoples:
        if i in favorite_languages.keys():
            print(f"{i.title()}, thanks for responding in the survey.")
        else:
            print(f"{i.title()}, please join in the survey.")
    return f"\n==Pollin function executed==\n"


if __name__ == "__main__":
    print(glossary_two())
    print(rivers())
    print(polling())
