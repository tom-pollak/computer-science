from typing import List, Optional, TypeVar

V = TypeVar('V', bound='Vector')


class Vector:
    def __init__(self, vector=[], *args):
        if isinstance(vector, list):
            self._vector = vector[:]
        else:
            self._vector = []

    def __str__(self):
        string = '<'
        for el in self._vector:
            string += f'{float(el)}, '
        string = string.strip(' ')
        string = string.strip(',')
        string += '>'
        return string

    def dim(self):
        return len(self._vector)

    def set(self, index, value):
        self._vector[index] = value

    def get(self, index):
        return self._vector[index]

    def __getitem__(self, index):
        return self._vector[index]

    def equals(self, other_vector):
        if not isinstance(other_vector, Vector):
            raise TypeError('argument must be a Vector object')
        if self._vector.dim() != other_vector.dim():
            return False

        for i in range(self._vector):
            if self._vector.dim() != other_vector.dim():
                return False
        return True

    def __mul__(self):
        return NotImplemented

    def scalar_product(self, scalar):
        vector = []
        for dimension in self._vector:
            vector.append(dimension * scalar)
        return Vector(vector=vector)

    def __rmul__(self, scalar):
        vector = []
        for dimension in self._vector:
            vector.append(dimension * scalar)
        return Vector(vector=vector)

    def add(self, other_vector):
        if not isinstance(other_vector, Vector):
            raise TypeError('argument must be a Vector object')
        if self._vector.dim() != other_vector.dim():
            raise ValueError('Vectors not the same dimension')
        vector = Vector()
        for i in range(self._vector):
            vector[i] = self._vector.get(i) + other_vector.get(i)
        return vector

    def __add__(self, other_vector):
        if not isinstance(other_vector, Vector):
            raise TypeError('argument must be a Vector object')
        if self._vector.dim() != other_vector.dim():
            raise ValueError('Vectors not the same dimension')
        vector = Vector()
        for i in range(self._vector):
            vector[i] = self._vector.get(i) + other_vector.get(i)
        return vector

    def __eq__(self, other_vector):
        if not isinstance(other_vector, Vector):
            raise TypeError('argument must be a Vector object')
        if self._vector.dim() != other_vector.dim():
            return False

        for i in range(self._vector):
            if self._vector.dim() != other_vector.dim():
                return False
        return True

    def __ne__(self, other_vector):
        if not isinstance(other_vector, Vector):
            raise TypeError('argument must be a Vector object')
        if self._vector.dim() != other_vector.dim():
            return True

        for i in range(self._vector):
            if self._vector.dim() == other_vector.dim():
                return False
        return True

    def __iadd__(self, other_vector):
        return self.__add__(other_vector)

    def __imul__(self, scalar):
        return self.__rmul__(scalar)

    def __setitem__(self, index, value):
        self._vector[index] = value

    # def vector_addition(self, vector1: List[float],
    #                     vector2: List[float]) -> Optional[List[float]]:
    #     if len(vector1) != len(vector2):
    #         return None
    #
    #     result_vector = []
    #     for dimension1, dimension2 in zip(vector1, vector2):
    #         result_vector.append(dimension1 + dimension2)
    #     return result_vector
