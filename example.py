import planar_diagram
import codes
import app

if __name__ == "__main__":

    # Render using matplotlib
    #planar_diagram.get_planar_diagram(codes.PD["6^2_1++*"], "matplotlib")

    # Render png output/t57.png
    #planar_diagram.get_planar_diagram(codes.PD["+t5_7"], "png", "t57")

    # Render svg output/t613.svg
    #planar_diagram.get_planar_diagram(codes.PD["+t6_13"], "svg", "t613")

    # Run GUI
    app.App()
