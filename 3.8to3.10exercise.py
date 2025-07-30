"""
3-8. Seeing the World: Think of at least five places in the world you’d like to visit.
Store the locations in a list. Make sure the list is not in alphabetical order.
Print your list in its original order. Don’t worry about printing the list neatly; just print it
as a raw Python list.
Use sorted() to print your list in alphabetical order without modifying the actual list.
Show that your list is still in its original order by printing it.
Use sorted() to print your list in reverse-alphabetical order without changing the order
of the original list.
Show that your list is still in its original order by printing it again.
Use reverse() to change the order of your list. Print the list to show that its order has
changed.
Use reverse() to change the order of your list again. Print the list to show it’s back to its
original order.
Use sort() to change your list so it’s stored in alphabetical order. Print the list to show
that its order has been changed.
Use sort() to change your list so it’s stored in reverse-alphabetical order. Print the list
to show that its order has changed.
3-9. Dinner Guests: Working with one of the programs from Exercises 3-4 through 3-7
(pages 41–42), use len() to print a message indicating the number of people you’re
inviting to dinner.
3-10. Every Function: Think of things you could store in a list. For example, you could
make a list of mountains, rivers, countries, cities, languages, or anything else you’d
like. Write a program that creates a list containing these items and then uses each
function introduced in this chapter at least once.
"""


def seeing_the_world():
    """
    Seeing the World: Think of at least five places in the world you’d like to visit.
    Store the locations in a list. Make sure the list is not in alphabetical order.
    Print your list in its original order. Don’t worry about printing the list neatly; just print it
    as a raw Python list.
    Use sorted() to print your list in alphabetical order without modifying the actual list.
    Show that your list is still in its original order by printing it.
    Use sorted() to print your list in reverse-alphabetical order without changing the order
    of the original list.
    Show that your list is still in its original order by printing it again.==
    Use reverse() to change the order of your list. Print the list to show that its order has
    changed.
    Use reverse() to change the order of your list again. Print the list to show it’s back to its
    original order.
    Use sort() to change your list so it’s stored in alphabetical order. Print the list to show
    that its order has been changed.
    Use sort() to change your list so it’s stored in reverse-alphabetical order. Print the list
    to show that its order has changed.
    """
    places = ["Sabarimala", "Tiruttani",
              "Tiruchandur", "Marudhamalai", "Pazhani"]
    print(f"Original order: {places}")
    temp_sorted_list = sorted(places)
    print(f"Temporarily Sorted Alphabetical List: {temp_sorted_list}")
    print(f"After sorting temporarily: {places}")
    temp_sorted_list_rev = sorted(places, reverse=True)
    print(
        f"Temporarily Sorted Reverse Alphabetical List: {temp_sorted_list_rev}")
    print(f"After sorting temporarily: {places}")
    places.reverse()
    print(f"After reversing permanantly: {places}")
    places.reverse()
    print(f"After reverse reversing permanantly: {places}")
    places.sort()
    print(f"After reverse sorting permanantly: {places}")
    places.sort(reverse=True)
    print(f"After reverse sorting permanantly: {places}")
    return "Sort completed successfully"


def dinner_guests():
    """
    Working with one of the programs from Exercises 3-4 through 3-7
   (pages 41–42), use len() to print a message indicating the number of people you’re
    inviting to dinner.
    """
    fav_members = ['Harry', 'John', 'Jim Carey',
                   'Jack', 'Wellington', 'Reynold']
    return f"The number of invitees for the Dinner is: {len(fav_members)}"


def every_function_list():
    """
    Think of things you could store in a list. For example, you could
    make a list of mountains, rivers, countries, cities, languages, or anything else you’d
    like. Write a program that creates a list containing these items and then uses each
    function introduced in this chapter at least once.
    """
    desired_list_of_rivers = ["Kaveri", "Krishna",
                              "Godavari", "Thungabhadra", "Ganga"]
    return desired_list_of_rivers


if __name__ == "__main__":
    print(seeing_the_world())
    print(dinner_guests())
    print(every_function_list())
