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

        self._n = vertices
        self._r = circumradius

    @property
    def edges(self):
        return self._n

    @property
    def circumradius(self):
        return self._r

    @property
    def interior_angle(self):
        return (self._n - 2)*(180/self._n)

    @property
    def edge_len(self):
        return round(2*self._r*math.sin(math.pi/self._n), 3)

    @property
    def apothem(self):
        return self._r * math.cos(math.pi/self._n)

    @property
    def area(self):
        return 0.5*self._n * self.edge_len * self.apothem

    @property
    def perimeter(self):
        return self._n * self.edge_len

    def __repr__(self):
        return f'<Polygon Object at {hex(id(self))}> with {self._n} sides and Circmradius of {self._r}'

    def __eq__(self, other):
        if not isinstance(other, Polygon):
            raise TypeError(f'{other} Object must be of Type Polygon')
        return (self._n == other.edges) and (self._r == other.circumradius)

    def __gt__(self, other):
        if not isinstance(other, Polygon):
            raise TypeError(f'{other} Object must be of Type Polygon')
        return self._n > other.edges

    def __ge__(self, other):
        if not isinstance(other, Polygon):
            raise TypeError(f'{other} Object must be of Type Polygon')
        return self._n >= other.edges
