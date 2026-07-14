"""determine whether a number is an Armstrong number"""
def is_armstrong_number(number):
    """this function will detirmine whether the nuber is armstrong number or not.
    parameter:
    number: The number which will be input
    result :
    it the input number is armstrong number it will give us boolean value"""
    total = 0
    for digit in str(number):
        total += int(digit) ** len(str(number))
    return number == total