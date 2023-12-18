from utility import circle_intersection, undercrossing_pivot


def clear_arcs(graph):
    for node_index in graph.nodes:
        node = graph.get_node(node_index)
        node["visited"] = False


def get_paths(graph):
    """
    get_paths Return a set of paths representing connected curves on the final image

    :graph: planar graph representation
    :perpendicular: whether to draw perpendicular lines at crossings
    :return
    """

    clear_arcs(graph)
    paths = []

    # Traverse paths starting at a vertex
    for arc_index in graph.get_arcs():
        arc_node = graph.get_node(arc_index)

        if arc_node["visited"]:
            continue

        path_one = get_path_perpendicular(graph, arc_index, 0)[1:]
        path_two = get_path_perpendicular(graph, arc_index, 1)

        joined_path = list(reversed(path_one)) + path_two
        paths.append(joined_path)

    return paths


# Go in one direction until you hit a vertex or original arc
# perpendicular
def get_path_perpendicular(graph_copy, start, direction):
    prev_index = None
    prev_node = None

    current_index = start
    current_node = graph_copy.get_node(current_index)
    current_node["visited"] = True
    points = []

    next_index = None
    next_node = None

    while current_node["type"] != "vertex":
        if current_node["type"] == "crossing":
            # arcs are listed counter clockwise => exit = indexof(entry) + 2
            entry_index = current_node["arcs"].index(prev_node["arcId"])
            exit_index = (entry_index + 2) % 4
            next_index = "A" + str(current_node["arcs"][exit_index])
            next_node = graph_copy.get_node(next_index)

            # Align inner cross with first arc intersection
            ref_node_index = "A" + str(current_node["arcs"][0])
            ref_node = graph_copy.get_node(ref_node_index)
            ref_node_intersection = circle_intersection(ref_node, current_node)

            outter_circle = undercrossing_pivot(
                current_node["weightedPosition"].real,
                current_node["weightedPosition"].imag,
                ref_node_intersection[0],
                ref_node_intersection[1],
                current_node["radius"],
                0.035,
            )

            inner_circle = undercrossing_pivot(
                current_node["weightedPosition"].real,
                current_node["weightedPosition"].imag,
                ref_node_intersection[0],
                ref_node_intersection[1],
                current_node["radius"],
                0.02,
            )

            if entry_index == 1 or entry_index == 3:
                points.append(outter_circle[entry_index])
                points.append(inner_circle[entry_index])

                # Break a line before center
                return points

            if entry_index == 0 or entry_index == 2:
                # Just draw a line through the center
                points.append(outter_circle[entry_index])
                points.append(inner_circle[entry_index])
                points.append(
                    (
                        current_node["weightedPosition"].real,
                        current_node["weightedPosition"].imag,
                    )
                )
                points.append(inner_circle[exit_index])
                points.append(outter_circle[exit_index])

        elif current_node["type"] == "arc":
            # Move from arc to vertex
            points.append(
                (
                    current_node["weightedPosition"].real,
                    current_node["weightedPosition"].imag,
                )
            )
            if prev_index is None:
                # First step, follow provided direction
                next_list = list(
                    filter(
                        lambda x: x[0] == "V",
                        graph_copy.get_neighbours(current_index),
                    )
                )
                next_index = next_list[direction]
                next_node = graph_copy.get_node(next_index)
            else:
                # Step in the opposite direction from previous node
                if current_node["visited"]:
                    return []

                next_list = list(
                    filter(
                        lambda x: x is not prev_index and x[0] == "V",
                        graph_copy.get_neighbours(current_index),
                    )
                )
                next_index = next_list[0]
                next_node = graph_copy.get_node(next_index)

            current_node["visited"] = True

        prev_index = current_index
        prev_node = current_node
        current_index = next_index
        current_node = next_node

        if current_index == start:
            break

    points.append(
        (
            current_node["weightedPosition"].real,
            current_node["weightedPosition"].imag,
        )
    )
    return points
