import math

class Vector:
    def __init__(self, components):
        self.components = components


def dot(vector1, vector2):
    if len(vector1.components) != len(vector2.components):
        raise ValueError("Vectors must have the same number of components")
    result = 0
    for component1, component2 in zip(vector1.components, vector2.components):
        result += component1 * component2
    return result


def distance(vector1, vector2):
    if len(vector1.components) != len(vector2.components):
        raise ValueError("Vectors must have the same number of components")
    
    squared_distance = sum((component1 - component2) ** 2 for component1, component2 in zip(vector1.components, vector2.components))
    return math.sqrt(squared_distance)


def add(vector1, vector2):
    if len(vector1.components) != len(vector2.components):
        raise ValueError("Vectors must have the same number of components")
    
    result_components = [component1 + component2 for component1, component2 in zip(vector1.components, vector2.components)]
    return Vector(result_components)


def scalar_multiply(vector, scalar):
    result_components = [scalar * component for component in vector.components]
    return Vector(result_components)