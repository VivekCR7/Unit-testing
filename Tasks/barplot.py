# pylint: disable=missing-function-docstring
# pylint: disable=missing-module-docstring

"""
Approach:

For this task we just need to plot the bar plot of the company registrations vs year
so, I just created a function get_the_dictionary(), and iterate over my dataset and
retrieved the no.of company registered respective to the year, where year is key and
the count is the values
eg: {"year":count"}

after getting the dictionary I created one more function for plotting graph in which
I used matplotlib's plt.bar() to plot the bar plot.

"""

from transform import get

dataset = get()


def get_the_dictionary(data):
    registration_dictionary = {}
    for ele in data:
        date = int('20'+ele['DATE_OF_REGISTRATION'][6:])
        if date not in registration_dictionary:
            registration_dictionary[date] = 1
        else:
            registration_dictionary[date] += 1

    keys = list(registration_dictionary.keys())
    values = list(registration_dictionary.values())

    return keys, values
