""""
The following exercises are a bit more complex than those in Chapter 2, but they give
you an opportunity to use lists in all of the ways described.

3-4. Guest List: If you could invite anyone, living or deceased, to dinner, who would
you invite? Make a list that includes at least three people you’d like to invite to dinner.
Then use your list to print a message to each person, inviting them to dinner.

3-5. Changing Guest List: You just heard that one of your guests can’t make the
dinner, so you need to send out a new set of invitations. You’ll have to think of
someone else to invite.
Start with your program from Exercise 3-4. Add a print() call at the end of your
program, stating the name of the guest who can’t make it.
Modify your list, replacing the name of the guest who can’t make it with the name of the
new person you are inviting.
Print a second set of invitation messages, one for each person who is still in your list.

3-6. More Guests: You just found a bigger dinner table, so now more space is
available. Think of three more guests to invite to dinner.
Start with your program from Exercise 3-4 or 3-5. Add a print() call to the end of your
program, informing people that you found a bigger table.
Use insert() to add one new guest to the beginning of your list.
Use insert() to add one new guest to the middle of your list.
Use append() to add one new guest to the end of your list.
Print a new set of invitation messages, one for each person in your list.

3-7. Shrinking Guest List: You just found out that your new dinner table won’t arrive in
time for the dinner, and now you have space for only two guests.
Start with your program from Exercise 3-6. Add a new line that prints a message saying
that you can invite only two people for dinner.
Use pop() to remove guests from your list one at a time until only two names remain in
your list. Each time you pop a name from your list, print a message to that person
letting them know you’re sorry you can’t invite them to dinner.
Print a message to each of the two people still on your list, letting them know they’re
still invited.
Use del to remove the last two names from your list, so you have an empty list. Print
your list to make sure you actually have an empty list at the end of your program.
"""


def guess_list():
    """
    If you could invite anyone, living or deceased, to dinner, who would
    you invite? Make a list that includes at least three people you’d like to invite to dinner.
    Then use your list to print a message to each person, inviting them to dinner.
    Start with your program from Exercise 3-4. Add a print() call at the end of your
    program, stating the name of the guest who can’t make it.
    Modify your list, replacing the name of the guest who can’t make it with the name of the
    new person you are inviting.
    Print a second set of invitation messages, one for each person who is still in your list.
    """
    message = "You are cordially invited to a dinner party at our home on Saturday at 7 PM. We would be delighted if you could join us."
    fav_members = ["John", "Jack", "Wellington"]
    return f"==Exercise 3.4==\nHello, {fav_members[0]}.{message}.\nHello, {fav_members[1]}.{message}.\nHello, {fav_members[2]}.{message}."


def changing_guest_list():
    """
    Changing Guest List: You just heard that one of your guests can’t make the
    dinner, so you need to send out a new set of invitations. You’ll have to think of
     someone else to invite.
    """
    message = "You are cordially invited to a dinner party at our home on Saturday at 7 PM. We would be delighted if you could join us."
    fav_members = ["John", "Jack", "Wellington"]
    print(f"==Exercise 3.5==\nBefore change:\n{fav_members}")
    removed_member = fav_members.pop(0)
    fav_members.insert(0, 'Jemi')
    print(f"After change:\n{fav_members}")
    return f"Hello, {fav_members[0]}.{message}.\nHello, {fav_members[1]}.{message}.\nHello, {fav_members[2]}.{message}.\n{removed_member} can't make it to the dinner...."


def more_guest_list():
    """
    You just found a bigger dinner table, so now more space is
    available. Think of three more guests to invite to dinner.
    Start with your program from Exercise 3-4 or 3-5. 
    Add a print() call to the end of your program, informing people that you found a bigger table.
    Use `insert()` to add one new guest to the beginning of your list.
    Use `insert()` to add one new guest to the middle of your list.
    Use `append()` to add one new guest to the end of your list.
    Print a new set of invitation messages, one for each person in your list.
    """
    print("==Exercise 3.6==")
    message = "You are cordially invited to a dinner party at our home on Saturday at 7 PM. We would be delighted if you could join us."
    fav_members = ["John", "Jack", "Wellington"]
    print(f"Before Change: {fav_members}")
    fav_members.insert(0, "Harry")
    fav_members.insert(len(fav_members)//2, "Jim Carey")
    fav_members.append("Reynold")
    print(f"After Change: {fav_members}")
    return f"""Hello, "{fav_members[0]}".{message}.\nHello, "{fav_members[1]}".{message}.\nHello, "{fav_members[2]}".{message}.\nHello, "{fav_members[3]}".{message}.\nHello, "{fav_members[4]}".{message}.\nHello, "{fav_members[5]}".{message}."""


def shrinking_guest_list():
    """
    You just found out that your new dinner table won’t arrive in
    time for the dinner, and now you have space for only two guests.
    Start with your program from Exercise 3-6. Add a new line that prints a message saying
    that you can invite only two people for dinner.
    Use pop() to remove guests from your list one at a time until only two names remain in
    your list. Each time you pop a name from your list, print a message to that person
    letting them know you’re sorry you can’t invite them to dinner.
    Print a message to each of the two people still on your list, letting them know they’re
    still invited.
    Use del to remove the last two names from your list, so you have an empty list. Print
    your list to make sure you actually have an empty list at the end of your program. 
    """
    fav_members = ['Harry', 'John', 'Jim Carey',
                   'Jack', 'Wellington', 'Reynold']
    message = "You are cordially invited to a dinner party at our home on Saturday at 7 PM. We would be delighted if you could join us."
    print(f"==Exercise 3.7==\nSorry for the inconvenience.Only \"two\" members are allowed to be invited.")
    removed_member_one = fav_members.pop()
    print(
        f"Sorry for the inconvenience.Dinner cancelled for {removed_member_one} as there is space for two people only.")
    removed_member_two = fav_members.pop()
    print(
        f"Sorry for the inconvenience.Dinner cancelled for {removed_member_two} as there is space for two people only.")
    removed_member_three = fav_members.pop()
    print(
        f"Sorry for the inconvenience.Dinner cancelled for {removed_member_three} as there is space for two people only.")
    removed_member_four = fav_members.pop()
    print(
        f"Sorry for the inconvenience.Dinner cancelled for {removed_member_four} as there is space for two people only.")
    print(
        f"Hello, \"{fav_members[0]}\".{message}.\nHello, \"{fav_members[1]}\".{message}.")
    del fav_members[0]
    del fav_members[0]
    print(f"The final list contains {len(fav_members)} members")
    return f"Dinner successfully completed"


if __name__ == "__main__":
    print(guess_list())
    print(changing_guest_list())
    print(more_guest_list())
    print(shrinking_guest_list())
