import numpy as np
import csv


# Build point type matrix, Mpt
# Point type matrix  Mtp(n_p,6) (i,j,place,edge,corner,bound)
#
#   Place:     1-inside plade           2111112
#              2-edge                   1000001
#              3-corner                 1000001
#                                       2111112
#
#    Edge:     1-upper(j=0)            ----1----
#              2-rigth(i=n_x)          |       |
#              3-lower(j=n_y)          4       2
#              4-left(i=0)             |       |
#                                      ----3----
#
#    Corner:   1-(i=0,j=0)             1-------2
#              2-(i=n_x,j=0)           |       |
#              3-(i=n_x,j=n_y)         |       |
#              4-(i=0,j=n_y)           |       |
#                                      4-------3
#
#    Bound:    1-free edge
#              2-simply supported
#              3-built-in edge
#              4-symmetry edge
#
def type_point(boundary, n_x, n_y, n_p):

    print("Building point type matrix......")

    Mtp = np.zeros((n_p, 6))
    i = 1
    j = 1
    for n in range(n_p):
        Mtp[n, 0] = i
        Mtp[n, 1] = j
        if i in [1, n_x] or j in [1, n_y]:
            if j == 1:
                Mtp[n, 2] = 1
                Mtp[n, 3] = 1
                Mtp[n, 5] = boundary[0]
            elif i == n_x:
                Mtp[n, 2] = 1
                Mtp[n, 3] = 2
                Mtp[n, 5] = boundary[1]
            elif j == n_y:
                Mtp[n, 2] = 1
                Mtp[n, 3] = 3
                Mtp[n, 5] = boundary[2]
            elif i == 1:
                Mtp[n, 2] = 1
                Mtp[n, 3] = 4
                Mtp[n, 5] = boundary[3]

            if i == 1 and j == 1:
                Mtp[n, 2] = 2
                Mtp[n, 4] = 1
                Mtp[n, 5] = corners_boundary(0, 3, boundary)
            elif i == n_x and j == 1:
                Mtp[n, 2] = 2
                Mtp[n, 4] = 2
                Mtp[n, 5] = corners_boundary(1, 0, boundary)
            elif i == n_x and j == n_y:
                Mtp[n, 2] = 2
                Mtp[n, 4] = 3
                Mtp[n, 5] = corners_boundary(2, 1, boundary)
            elif i == 1 and j == n_y:
                Mtp[n, 2] = 2
                Mtp[n, 4] = 4
                Mtp[n, 5] = corners_boundary(3, 2, boundary)

        if i == n_x:
            i = 1
            j = j + 1
        else:
            i = i + 1

    return Mtp


# Define the boundary conditions at the corners
def corners_boundary(a, b, boundary):

    if boundary[a] == 1:
        return boundary[b]
    elif boundary[a] == 2:
        if boundary[b] == 1 or boundary[b] == 4:
            return 2
        elif boundary[b] == 2 or boundary[b] == 3:
            return 3
    elif boundary[a] == 3:
        return 3
    elif boundary[a] == 4:
        if boundary[b] == 1 or boundary[b] == 2:
            return 4
        elif boundary[b] == 3 or boundary[b] == 4:
            return 3


# Build matrix to locate the element points in the plate, M_l(n_e,4) (i,j,m,n)
def location(n_e, n_x, n_y):

    print("Building the location matrix......")

    M_l = np.empty((n_e, 4), dtype=int)
    for j in range(1, n_y):
        for i in range(1, n_x):
            n = (j - 1) * (n_x - 1) + (i - 1)
            M_l[n, 0] = j * n_x + i
            M_l[n, 1] = (j - 1) * n_x + i
            M_l[n, 2] = (j - 1) * n_x + (i - 1)
            M_l[n, 3] = j * n_x + (i - 1)

    return M_l


# Build vetor to reduce nodal deslocations, V_r(n_p,3) (w_p,theta_x_p,theta_y_p)
def nodal_reduction(boundary, n_p, Mpt):

    print("Building reduction vector......")

    V_r = np.zeros((n_p, 3), dtype=int)
    for n in range(n_p):

        # Plate edges
        if Mpt[n, 2] == 1:
            if Mpt[n, 5] == 2:
                if Mpt[n, 3] == 1 or Mpt[n, 3] == 3:
                    V_r[n, 0] = 1
                    V_r[n, 2] = 1
                elif Mpt[n, 3] == 2 or Mpt[n, 3] == 4:
                    V_r[n, 0] = 1
                    V_r[n, 1] = 1
            elif Mpt[n, 5] == 3:
                V_r[n, 0] = 1
                V_r[n, 1] = 1
                V_r[n, 2] = 1
            elif Mpt[n, 5] == 4:
                if Mpt[n, 3] == 1 or Mpt[n, 3] == 3:
                    V_r[n, 1] = 1
                elif Mpt[n, 3] == 2 or Mpt[n, 3] == 4:
                    V_r[n, 2] = 1
        # Plate corners
        elif Mpt[n, 2] == 2:
            if Mpt[n, 5] == 2:
                if Mpt[n, 4] == 1 or Mpt[n, 4] == 2:
                    if boundary[0] == 2:
                        V_r[n, 0] = 1
                        V_r[n, 2] = 1
                    else:
                        V_r[n, 0] = 1
                        V_r[n, 1] = 1
                elif Mpt[n, 4] == 3 or Mpt[n, 4] == 4:
                    if boundary[2] == 2:
                        V_r[n, 0] = 1
                        V_r[n, 2] = 1
                    else:
                        V_r[n, 0] = 1
                        V_r[n, 1] = 1
            elif Mpt[n, 5] == 3:
                V_r[n, 0] = 1
                V_r[n, 1] = 1
                V_r[n, 2] = 1
            elif Mpt[n, 5] == 4:
                if Mpt[n, 4] == 1 or Mpt[n, 4] == 2:
                    if boundary[0] == 4:
                        V_r[n, 1] = 1
                    else:
                        V_r[n, 2] = 1
                elif Mpt[n, 4] == 3 or Mpt[n, 4] == 4:
                    if boundary[2] == 4:
                        V_r[n, 1] = 1
                    else:
                        V_r[n, 2] = 1

    # Build Reduce vetor in one column
    V_r_l = np.zeros((n_p * 3), dtype=int)
    for j in range(n_p):
        for i in range(3):
            V_r_l[(3 * j + i)] = V_r[j, i]

    return V_r_l


# Build matrix R
def RR_matrix(d_x, d_y):

    print("Building [R] matix......")
    M_rr = np.zeros((12, 12))
    for j in range(4):
        i = j * 3
        M_rr[i, i] = 1
        i += 1
        M_rr[i, i] = d_y
        i += 1
        M_rr[i, i] = d_x

    return M_rr


# Built matrix of the coefficients(k1, k2, k3, k4)
def read_kk_coefficients(d_x, d_y):

    print("Reading k1, k2, k3, and k4 coefficients......")
    k = np.empty((12, 12, 4))
    with open("k_coefficients.csv", "r") as file:
        data = csv.reader(file)
        j = -1
        for lines in data:
            if len(lines) != 12:
                i = 0
                j += 1
            else:
                k[i, :, j] = np.array(lines, dtype=float)
                i += 1

    k[:, :, 0] = pow((d_y / d_x), 2) * k[:, :, 0]
    k[:, :, 1] = pow((d_x / d_y), 2) * k[:, :, 1]

    return k[:, :, 0], k[:, :, 1], k[:, :, 2], k[:, :, 3]
