def rule(sides):
    """Check whether three side lengths can form a valid triangle.

    Returns False if any side is zero or negative, or if the sides
    fail the triangle inequality (any two sides must sum to at least
    the third). Otherwise returns True.
    """
    if (
        sides[0] <= 0 or 
        sides[1] <= 0 or 
        sides[2] <= 0 ):
        return False
    if(
        (sides[0] + sides[1] >= sides[2]) and 
        (sides[1] + sides[2] >= sides[0]) and
        (sides[0] + sides[2] >= sides[1]) ):
        return True
    else:
        return False



def equilateral(sides):
    """Return True if all three sides are equal and form a valid triangle."""
    return sides[0]==sides[1]==sides[2] and rule(sides)
    
def isosceles(sides):
    """Return True if at least two sides are equal and form a valid triangle."""
    return (sides[0]== sides[1] or sides[1]==sides[2] or sides[0]==sides[2]) and rule (sides)

def scalene(sides):
    """Return True if all three sides are different and form a valid triangle."""
    return sides[0]!= sides[1] and sides[1]!=sides[2] and sides[0]!=sides[2] and rule (sides)