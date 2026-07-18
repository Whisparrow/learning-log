"""Determine whether a given year is a leap year."""
def leap_year(year):
    """Return True if the year is a leap year, False otherwise.

    A year is a leap year if it's divisible by 4, except century
    years (divisible by 100), which are only leap years if they're
    also divisible by 400."""
    return (
        year % 4 == 0 and 
        year % 100 != 0 or 
        year % 400 == 0
    )