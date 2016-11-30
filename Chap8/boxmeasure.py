from math import fabs

def surface_area(x1, y1, z1,  x2, y2, z2,  x3, y3, z3,  x4, y4, z4,
                 x5, y5, z5,  x6, y6, z6,  x7, y7, z7,  x8, y8, z8):
    """  Computes the surface area of a rectangular box
         (cuboid) defined by the 3D points (x,y,z) of
         its eight corners:

           7------8
          /|     /|
         3------4 |
         | |    | |
         | 5----|-6
         |/     |/ 
         1------2
    """ 

    # Local helper function to compute area
    def area(length, width):
        """  Computes the area of a length x width rectangle """
        return length * width

    # Main code for surface_area function
    # Compute area of front face
    length = fabs(x2 - x1)
    height = fabs(y3 - y1)
    front_area = area(length, height)
    # Compute area of side face
    width = fabs(z5 - z1)
    side_area = area(width, height)
    # Compute area of top face
    top_area = area(length, width)
    # Compute and return surface area: front/back,
    # left side/right side, and top/bottom faces
    return 2*front_area + 2*side_area + 2*top_area


def volume(length, width, height):
    """  Computes the volume of a rectangular box 
         (cuboid) defined by its length, width, and height """
    return length * width * height

def get_point(msg):
    """ Prints a message specified by msg and allows the user to 
        enter the (x, y, z) coordinates of a point.  Returns the 
        point as a tuple. """
    print(msg)
    x = float(input("Enter x coordinate: "))
    y = float(input("Enter y coordinate: "))
    z = float(input("Enter z coordinate: "))
    return x, y, z
    

#  Get the coordinates of the box's corners from the user
print('Enter the coordinates of each of the box\'s corners')
print('''
       7------8
      /|     /|
     3------4 |
     | |    | |
     | 5----|-6
     |/     |/ 
     1------2
      ''')
x1, y1, z1 = get_point('Corner 1')
x2, y2, z2 = get_point('Corner 2')
x3, y3, z3 = get_point('Corner 3')
x4, y4, z4 = get_point('Corner 4')
x5, y5, z5 = get_point('Corner 5')
x6, y6, z6 = get_point('Corner 6')
x7, y7, z7 = get_point('Corner 7')
x8, y8, z8 = get_point('Corner 8')

#  Compute the surface area of the box
print('Surface area:', surface_area(x1, y1, z1,  x2, y2, z2,
                                    x3, y3, z3,  x4, y4, z4,
                                    x5, y5, z5,  x6, y6, z6,
                                    x7, y7, z7,  x8, y8, z8))
#  Compute the volume of the box
ln = fabs(x2 - x1)  # Compute length
wd = fabs(z5 - z1)  # Compute width
ht = fabs(y3 - y1)  # Compute height
print('Volume:', volume(ln, wd, ht))
