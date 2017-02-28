import math


class ShapeError(Exception):
    pass


def shape(v):
    return (len(v), )


def vector_add(v1, v2):
    if shape(v1) == shape(v2):
        return [sum(item) for item in zip(v1, v2)]
    else:
        raise ShapeError


def vector_sub(v1, v2):
    if shape(v1) == shape(v2):
        return[v1 - v2 for v1, v2 in zip(v1, v2)]
    else:
        raise ShapeError


def vector_sum(*args):
    new_list = [len(arg) == len(args[0]) for arg in args]
    if sum(new_list) != len(args):
        raise ShapeError
    return [sum(item) for item in zip(*args)]


def dot(*args):
    new_list = [len(arg) == len(args[0]) for arg in args]
    if sum(new_list) != len(args):
        raise ShapeError
    return sum([(a * b) for (a, b) in zip(*args)])


def vector_multiply(v, n):
    return [(item * n) for item in v]


def vector_mean(*args):
    return ([sum(item)/len(args) for item in zip(*args)])


def magnitude(v):
    return math.sqrt(sum(item**2 for item in v))
