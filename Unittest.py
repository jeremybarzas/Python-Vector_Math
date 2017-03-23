'''unittesting for vector math'''

from Vector2 import Vector2

def unit_test():
    '''unit test'''
    vec2a = Vector2([1, 2])
    vec2b = Vector2([3, 4])

    print "\nAddition"
    add = vec2a.add(vec2b)
    add.print_info()

    print "\nSubtraction"
    sub = vec2a.subtract(vec2b)
    sub.print_info()

    print "\nScalar Multiplication"
    mult = vec2a.scalarmult(5)
    mult.print_info()

    print "\nMagnitude"
    print vec2a.magnitude()

    print "\nNormalize"
    norm = vec2a.normalize()
    norm.print_info()

    print "\nDot Product"
    print vec2a.dotproduct(vec2b)


if __name__ == "__main__":
    unit_test()
