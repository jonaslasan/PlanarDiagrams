import numpy as np
from scipy import interpolate

import matplotlib.pyplot as plt
import matplotlib.pyplot as plt


def render(paths, show_plot, filename="output/output"):
    scale = 500
    offsetX = 500
    offsetY = 500

    min_x = []
    max_x = []

    min_y = []
    max_y = []

    plt.figure(figsize=(11, 8))

    for path in paths:
        path.append(path[-1])
        scaled_points = [(x * scale + offsetX, y * scale + offsetY) for (x, y) in path]

        ctr = np.array(scaled_points)
        x = ctr[:, 0]
        y = ctr[:, 1]

        l = len(x)
        t = np.linspace(0, 1, l - 2, endpoint=True)
        t = np.append([0, 0, 0], t)
        t = np.append(t, [1, 1, 1])

        tck = [t, [x, y], 3]
        u3 = np.linspace(0, 1, (max(l * 2, 70)), endpoint=True)

        out = interpolate.splev(u3, tck)
        plt.plot(out[0], out[1], "black", linewidth=2.0, label="B-spline curve")

        min_x.append(np.ndarray.min(x))
        min_y.append(np.ndarray.min(y))
        max_x.append(np.ndarray.max(x))
        max_y.append(np.ndarray.max(y))

    plt.axis([0, 1000, 0, 1000])

    # Mirror the y axis to match tkinter and SVG
    plt.gca().invert_yaxis()
    plt.axis("off")

    if show_plot:
        plt.show()
    else:
        plt.savefig(
            filename + ".png", bbox_inches="tight", transparent=True
        )
        plt.close()
