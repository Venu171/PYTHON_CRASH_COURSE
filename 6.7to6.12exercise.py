"""
6-7. People: Start with the program you wrote for Exercise 6-1 (page 98). Make two
 new dictionaries representing different people, and store all three dictionaries in a list
 called people. Loop through your list of people. As you loop through the list, print
 everything you know about each person.
 6-8. Pets: Make several dictionaries, where each dictionary represents a different pet.
 In each dictionary, include the kind of animal and the owner’s name. Store these
 dictionaries in a list called pets. Next, loop through your list and as you do, print
 everything you know about each pet.
 6-9. Favorite Places: Make a dictionary called favorite_places. Think of three names
 to use as keys in the dictionary, and store one to three favorite places for each person.
 To make this exercise a bit more interesting, ask some friends to name a few of their
 favorite places. Loop through the dictionary, and print each person’s name and their
 favorite places.
 6-10. Favorite Numbers: Modify your program from Exercise 6-2 (page 98) so each
 person can have more than one favorite number. Then print each person’s name along
 with their favorite numbers.
 6-11. Cities: Make a dictionary called cities. Use the names of three cities as keys in
 your dictionary. Create a dictionary of information about each city and include the
 country that the city is in, its approximate population, and one fact about that city. The
 keys for each city’s dictionary should be something like country, population, and fact.
 Print the name of each city and all of the information you have stored about it.
 6-12. Extensions: We’re now working with examples that are complex enough that
 they can be extended in any number of ways. Use one of the example programs from
 this chapter, and extend it by adding new keys and values, changing the context of the
 program, or improving the formatting of the output.
"""


def people():
    """
    Start with the program you wrote for Exercise 6-1 (page 98). Make two
    new dictionaries representing different people, and store all three dictionaries in a list
    called people. Loop through your list of people. As you loop through the list, print
    everything you know about each person.
    """
    venu_info = {"first_name": "Venu",
                 "last_name": "Pelluru", "age": 28, "city": "Srikalahasti"}
    messi_info = {
        "first_name": "Lionel", "last_name": "Messi", "age": 36, "city": "Rosario"
    }
    mcallister_info = {
        "first_name": "Alexis", "last_name": "Mcallister", "age": 27, "city": "River Plate"
    }
    people = [venu_info, messi_info, mcallister_info]
    for i in people:
        print(f"{i}")
    return f"\n==People Function implemented.==\n"


def pets():
    """
    Make several dictionaries, where each dictionary represents a different pet.
    In each dictionary, include the kind of animal and the owner’s name. Store these
    dictionaries in a list called pets. Next, loop through your list and as you do, print
    everything you know about each pet.
    """
    dog_pet = {"name": "charlie", "type": "dog", "owner_name": "rakshit"}
    parrot_pet = {"name": "thomas", "type": "parrot", "owner_name": "kajal"}
    anil_pet = {"name": "anil", "type": "squirrel", "owner_name": "vijay"}
    pets = [dog_pet, parrot_pet, anil_pet]
    for i in pets:
        print(i)
    return f"\n==Pets function implemented.==\n"


def favourite_places():
    """
    Make a dictionary called favorite_places. Think of three names
    to use as keys in the dictionary, and store one to three favorite places for each person.
    To make this exercise a bit more interesting, ask some friends to name a few of their
    favorite places. Loop through the dictionary, and print each person’s name and their
    favorite places.
    """
    print("`Person's Name` : `Favourite Place`")
    favourite_places = {
        "venu": "chandragirifort", "messi": "tirumala tirupati temple", "suarez": "srikalahasti temple"
    }
    for key, value in favourite_places.items():
        print(f"{key.title()} : {value.title()}")
    return f"\n==Favourite places function implemented.==\n"


def favourite_numbers():
    """
    Modify your program from Exercise 6-2 (page 98) so each
    person can have more than one favorite number. Then print each person’s name along
    with their favorite numbers.
    """
    people_fav_nums = {"venu": [9, 3, 1], "messi": [10, 19],
                       "rdp": [14, 30, 45], "ronaldo": [7, 11, 89, 34], "lukamodric": [30, 99]}
    for i, j in people_fav_nums.items():
        print(f"{i}'s favourite numbers are:")
        for ii in j:
            print(ii)
    return f"\n==Favourite numbers function implemented.==\n"


def cities():
    """
    Make a dictionary called cities. Use the names of three cities as keys in
    your dictionary. Create a dictionary of information about each city and include the
    country that the city is in, its approximate population, and one fact about that city. The
    keys for each city’s dictionary should be something like country, population, and fact.
    Print the name of each city and all of the information you have stored about it.
    """
    cities = {"chennai":
              {"country": "India",
               "population": 8000000,
               "fact": "formerly called as madras"},
              "mumbai": {
                  "country": "India",
                  "population": 20000000,
                  "fact": "formerly called as bombay"
              },
              "beijing": {
                  "country": "China",
                  "population": 65000000,
                  "fact": "capital of china"
              }
              }
    for key, value in cities.items():
        print(f"{key.capitalize()}'s information:\n")
        country = value["country"]
        population = value["population"]
        fact = value["fact"]
        print(
            f"Country : {country}\nPopulation : {population}\nFact : {fact}.\n")
    return f"\n==Cities function implemented.==\n"


def extensions():
    """
    We’re now working with examples that are complex enough that
    they can be extended in any number of ways. Use one of the example programs from
    this chapter, and extend it by adding new keys and values, changing the context of the
    program, or improving the formatting of the output.
    """
    venu_info = {"first_name": "Venu",
                 "last_name": "Pelluru", "age": 28, "city": "Srikalahasti"}
    venu_info["graduation_year"] = 2019
    print(f"Information: {venu_info}")
    return f"Extensions function executed"


if __name__ == "__main__":
    print(people())
    print(pets())
    print(favourite_places())
    print(favourite_numbers())
    print(cities())
    print(extensions())
