import math


# crossing center -> (x1, y1)
# crossing & arc intersection -> (x2, y2)
def undercrossing(x1, y1, x2, y2, radius, gap=0.03):
    vector = (x2 - x1, y2 - y1)
    magnitude = math.sqrt(vector[0] ** 2 + vector[1] ** 2)

    # Gap can't be bigger than the crossing circle itself
    # For smaller crossing circles intersections are the end points
    if radius <= gap:
        return (x1 + vector[0], y1 + vector[1])

    # In bigger crossing circles move 'gap' away from the center
    unit_vector = (vector[0] / magnitude, vector[1] / magnitude)
    destination = (x1 + unit_vector[0] * gap, y1 + unit_vector[1] * gap)

    return destination

# crossing center -> (x1, y1)
# crossing & arc intersection -> (x2, y2)
def undercrossing_new(x1, y1, x2, y2, radius, gap=0.03, pivot=0.075):
    vector = (x2 - x1, y2 - y1)
    magnitude = math.sqrt(vector[0] ** 2 + vector[1] ** 2)

    # Gap can't be bigger than the crossing circle itself
    # For smaller crossing circles intersections are the end points
    if radius <= gap:
        return (x1 + vector[0], y1 + vector[1])

    # In bigger crossing circles move 'gap' away from the center
    unit_vector = (vector[0] / magnitude, vector[1] / magnitude)
    unit_vector_opposite = (vector[0] / magnitude * -1, vector[1] / magnitude * -1)

    destination = (x1 + unit_vector[0] * gap, y1 + unit_vector[1] * gap)
    destination2 = (x1 + unit_vector[0] * pivot, y1 + unit_vector[1] * pivot)

    destination_opposite = (x1 + unit_vector_opposite[0] * gap, y1 + unit_vector_opposite[1] * gap)
    destination_opposite2 = (x1 + unit_vector_opposite[0] * pivot, y1 + unit_vector_opposite[1] * pivot)

    return [destination2, destination, destination_opposite, destination_opposite2]

def cross(x,y, gap=0.03):
    top = (x, y + gap)
    bottom = (x, y - gap)
    left = (x - gap, y)
    right = (x + gap, y)

    return(top, bottom, left, right)



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
