"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


EXPECTED_BAKE_TIME = 40
PREPARAION_TIME = 30

def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(number_of_layers):
    """Calculate the preparation time in minutes.

    :param number_of_layers: int - number of layers you want to add to lasagna.
    :return: int - minutes you would spend making them.

    Function that takes the number of layers to be added to the lasagna as
    an argument and returns how many minutes will be spent on making them.
    Assuming each layer takes 2 minutes to prepare.
    """
    return 2 * number_of_layers


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time = PREPARAION_TIME):
    """Calculate the preparation time in minutes.

    :param number_of_layers: int - number of layers you want to add to lasagna.
    :param elapsed_bake_time: int - number of minutes lasagna has spend baking in the oven already.
    :return: int - total minutes in the kitchen cooking

    Function that takes 2 parameters as arguments:
    the number of layers to be added to the lasagna and
    the number of minutes the lasagna has spent baking in the oven already
    Returns total minutes in the kitchen cooking - 
    preparation time layering + the time the lasagna has spend baking in the oven.
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time