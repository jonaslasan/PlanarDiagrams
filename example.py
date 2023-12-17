import planar_diagram
import codes
import app
import codes_theta
import os

def Sort_Tuple(tup):
 
    # getting length of list of tuples
    lst = len(tup)
    for i in range(0, lst):
 
        for j in range(0, lst-i-1):
            if (tup[j][1] > tup[j + 1][1]):
                temp = tup[j]
                tup[j] = tup[j + 1]
                tup[j + 1] = temp
    return tup

# Read all files in a directory
def read_all_files_in_directory(directory):
    all = ''
    files = []
    for filename in os.listdir(directory):
        index = filename[:filename.find("_")]
        files.append((filename, int(index)))

    ordered = Sort_Tuple(files)

    for tuple in ordered:
        filename = tuple[0]
        entry = "<div class='theta'><h2 class='heading'>" + filename[filename.find("_")+1:-4] + "</h2>\n" 
        f = open(os.path.join(directory, filename), "r")
        content = f.read()
        entry += content + "</div>\n"
        all += entry
    
    write_text_to_file("output.txt", all)

# Python write text to file
def write_text_to_file(filename, text):
    # Open file
    f = open(filename, "w")

    # Write text
    f.write(text)

    # Close file
    f.close()

#read_all_files_in_directory("output")

if __name__ == "__main__":

    # Render using matplotlib
    #planar_diagram.get_planar_diagram(codes.PD["t5_1.1"], "matplotlib")

    # Render png output/t57.png
    #i = 1
    #for key in codes_theta.THETA:
        #value = codes_theta.THETA[key]
        #planar_diagram.get_planar_diagram(value, "svg", "output/" + str(i) + "_" + key)
        #i = i + 1

    #planar_diagram.get_planar_diagram(codes.PD["+t3_1"], "png", "output/t31")

    # Render svg output/t613.svg
    # planar_diagram.get_planar_diagram(codes.PD["+t6_13"], "svg", "t613")

    # Run GUI
    app.App()

    # Read all files data in a directory
    pass