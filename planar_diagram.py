import code_parser
import circle_packing
import traversal
import svg
import png

def get_planar_diagram(pd_code: str, type: str, filename: str = "output/output"):
    meta_graph = code_parser.get_meta_graph(pd_code)
    meta_circle_packing = circle_packing.CirclePack(meta_graph)

    if type == "svg":
        path = traversal.get_paths(meta_circle_packing.graph)
        svg.render(path, filename)
    elif type == "png":
        path = traversal.get_paths(meta_circle_packing.graph)
        png.render(path, False, filename)
    elif type == "matplotlib":
        path = traversal.get_paths(meta_circle_packing.graph)
        png.render(path, True, filename)
    else:
        raise Exception("Type should be svg or png")