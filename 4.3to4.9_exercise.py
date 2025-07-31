"""
4-3. Counting to Twenty: Use a for loop to print the numbers from 1 to 20, inclusive.
4-4. One Million: Make a list of the numbers from one to one million, and then use a
for loop to print the numbers. (If the output is taking too long, stop it by pressing CTRLC or by closing the output window.)
4-5. Summing a Million: Make a list of the numbers from one to one million, and then
use min() and max() to make sure your list actually starts at one and ends at one
million. Also, use the sum() function to see how quickly Python can add a million
numbers.
4-6. Odd Numbers: Use the third argument of the range() function to make a list of the
odd numbers from 1 to 20. Use a for loop to print each number.
4-7. Threes: Make a list of the multiples of 3, from 3 to 30. Use a for loop to print the
numbers in your list.
4-8. Cubes: A number raised to the third power is called a cube. For example, the cube
of 2 is written as 2**3 in Python. Make a list of the first 10 cubes (that is, the cube of
each integer from 1 through 10), and use a for loop to print out the value of each cube.
4-9. Cube Comprehension: Use a list comprehension to generate a list of the first 10
cubes.
"""


def count_to_twenty():
    """
    Use a for loop to print the numbers from 1 to 20, inclusive.
    """
    for i in range(1, 21):
        print(i)
    return f"Count from 1 to 20 completed\n"


def one_million():
    """
    Make a list of the numbers from one to one million, and then use a
    for loop to print the numbers. (If the output is taking too long, stop it by pressing CTRLC or by closing the output window.)
    """
    million_numbers = list(range(1, 1000001))
    for i in million_numbers:
        print(i)
    return f"The counting completed\n"


def summing_a_million():
    """Make a list of the numbers from one to one million, and then
        use min() and max() to make sure your list actually starts at one and ends at one
        million. Also, use the sum() function to see how quickly Python can add a million
        numbers.
    """
    one_million_nums = list(range(1, 1000001))
    print(f"Max of million:{max(one_million_nums)}")
    print(f"Min of million:{min(one_million_nums)}")
    print(f"Sum of million:{sum(one_million_nums)}")
    return f"Summing a million completed\n"


def odd_numbers():
    """
    Use the third argument of the range() function to make a list of the
    odd numbers from 1 to 20. Use a for loop to print each number.
    """
    oddnumbers = list(range(1, 20, 2))
    for i in oddnumbers:
        print(i)
    return "Odd numbers printing with step completed.\n"

# A multiple is the product of the 3 and any integer like 3x5=15, here 15=multiple,3 and 5 are factors or divisors


def threes():
    """
    Make a list of the multiples of 3, from 3 to 30. Use a for loop to print the
    numbers in your list.
    """
    multiples = list(range(3, 31, 3))
    for i in multiples:
        print(i)
    return f"Forming the list of multiples of 3 completed\n"


def cubes():
    """
    A number raised to the third power is called a cube. For example, the cube
    of 2 is written as 2**3 in Python. Make a list of the first 10 cubes (that is, the cube of
    each integer from 1 through 10), and use a for loop to print out the value of each cube.
    """
    cube_of_10_nums = []
    for i in range(1, 11):
        cube_of_10_nums.append(i**3)
        print(i**3)
    return f"Cube of first 10 numbers implemented.{cube_of_10_nums}\n"


def cube_comprehension():
    """
    Use a list comprehension to generate a list of the first 10
    cubes.
    """
    return [i**3 for i in range(1, 11)]


if __name__ == "__main__":
    print(count_to_twenty())
    # print(one_million())# since it's taking more time I commented this line
    print(summing_a_million())
    print(odd_numbers())
    print(threes())
    print(cubes())
    print(cube_comprehension())
