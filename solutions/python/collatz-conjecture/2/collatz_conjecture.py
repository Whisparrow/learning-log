"""Given a positive integer, return the number of steps it takes to reach 1 according to the rules of the Collatz Conjecture."""

def steps(x):
    """
    this function will count how many steps will take to take certain number to 1
    
    parameater:
    x = is the input number
    
    process: 
    the program filter out all -ve int and 0
    if the x is even it will be devided 2 if its odd it will multiple x by 3 and add 1
    
    result:
    it will count and return the value of the number of ittaration its performing.
    
    """
    if x <= 0:
        raise ValueError("Only positive integers are allowed")
    count = 0
    while x != 1:
        if x % 2 == 0:
            x = x / 2
        else:
            x = 3 * x + 1
        count = count + 1
    return count

 
