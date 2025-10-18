# Question 1

# Write a function that prints "Fizz" when the number is divisible by 3, "Buzz" when the number is divisible by 5
# and "FizzBuzz" when the number is divisible by both 3 and 5.
# If the number is not divisible by either 3 or 5, the function should return the number itself.


def fizz_buzz(number):
    """Returns Fizz if number is divisible by 3, Buzz if divisible by 5, FizzBuzz if divisible by both 3 and 5.
    If not divisible by either 3 or 5, returns the number itself.
    >>> fizz_buzz(3)
    'Fizz'
    >>> fizz_buzz(5)
    'Buzz'
    >>> fizz_buzz(15)
    'FizzBuzz'
    """
    return

# assignemnt 1.1 Q1

def fizz_buzz(number):
    if number % 3 == 0 and number % 5 == 0:
        return "FizzBuzz"
    elif number % 5 == 0:
        return "Buzz"
    elif number % 3 == 0:
        return "Fizz"
    else:
        return number

number = 9
print (fizz_buzz(number))
number = 10
print (fizz_buzz(number))
number = 10
print (fizz_buzz(number))
number = 16
print (fizz_buzz(number))


# Question 2

# Write a function that takes a list of numbers and returns the sum of the squares of all the numbers.

# assignemnt 1.1 Q2

def sum_of_squares(numbers):
    """Returns the sum of the squares of all the numbers in a list.
    >>> sum_of_squares([1, 2, 3])
    14
    >>> sum_of_squares([2, 4, 6])
    56
    """
    return

def sum_of_squares(numbers):
   return sum([number**2 for number in numbers])

numbers = [1 ,2 ,3]
print (sum_of_squares(numbers))

numbers = [2 ,4 ,6]
print (sum_of_squares(numbers))


# Question 3

# Write a function that counts the number of vowels in a string.


def count_vowels(string):
    """Returns the number of vowels in a string.
    >>> count_vowels("hello")
    2
    >>> count_vowels("aeiou")
    5
    """
    return


# assignemnt 1.1 Q3

def count_vowels(string):
    vowels = "aeiou"
    return len([word for word in string if word in vowels])


string = "hello"
print (count_vowels(string))
string = "aeiou"
print (count_vowels(string))
string = "kierun"
print (count_vowels(string))

# Question 4

# Write a function that counts the number of repeated characters in a string.


def count_repeats(string):
    """Returns the number of repeated characters in a string.
    >>> count_repeats("hello")
    2
    >>> count_repeats("aeiou")
    0
    """
    return

# assignemnt 1.1 Q4

def count_repeats(string):
    return len([word for word in string if string.count(word) > 1])

string = "hello"
print (count_repeats(string))
string = "aeiou"
print (count_repeats(string))
string = "Kiekie"
print (count_repeats(string))


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
