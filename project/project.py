import pre_processing
import processing
import post_processing
import sys
import os
import numpy as np
import matplotlib.pyplot as plt


def main():
    # Validate arguments and set the file name
    files_name = input_argument(sys.argv)
    p = Plate(files_name[0])

    # Pre-processing
    Mtp, M_l, V_r_l, M_rr, k1, k2, k3, k4 = pre_processing_(p)

    # Processing
    delta_g = processing_(Mtp, M_l, V_r_l, M_rr, k1, k2, k3, k4, p)

    # Post-processing
    e_g, M_qq, M_mm, sigma = post_processing_(Mtp, M_l, delta_g, p)

    # Output
    tecplot_output(files_name[1], p, Mtp, delta_g, e_g, M_qq, M_mm, sigma)
    call_3D_visualization(files_name[1], p, Mtp, delta_g, e_g, M_qq, M_mm, sigma)


class Plate:
    def __init__(self, file_name):
        # Input file name
        self.file_name = file_name
        # Dimensions of the rectangular plate, (a*b*t) [m]
        self.a = None
        self.b = None
        self.t = None
        # Material characteristcs, E [Mpa] and v
        self.E = None
        self.v = None
        # Relatice center positon of the load, (x/a,y/b)
        self.x_c_a = None
        self.y_c_b = None
        # Relative dimensions of distributed load, (c/a,d/b)
        self.c_a = None
        self.d_b = None
        # Intensity of the uniformly distributed transverse load [Pa]
        self.p_0 = None
        # Boundary Conditions (1-free, 2-simply supported, 3-built-in, 4-symmetry)
        self.boundaries = []
        # Number of points (n_x,n_y)
        self.n_x = None
        self.n_y = None
        # Center positon of the load, (x,y)
        self.x_c = None
        self.y_c = None
        # Dimensions of the distributed load, (c,d)
        self.c = None
        self.d = None
        # Distance between points in the direction x and y
        self.d_x = None
        self.d_y = None
        # Number of points and elements
        self.n_p = None
        self.n_e = None

        # Load data from file
        self.load_data()

        # Calcutate aditional data
        self.calculate_data()

    # Reads data from a file and assigns the class attributes
    def load_data(self):
        print("Reading file......")

        with open(self.file_name, "r") as file:
            lines = file.readlines()

        try:
            self.a, self.b, self.t = list(map(float, lines[1].split()))
            self.E, self.v = list(map(float, lines[3].split()))
            self.x_c_a, self.y_c_b = list(map(float, lines[5].split()))
            self.c_a, self.d_b = list(map(float, lines[7].split()))
            self.p_0 = float(lines[9].split()[0])
            self.boundaries = list(map(int, lines[12].split()))
            self.n_x, self.n_y = list(map(int, lines[14].split()))
        except ValueError:
            sys.exit(f"Invalid input data in file {self.file_name}!")

    # Calcutate aditional data
    def calculate_data(self):
        print("Calculating positions......")

        # Calculate positions, dimensions and distances from relative values
        self.x_c = self.a * self.x_c_a
        self.y_c = self.b * self.y_c_b
        self.c = self.a * self.c_a
        self.d = self.b * self.d_b
        self.d_x = self.a / (self.n_x - 1)
        self.d_y = self.b / (self.n_y - 1)

        # Calculate the number of points and elements
        self.n_p = self.n_x * self.n_y
        self.n_e = (self.n_x - 1) * (self.n_y - 1)


# Validate arguments and set the file name
def input_argument(s):

    print("Validating arguments......")

    # Default files name
    files_name = ["input.txt", "output.txt"]
    if len(s) == 1:
        # Check if input file exists
        if not os.path.exists("input.txt"):
            sys.exit("Missing input file!")
    elif len(s) in [2, 4]:
        sys.exit("Missing arguments!")
    elif len(s) in [3, 5]:
        # Check if the arguments are duplicated
        if s[1] == s[3] or s[2] == s[4]:
            sys.exit("Repeated arguments!")
        for i in [1, 3]:
            if s[i] == "-i":
                # Check if it is a .txt file and that it exists
                if os.path.exists(s[i + 1]) and ".txt" in s[i + 1]:
                    files_name[0] = s[i + 1]
                else:
                    sys.exit("Invalid or missing input file!")
            elif s[i] == "-o":
                # Check if it is a .txt file
                if ".txt" in s[i + 1]:
                    files_name[1] = s[i + 1]
                else:
                    sys.exit("Invalid output file!")
            else:
                sys.exit("Invalid arguments!")
    elif len(s) > 5:
        sys.exit("Too many arguments!")

    print("Arguments validated and files name set.")
    return files_name


# Pre-processing
def pre_processing_(p):

    Mtp = pre_processing.type_point(p.boundaries, p.n_x, p.n_y, p.n_p)
    M_l = pre_processing.location(p.n_e, p.n_x, p.n_y)
    V_r_l = pre_processing.nodal_reduction(p.boundaries, p.n_p, Mtp)
    M_rr = pre_processing.RR_matrix(p.d_x, p.d_y)
    k1, k2, k3, k4 = pre_processing.read_kk_coefficients(p.d_x, p.d_y)

    return Mtp, M_l, V_r_l, M_rr, k1, k2, k3, k4


# Processing
def processing_(Mtp, M_l, V_r_l, M_rr, k1, k2, k3, k4, p):
    K_e = processing.stiffness_matrix_element(
        k1, k2, k3, k4, M_rr, p.v, p.E, p.t, p.d_x, p.d_y
    )
    K_g = processing.stiffness_matrix_plate(p.n_p, p.n_e, M_l, K_e)
    Q_e_1, Q_e_2, Q_e_3 = processing.nodal_force_element(
        p.c, p.d, p.x_c, p.y_c, p.d_x, p.d_y, p.p_0, p.n_e, Mtp, M_l
    )
    Q_g = processing.nodal_force_plate(p.n_e, p.n_p, M_l, Q_e_1, Q_e_2, Q_e_3)
    Q_r, K_r = processing.reduce_matrix_vector(V_r_l, Q_g, K_g)
    delta_g = processing.global_deslocation_vector(p.n_p, Q_r, K_r, V_r_l)

    return delta_g


# Post-Processing
def post_processing_(Mtp, M_l, delta_g, p):
    M_da, M_dd, D_q = post_processing.elasticity_matrix(p.t, p.E, p.v)
    M_cc_i = post_processing.inv_CC_matrix(p.d_x, p.d_y)
    e_g, M_qq, M_mm, sigma = post_processing.element_extensions(
        p.t, p.d_x, p.d_y, p.n_p, p.n_e, Mtp, delta_g, M_l, M_cc_i, M_dd, M_da, D_q
    )
    return e_g, M_qq, M_mm, sigma


# Create output file in tecplot format
def tecplot_output(file_name, p, Mtp, delta_g, e_g, M_qq, M_mm, sigma):

    headline = [
        "x[m]",
        "y[m]",
        "w[m]",
        "t_x[rad]",
        "t_y[rad]",
        "e_x",
        "e_y",
        "e_xy",
        "Q_x[N]",
        "Q_y[N]",
        "M_x[Nm]",
        "M_y[Nm]",
        "M_xy[Nm]",
        "s_x[MPa]",
        "s_y[MPa]",
        "s_xy[MPa]",
    ]

    print("Writing the output file.....")
    col_width = 24
    float_format = "{:.12f}"
    int_format = "{:04d}"
    with open(file_name, "w") as file:
        file.write(f'TITLE = "Plate"\n')
        file.write(f'VARIABLES = "')
        for i in range(16):
            file.write(f"{headline[i]}")
            if i != 15:
                file.write(f",")
        file.write(f'"\n')
        file.write(
            f'ZONE T="Plate", I={int_format.format(p.n_x)} J={int_format.format(p.n_y)}\n'
        )

        col = np.zeros(16)
        for n in range(p.n_p):

            col[0] = p.d_x * (Mtp[n, 0] - 1)  # X-coordinates
            col[1] = p.d_y * (Mtp[n, 1] - 1)  # Y-coordinates
            col[2:5] = delta_g[3 * n : 3 * n + 3]  # Delta values
            col[5:8] = e_g[3 * n : 3 * n + 3]  # Extensions
            col[8:10] = M_qq[2 * n : 2 * n + 2]  # Shear forces
            col[10:13] = M_mm[3 * n : 3 * n + 3]  # Bending moments
            col[13:16] = sigma[3 * n : 3 * n + 3] / pow(
                10, 6
            )  # Stress values (converted to MegaPascals)

            for i in range(16):
                file.write(f"{float_format.format(col[i]).ljust(col_width)}")
            file.write(f"\n")


# Create 3D scatter graphic
def Build_3D_graph(file_name, title, x, y, z):

    fig = plt.figure(figsize=(16, 10))
    ax = fig.add_subplot(111, projection="3d")

    # Create a 3D scatter plot
    scatter = ax.scatter3D(x, y, z, c=z, cmap="tab20c")
    # Add color bar
    cbar = fig.colorbar(scatter, ax=ax)

    # Add labels to axes
    ax.set_xlabel("x[m]")
    ax.set_ylabel("y[m]")
    # ax.set_zticks([])
    ax.set_title(title)

    # Save plot
    fig.savefig(file_name.removesuffix(".txt") + "/" + title + "_plot.png", dpi=300)
    plt.close(fig)


# Call visualization for all the properties
def call_3D_visualization(file_name, p, Mtp, delta_g, e_g, M_qq, M_mm, sigma):
    while True:
        text = input("3D visualization?(Yes/No)").lower()
        if text == "yes":
            visualize = True
            break
        elif text == "no":
            visualize = False
            break

    if visualize:
        headline = [
            "x[m]",
            "y[m]",
            "w[m]",
            "t_x[rad]",
            "t_y[rad]",
            "e_x",
            "e_y",
            "e_xy",
            "Q_x[N]",
            "Q_y[N]",
            "M_x[Nm]",
            "M_y[Nm]",
            "M_xy[Nm]",
            "s_x[MPa]",
            "s_y[MPa]",
            "s_xy[MPa]",
        ]

        print("Building the graphical representation.....")
        data = np.zeros((p.n_p, 16))

        data[:, 0] = p.d_x * (Mtp[:, 0] - 1)  # X-coordinates
        data[:, 1] = p.d_y * (Mtp[:, 1] - 1)  # Y-coordinates
        data[:, 2:5] = delta_g.reshape(p.n_p, 3)  # Delta values
        data[:, 5:8] = e_g.reshape(p.n_p, 3)  # Extensions
        data[:, 8:10] = M_qq.reshape(p.n_p, 2)  # Shear forces
        data[:, 10:13] = M_mm.reshape(p.n_p, 3)  # Bending moments
        data[:, 13:16] = sigma.reshape(p.n_p, 3) / pow(10, 6
        )  # Stress values (converted to MegaPascals)

        for i in range(2, 16):
            Build_3D_graph(file_name, headline[i], data[:, 0], data[:, 1], data[:, i])


if __name__ == "__main__":
    main()
