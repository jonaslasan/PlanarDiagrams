import math


# crossing center -> (x1, y1)
# crossing & arc intersection -> (x2, y2)
def overcrossing_pivot(x1, y1, x2, y2, gap=0.02):
    vector = (x2 - x1, y2 - y1)
    magnitude = math.sqrt(vector[0] ** 2 + vector[1] ** 2)

    # In bigger crossing circles move 'gap' away from the center
    unit_vector = (vector[0] / magnitude, vector[1] / magnitude)
    destination = (x1 + unit_vector[0] * gap, y1 + unit_vector[1] * gap)

    return destination


# crossing center -> (x1, y1)
# crossing & arc intersection -> (x2, y2)
def undercrossing_pivot(x1, y1, x2, y2, gap=0.02):
    vector = (x2 - x1, y2 - y1)
    magnitude = math.sqrt(vector[0] ** 2 + vector[1] ** 2)

    unit_vector_0 = (vector[0] / magnitude, vector[1] / magnitude)
    unit_vector_1 = (unit_vector_0[1] * -1, unit_vector_0[0])
    unit_vector_2 = (unit_vector_0[0] * -1, unit_vector_0[1] * -1)
    unit_vector_3 = (unit_vector_0[1], unit_vector_0[0] * -1)

    destination_0 = (x1 + unit_vector_3[0] * gap, y1 + unit_vector_3[1] * gap)
    destination_1 = (x1 + unit_vector_0[0] * gap, y1 + unit_vector_0[1] * gap)
    destination_2 = (x1 + unit_vector_1[0] * gap, y1 + unit_vector_1[1] * gap)
    destination_3 = (x1 + unit_vector_2[0] * gap, y1 + unit_vector_2[1] * gap)

    return [destination_0, destination_1, destination_2, destination_3]


def cross(x, y, gap=0.03):
    top = (x, y + gap)
    bottom = (x, y - gap)
    left = (x - gap, y)
    right = (x + gap, y)

    return (top, bottom, left, right)


def circle_intersection(node1, node2):
    x1 = node1["position"].real
    y1 = node1["position"].imag
    r1 = node1["radius"]
    x2 = node2["position"].real
    y2 = node2["position"].imag

    vector = (x2 - x1, y2 - y1)
    magnitude = math.sqrt(vector[0] ** 2 + vector[1] ** 2)
    unit_vector = (vector[0] / magnitude, vector[1] / magnitude)

    intersection = (x1 + unit_vector[0] * r1, y1 + unit_vector[1] * r1)

    return intersection


def norm(z):
    return z.real * z.real + z.imag * z.imag
