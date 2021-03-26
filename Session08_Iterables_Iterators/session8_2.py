from session8_1 import Polygon


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
