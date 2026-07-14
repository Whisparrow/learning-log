def square(number):
    """Calculating the number of grains of wheat on a chessboard
    Parameater:
    number: the number of the square
    Result:
    A chessboard has 64 squares. Square 1 has one grain, square 2 has two grains, square 3 has four grains, and so on, doubling each time"""
    if 1 <= number <= 64:
        return 2** (number - 1)
    raise ValueError("square must be between 1 and 64")


def total():
    return 2**64 - 1
