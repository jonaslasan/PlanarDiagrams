from tkinter import *
import code_parser
import circle_packing
import traversal


class App:
    def __init__(self):
        self.circle_packing = None
        self.sliders = {}
        self.slider_row = 3

        self.initialize_slider_values()
        self.init_canvas()

    def set_circle_packing(self, packing):
        self.circle_packing = packing
        self.graph = packing.graph
        self.initialize_slider_values()

    def init_canvas(self):
        # Canvas
        self.tk_window = Tk()

        # Left side = controls
        self.left_panel = Frame(self.tk_window)
        self.left_panel.grid(row=0, column=0, sticky="NW")

        # Input Row
        self.input_row = Frame(self.left_panel)
        self.input_row.grid(row=0, column=0, sticky="W")
        self.pd_input = Text(self.input_row, heigh=1, width=50)
        self.pd_input.grid(row=0, column=0)

        self.control_row = Frame(self.left_panel)
        self.control_row.grid(row=1, column=0, sticky="W", pady=10, padx=10)
        reset_button = Button(self.control_row, text="Reset", width=20, command=self.reset_values)
        reset_button.grid(row=0, column=0, sticky="W")
        draw_curve_button = Button(
            self.control_row, text="Draw", width=20, command=self.draw_curve
        )
        draw_curve_button.grid(row=0, column=1, sticky="W", pady=10, padx=10)

        # Options
        self.draw_circles_value = BooleanVar()
        self.draw_circles_checkbox = Checkbutton(self.control_row, text='Draw Circle Packing',variable=self.draw_circles_value, onvalue=True, offvalue=False, command=self.draw)
        self.draw_circles_checkbox.grid(row=1, column=0, sticky="W")

        self.draw_path_points_value = BooleanVar()
        self.draw_path_points_checkbox = Checkbutton(self.control_row, text='Draw Path Points',variable=self.draw_path_points_value, onvalue=True, offvalue=False, command=self.draw)
        self.draw_path_points_checkbox.grid(row=2, column=0, sticky="W")

        for key in ["a0", "a1", "b0", "b1", "c0", "c1", "d0", "d1"]:
            self.add_slider(key)

        self.add_slider("offsetX", 0, 100)
        self.add_slider("offsetY", 0, 100)
        self.add_slider("scale", 0, 2000)

        # Right side = canvas
        self.canvas = Canvas(self.tk_window, bg="white", height=1000, width=1000)
        self.canvas.grid(row=0, column=1)

        self.tk_window.mainloop()

    def draw_curve(self):
        input = self.pd_input.get("1.0", "end-1c")
        graph = code_parser.get_meta_graph(input)
        packing = circle_packing.CirclePack(graph)
        self.set_circle_packing(packing)
        self.reset_values()
        self.draw()

    def initialize_slider_values(self):
        self.slider_values = {
            "a0": 0,
            "a1": 0,
            "b0": 0,
            "b1": 0,
            "c0": 0,
            "c1": 0,
            "d0": 0,
            "d1": 0,
            "offsetX": 50,
            "offsetY": 50,
            "scale": 400,
        }

        if self.circle_packing is not None:
            self.slider_values = {
                "a0": self.circle_packing.optimal_mobius[0].real * 100,
                "a1": self.circle_packing.optimal_mobius[0].imag * 100,
                "b0": self.circle_packing.optimal_mobius[1].real * 100,
                "b1": self.circle_packing.optimal_mobius[1].imag * 100,
                "c0": self.circle_packing.optimal_mobius[2].real * 100,
                "c1": self.circle_packing.optimal_mobius[2].imag * 100,
                "d0": self.circle_packing.optimal_mobius[3].real * 100,
                "d1": self.circle_packing.optimal_mobius[3].imag * 100,
                "offsetX": 50,
                "offsetY": 50,
                "scale": 400,
            }

    def reset_values(self):
        self.initialize_slider_values()

        for slider_key in self.sliders:
            self.sliders[slider_key].set(self.slider_values[slider_key])

        self.draw()

    def add_slider(self, key, min=-100, max=100):
        slider = Scale(
            self.control_row,
            from_=min,
            to=max,
            command=lambda x: self.update_slider_value(x, key),
            label=key,
            orient=HORIZONTAL,
        )
        slider.grid(row=self.slider_row, column=0)
        self.slider_row += 1
        slider.set(self.slider_values[key])
        self.sliders[key] = slider

    def update_slider_value(self, value, key):
        self.slider_values[key] = int(value)
        self.draw()

    def draw_circle(self, x, y, r, fill="black"):
        self.canvas.create_oval(x - r, y - r, x + r, y + r, fill=fill)

    def draw(self):
        if self.circle_packing is None:
            return

        self.canvas.delete("all")

        a = complex(self.slider_values["a0"], self.slider_values["a1"])
        b = complex(self.slider_values["b0"], self.slider_values["b1"])
        c = complex(self.slider_values["c0"], self.slider_values["c1"])
        d = complex(self.slider_values["d0"], self.slider_values["d1"])

        self.circle_packing.mobius(a, b, c, d)
        self.graph = self.circle_packing.graph

        if self.draw_circles_value.get():
            self.draw_circle_packing()

        paths = traversal.get_paths(self.graph)

        offsetX = self.slider_values["offsetX"] * 10
        offsetY = self.slider_values["offsetY"] * 10
        scale = self.slider_values["scale"]

        for path in paths:
            scaled_points = [
                (x * scale + offsetX, y * scale + offsetY) for (x, y) in path
            ]
            self.canvas.create_line(scaled_points, fill="black", smooth=True, width=2)

            if self.draw_path_points_value.get():
                radius = 0.002 * scale
                for point in scaled_points:
                    self.draw_circle(point[0], point[1], radius)

    def draw_circle_packing(self):
        for index in self.graph.nodes:
            if index == "0":
                continue

            circle = self.graph.nodes[index]
            position = circle["position"]
            radius = circle["radius"]

            x = position.real
            y = position.imag

            offsetX = self.slider_values["offsetX"] * 10
            offsetY = self.slider_values["offsetY"] * 10
            scale = self.slider_values["scale"]

            drawX = x * scale + offsetX
            drawY = y * scale + offsetY

            scaledRadius = radius * scale
            self.canvas.create_oval(
                drawX - scaledRadius,
                drawY - scaledRadius,
                drawX + scaledRadius,
                drawY + scaledRadius,
                fill=circle["color"],
            )
            self.canvas.create_text(drawX, drawY, text=str(index))
