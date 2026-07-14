"""Given a positive integer, return the number of steps it takes to reach 1 according to the rules of the Collatz Conjecture."""

def steps(x):
    """
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
    return(count)

 
