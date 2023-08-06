import numpy as np
from functools import reduce
import sys


def render(paths, filename="output/output"):
    min_x = sys.maxsize
    max_x = -sys.maxsize

    min_y = sys.maxsize
    max_y = -sys.maxsize

    svg_paths = ""

    for path in paths:
        path_data = ""

        path.append(path[-1])
        for point_index in range(len(path)):
            point = path[point_index]

            if point[0] < min_x:
                min_x = point[0]
            if point[0] > max_x:
                max_x = point[0]

            if point[1] < min_y:
                min_y = point[1]
            if point[1] > max_y:
                max_y = point[1]

            if point_index == 0:
                path_data += "M " + str(point[0]) + "," + str(point[1])
                continue

            prevPoint = path[point_index - 1]
            controlPointX = (prevPoint[0] + point[0]) / 2
            controlPointY = (prevPoint[1] + point[1]) / 2

            path_data += (
                " Q "
                + str(prevPoint[0])
                + ","
                + str(prevPoint[1])
                + " "
                + str(controlPointX)
                + ","
                + str(controlPointY)
            )

        svg_paths += (
            '<path d="'
            + path_data
            + '" stroke="black" stroke-width="0.01" fill="none" />'
        )

    delta_x = max_x - min_x
    delta_y = max_y - min_y

    svg = (
        '<svg fill="none" xmlns="http://www.w3.org/2000/svg" viewBox="'
        + str(min_x)
        + " "
        + str(min_y)
        + " "
        + str(delta_x)
        + " "
        + str(delta_y)
        + '" width="100%" height="100%">'
        + svg_paths
        + "</svg>"
    )

    with open(filename + ".svg", "w") as file:
        file.write(svg)
