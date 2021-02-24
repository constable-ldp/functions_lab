def return_10():
    return 10


def add(number_1, number_2):
    return number_1 + number_2


def subtract(number_1, number_2):
    return number_1 - number_2


def multiply(number_1, number_2):
    return number_1 * number_2


def divide(number_1, number_2):
    return number_1 / number_2


def length_of_string(string):
    return len(string)


def join_string(string_1, string_2):
    return string_1 + string_2


def add_string_as_number(string_1, string_2):
    return int(string_1) + int(string_2)


def number_to_full_month_name(month_number):
    months = ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December']
    for i in range(1, len(months)+1):
        if month_number == i:
            return months[i-1]


def number_to_short_month_name(month_number):
    return number_to_full_month_name(month_number)[:3]


def volume_of_cube(length_of_side):
    return length_of_side ** 3


def reverse_string(string):
    return string[::-1]

# F − 32) × 5/9 = C


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9
