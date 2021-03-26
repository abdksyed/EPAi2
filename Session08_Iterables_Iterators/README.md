# Session 8 - Iterables and Iterators

### [Class Notebook - Iterables and Iterators](https://github.com/abdksyed/EPAi2/blob/main/Session08_Iterables_Iterators/notebooks/Iterables_and_Iterators.ipynb)

Click on **Open in Colab** for hands-on.

### [Assignment Notebook](https://colab.research.google.com/drive/1uhMg9g6YBnShhdvn30AihwzdfrBif8S7?usp=sharing)

### Topic Covered:

* #### Iterating Collections
* #### Iterators
* #### Iterators and Iterables
* #### Python BUilt-In Iterators and Iterables
* #### iter() Function

# Sequence Types
In Math: S = x1, x2, x3...(countable sequence)  
Note the indices of sequence are 1,2,3,4....  

We can refer to any item in the sequence by it's index number. ex: S\[2](=x2)  
So we have a concept of first element, second element and so on, -> _positional ordering_

In Python Sequence is similiar object, which is having an order, but here the index starts from 0.



## Creating a Polygon Class.

A regular strictly convex polygon is a polygon that has the following characteristics:
* all interior angles are less than 180
* all sides have equal length
![](RegularPolygon.png)

**Note: All the Calculated Attributes must be lazy loaded and calculated only once unless edge/radius is modified.**

For a regular strictly convex polygon with:
n edges (=n vertices)
R circumradius
* interiorAngle = ( n − 2 ) ⋅ 180 n
* edgeLength, s = 2 ⋅ R ⋅ sin ⁡ ( π n )
* apothem, a = R ⋅ cos ⁡ ( π n )
* area = 1/2 ⋅ n ⋅ s ⋅ a
* perimeter = n ⋅ s

#### The class must have 
1. initializer which takes in:
    * number of edges/vertices
    * circumradius
2. That can provide these properties:
    * \# edges
    * \# vertices
    * interior angle
    * edge length
    * apothem
    * area
    * perimeter
3. That has these functionalities:
    * a proper \_\_repr__ function
    * implements equality (==) based on # vertices and circumradius (\_\_eq__)
    * implements > based on number of vertices only (\_\_gt__)

```python
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
            print('Calculating Interior Angle')
            self._interior_angle = (self.edges - 2)*(180/self.edges)
        return self._interior_angle

    @property
    def edge_len(self):
        if self._edge_len is None:
            print('Calculating Edge Length')
            self._edge_len = round(
                2*self.circumradius*math.sin(math.pi/self.edges), 3)
        return self._edge_len

    @property
    def apothem(self):
        if self._apothem == None:
            print('Calculating Apothem')
            self._apothem = self.circumradius * math.cos(math.pi/self.edges)
        return self._apothem

    @property
    def area(self):
        if self._area is None:
            print('Calculating Area')
            self._area = 0.5*self.edges * self.edge_len * self.apothem
        return self._area

    @property
    def perimeter(self):
        if self._perimeter is None:
            print('Calculating Perimeter')
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
```

## Creating a Custom Sequence
Implementing a Custom Polygon sequence type:
1. where initializer takes in:
    * number of vertices for largest polygon in the sequence
    * common circumradius for all polygons
2. that can provide these properties:
    * max efficiency polygon: returns the Polygon with the highest area: perimeter ratio
3. that has these functionalities:
    * functions as a sequence type (\_\_getitem__)
    * supports the len() function (\_\_len__)
    * has a proper representation (\_\_repr__)

**Note: The Sequence Class Now must be both Iterator and Iterable.**


```python
class PolySeq():
    def __init__(self, max_sides: int, common_circumradius: float):
        if not isinstance(max_sides, int):
            raise TypeError('Max Sides must be of Type <int>')
        if not isinstance(common_circumradius, (float, int)):
            raise TypeError('Common Circumradius must be a number')
        if max_sides < 3:
            raise ValueError('There must be atleast 3 Sides for a Polygon')
        if common_circumradius <= 0:
            raise ValueError('Common Circumradius must be greater than 0')

        self._n = max_sides
        self._r = common_circumradius

    def __len__(self):
        return self._n - 2

    @property
    def max_eff(self):
        eff = dict()
        for i in self:
            eff[i.area/i.perimeter] = i.edges
        return {eff[max(eff)]: max(eff)}

    def __getitem__(self, s):
        if isinstance(s, int):
            # single item requested
            if s < 0:
                s = self._n + s + 1
            if s < 3 or s > self._n:
                raise IndexError(
                    f'Index for this Sequence begins at 3 and ends at {self._n}')
            return Polygon(s, self._r)
        else:
            # slice being requested
            idx = s.indices(self._n)
            rng = range(idx[0], idx[1]+1, idx[2])
            return [self[n] for n in rng]

    def __iter__(self):
        return self.PolyIter(self._n, self._r)

    class PolyIter:
        def __init__(self, length, radius):
            self.length = length
            self.radius = radius
            self.i = 3

        def __iter__(self):
            return self

        def __next__(self):
            if self.i > self.length:
                raise StopIteration
            else:
                pol = Polygon(self.i, self.radius)
                self.i += 1
                return pol
```

