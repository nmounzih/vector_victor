class ShapeError(Exception):
    pass


class Vector:

    def __init__(self, length):
        self.length = length

    def shape(self, other):
        return (self.len(), ) == (other.len(), )

    def __add__(self, other):
        if self.shape() == other.shape():
            return [sum(item) for item in zip(self, other)]

    def __sub__(self, other):
        if self.shape == other.shape:
            return [self - other for self, other in zip(self, other)]
        else:
            raise ShapeError
