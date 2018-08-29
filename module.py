from copy import deepcopy

class module():

    def __init__(self, r = None, s = None):
        self.terms = [] if r is None or s is None else [(deepcopy(r), deepcopy(s))]

    def copy(self):
        return deepcopy(self)


    # index, contains

    def index(self, s):
        for ind, rs in enumerate(self.terms):
            if rs[1] == s: return ind
        return None

    # for inserting returns the index such that self.terms[i-1] < s < self.terms[i]
    def __insert_index(self, rs):
        for index, rs0 in enumerate(self.terms):
            if rs0[1] == rs[1]: raise ValueError("Cannot insert existing element.")
            if rs0[1] > rs[1]: return index
        return len(self.terms) if len(self.terms) else 0  # might as well be just len(self.terms)

    def __contains__(self, s):
        return self.index(s) is not None

    # adding/setting elements

    def __iadd__(self, other):

        if isinstance(other, tuple):
            index = self.index(other[1])
            if index is None:
                self.terms.insert(self.__insert_index(other), deepcopy(other)) # sorted insert
            else:
              #  print(self.terms[index])
                self.terms[index] = (self.terms[index][0] + other[0], self.terms[index][1]) # no copy!

        elif isinstance(other, module):
            # add two modules, element by element
            for rs in other:
                self += rs # no need of copy

        else: raise ValueError("Cannot iadd this type.")
        return self

    def __add__(self, other):
        m = self.copy()
        m += other # no need of copy
        return m

    def __radd__(self, other): return self + other

    def __isub__(self, other):

        if isinstance(other, tuple):
            index = self.index(other[1])
            if index is None:
                self.terms.insert(self.__insert_index(other), (-deepcopy(other[0]), deepcopy(other[1]))) # sorted insert
            else:
               # print(self.terms[index])
                self.terms[index] = (self.terms[index][0] - other[0], self.terms[index][1]) # no copy!

        elif isinstance(other, module):
            # add two modules, element by element
            for rs in other:
                self -= rs # no need of copy

        else: raise ValueError("Cannot iadd this type.")
        return self

    def __sub__(self, other):
        m = self.copy()
        m -= other # no need of copy
        return m

    def __rsub__(self, other): return self - other


    def __imul__(self, r):
        self.terms = [(rs[0] * r, rs[1]) for rs in self.terms]
        return self

    def __mul__(self, r):
        m = self.copy()
        m *= r
        return m

    def __rmul__(self, other): return self * other


    def __idiv__(self, r):
        self.terms = [(rs[0] / r, rs[1]) for rs in self.terms]
        return self

    def __div__(self, r):
        m = self.copy()
        m /= r
        return m

    def __ifloordiv__(self, r):
        self.terms = [(rs[0] // r, rs[1]) for rs in self.terms]
        return self

    def __floordiv__(self, r):
        m = self.copy()
        m //= r
        return m

    def __getitem__(self, s):
        if s not in self: raise  ValueError("Element not in module.")

    # def iterating

    def __iter__(self):
        self.current_index = 0
        return self

    def __next__(self):
        if self.current_index >= len(self.terms): raise StopIteration
        self.current_index += 1
        return self.terms[self.current_index-1]

    # comparing

    def __eq__(self, other):
        return self.terms == other.terms

    def __ne__(self, other):
        return self.terms != other.terms


    def __repr__(self):
        return (" + ".join( str(r)+str(s) for r, s in self.terms)).replace(" + -", " -")

m1 = module(2, "c")
m1 += (-6, "x")
m2 = module(15, "a")
m3 = module(3, "x")

print(m1)
print(m1+m2+m3)
print(10*m1+m2//3-m3)


