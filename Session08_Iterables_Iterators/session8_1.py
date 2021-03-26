import math


class Polygon:
    def __init__(self, vertices: int, circumradius: float):
        if not isinstance(vertices, int):
            raise TypeError('Vertices must be of Type <int>')
        if not isinstance(circumradius, (float, int)):
            raise TypeError('Common Circumradius must be a number')
        if vertices < 3:
            raise ValueError('There must be atleast 3 Vertices for a Polygon')
        if circumradius <= 0:
            raise ValueError('Circumradius must be greater than 0')

        self.edges = vertices
        self.circumradius = circumradius

    @property
    def edges(self):
        return self._edges

    @edges.setter
    def edges(self, n):
        self._edges = n
        self._interior_angle = None
        self._edge_len = None
        self._apothem = None
        self._perimeter = None

    @property
    def circumradius(self):
        return self._radius

    @circumradius.setter
    def circumradius(self, r):
        self._radius = r
        self._area = None
        self._edge_len = None
        self._apothem = None

    @property
    def interior_angle(self):
        if self._interior_angle is None:
            self._interior_angle = (self.edges - 2)*(180/self.edges)
        return self._interior_angle

    @property
    def edge_len(self):
        if self._edge_len is None:
            self._edge_len = round(
                2*self.circumradius*math.sin(math.pi/self.edges), 3)
        return self._edge_len

    @property
    def apothem(self):
        if self._apothem == None:
            self._apothem = self.circumradius * math.cos(math.pi/self.edges)
        return self._apothem

    @property
    def area(self):
        if self._area is None:
            self._area = 0.5*self.edges * self.edge_len * self.apothem
        return self._area

    @property
    def perimeter(self):
        if self._perimeter is None:
            self._perimeter = self.edges * self.edge_len
        return self._perimeter

    def __repr__(self):
        return f'Polygon(n={self.edges}, R={self.circumradius})'

    def __eq__(self, other):
        if not isinstance(other, Polygon):
            raise TypeError(f'{other} Object must be of Type Polygon')
        return (self.edges == other.edges) and (self.circumradius == other.circumradius)

    def __gt__(self, other):
        if not isinstance(other, Polygon):
            raise TypeError(f'{other} Object must be of Type Polygon')
        return self.edges > other.edges

    def __ge__(self, other):
        if not isinstance(other, Polygon):
            raise TypeError(f'{other} Object must be of Type Polygon')
        return self.edges >= other.edges
