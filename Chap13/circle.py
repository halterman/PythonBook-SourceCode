class Circle:
    """  Represents a geometric circle object  """
    def __init__(self, center, radius):
        """  Initalize the center's center and radius  """
        # Disallow a negative radius
        if radius < 0:
            raise ValueError('Negative radius')
        self.center = center
        self.radius = radius

    def get_radius(self):
        """  Return the radius of the circle """
        return self.radius

    def get_center(self):
        """  Return the coordinatess of the center """
        return self.center

    def get_area(self):
        """  Compute and return the area of the circle  """
        from math import pi
        return pi*self.radius*self.radius

    def get_circumference(self):
        """  Compute and return the circumference of the circle  """
        from math import pi
        return 2*pi*self.radius

    def move(self, pt):
        """  Moves the enter of the circle to point pt """
        self.center = pt

    def grow(self):
        """  Increases the radius of the circle """
        self.radius += 1

    def shrink(self):
        """  Decreases the radius of the circle;
             does not affect a circle with radius zero  """
        if self.radius > 0:
            self.radius -= 1
