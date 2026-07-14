"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2


def bake_time_remaining(elapsed_bake_time):
    """
calculate the bake_time_remaining.

Parameter:
elapsed_bake_time (int) : the baking time already elapsed

return:
int : How much bake time is remaining

This function takes one integer representing the time already spent baking the lasagna. 
It calculates the remaining bake time (expected bake time - elapsed bake time)."""
    
    return (EXPECTED_BAKE_TIME - elapsed_bake_time)



def preparation_time_in_minutes(number_of_layers):
    """Calculate the preparation_time_in_minutes.

Parameters:
number_of_layers (int): The number of layers in the lasagna.

Return:
int: How much timr will it take to prepare each layer of lasagna

This returns how many minutes you would spend making them. Assume each layer takes 2 minutes to prepare."""
    
    return (number_of_layers * PREPARATION_TIME)



def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the elapsed cooking time.
    
    Parameters:
        number_of_layers (int): The number of layers in the lasagna.
        elapsed_bake_time (int): Time the lasagna has been baking in the oven.
    
    Returns:
        int: The total time elapsed (in minutes) preparing and baking.

    This function takes two integers representing the number of lasagna 
    layers and the time already spent baking the lasagna. It calculates 
    the total elapsed minutes spent cooking (preparing + baking)."""
    
    return ((number_of_layers * PREPARATION_TIME) + elapsed_bake_time )
    
