def rule(sides):
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
    return sides[0]==sides[1]==sides[2] and rule(sides)
    
def isosceles(sides):
    return (sides[0]== sides[1] or sides[1]==sides[2] or sides[0]==sides[2]) and rule (sides)

def scalene(sides):
    return sides[0]!= sides[1] and sides[1]!=sides[2] and sides[0]!=sides[2] and rule (sides)