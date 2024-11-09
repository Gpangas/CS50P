import numpy as np


# Build the elasticity matrix
def elasticity_matrix(t, E, v):

    print("Building elasticity matrix......")
    M_da = np.zeros((3, 3))

    M_da[0, 0] = E * pow(10, 6) / (1 - pow(v, 2))
    M_da[0, 1] = E * pow(10, 6) / (1 - pow(v, 2)) * v
    M_da[1, 0] = E * pow(10, 6) / (1 - pow(v, 2)) * v
    M_da[1, 1] = E * pow(10, 6) / (1 - pow(v, 2))
    M_da[2, 2] = E * pow(10, 6) / (1 - pow(v, 2)) * (1 - v) / 2

    M_dd = pow(t, 3) / 12 * M_da

    D_q = E * pow(10, 6) * pow(t, 3) / (12 * (1 - pow(v, 2)))

    return M_da, M_dd, D_q


# Calculation of the element's CC inverted matrix, M_c_i
def inv_CC_matrix(d_x, d_y):

    print("Calculating element's CC inverted matrix......")

    # Calculation of the element's CC matrix
    M_cc = np.zeros((12, 12))
    for i in range(1, 5):
        x = d_x if i in [1, 2] else 0
        y = d_y if i in [1, 4] else 0

        M_cc[3 * (i - 1), :] = [
            1,
            x,
            y,
            x**2,
            x * y,
            y**2,
            x**3,
            x**2 * y,
            x * y**2,
            y**3,
            x**3 * y,
            x * y**3,
        ]

        M_cc[3 * (i - 1) + 1, :] = [
            0,
            0,
            1,
            0,
            x,
            2 * y,
            0,
            x**2,
            2 * x * y,
            3 * y**2,
            x**3,
            3 * x * y**2,
        ]

        M_cc[3 * (i - 1) + 2, :] = [
            0,
            1,
            0,
            2 * x,
            y,
            0,
            3 * x**2,
            2 * x * y,
            y**2,
            0,
            3 * y * x**2,
            y**3,
        ]
    # Invert the element's CC matrix
    M_cc_i = np.linalg.inv(M_cc)

    return M_cc_i


# Calculation of the element's AA matrix, M_aa
def AA_matrix(d_x, d_y, i):

    M_aa = np.zeros((2, 12))

    x = d_x if i in [0, 1] else 0
    y = d_y if i in [0, 3] else 0

    M_aa[0, :] = [0, 0, 0, 0, 0, 0, -6, 0, -2, 0, -6 * y, -6 * y]

    M_aa[1, :] = [0, 0, 0, 0, 0, 0, 0, -2, 0, -6, -6 * x, -6 * x]

    return M_aa


# Calculation of the element's HH matrix, M_aa
def HH_matrix(d_x, d_y, i):

    M_hh = np.zeros((3, 12))
    x = d_x if i in [0, 1] else 0
    y = d_y if i in [0, 3] else 0

    M_hh[0, :] = [0, 0, 0, -2, 0, 0, -6 * x, -2 * y, 0, 0, -6 * x * y, 0]

    M_hh[1, :] = [0, 0, 0, 0, 0, -2, 0, 0, -2 * x, -6 * y, 0, -6 * x * y]

    M_hh[2, :] = [0, 0, 0, 0, -2, 0, 0, -4 * x, -4 * y, 0, -6 * x**2, -6 * y**2]

    return M_hh


# Calculation of the element's extensions, shear forces, bending moment and stress
def element_extensions(
    t, d_x, d_y, n_p, n_e, Mtp, delta_g, M_l, M_cc_i, M_dd, M_da, D_q
):

    print(
        "Calculating the element's extensions, shear forces, bending moment and stress......"
    )
    delta_e = np.zeros(12)
    M_qq = np.zeros(2 * n_p)
    e_g = np.zeros(3 * n_p)
    M_mm = np.zeros(3 * n_p)
    sigma = np.zeros(3 * n_p)

    for n in range(n_e):
        for i in range(4):
            delta_e[3 * i] = delta_g[3 * M_l[n,i]]
            delta_e[3 * i + 1] = delta_g[3 * M_l[n,i] + 1]
            delta_e[3 * i + 2] = delta_g[3 * M_l[n,i] + 2]

        for i in range(4):
            M_hh = HH_matrix(d_x, d_y, i)
            M_aa = AA_matrix(d_x, d_y, i)

            M_bb = np.dot(M_hh, M_cc_i)
            e_p = (t / 2) *np.dot(M_bb, delta_e)
            Q_p = np.dot(D_q, np.dot(np.dot(M_aa, M_cc_i), delta_e))
            M_p = (2 / t) * np.dot(M_dd, e_p)
            sigma_p = (2 / t) * np.dot(M_da, e_p)

            for j in range(2):
                M_qq[2 * M_l[n,i] + j] += Q_p[j]

            for j in range(3):
                e_g[3 * M_l[n,i] + j] += e_p[j]
                M_mm[3 * M_l[n,i] + j] += M_p[j]
                sigma[3 * M_l[n,i] + j] += (t / 2) * sigma_p[j]

    # Ponderation
    for n in range(n_p):
        for i in range(3):
            if Mtp[n,2] == 0:
                e_g[3 * n + i] = e_g[3 * n + i] / 4
                M_mm[3 * n + i] = M_mm[3 * n + i] / 4
                sigma[3 * n + i] = sigma[3 * n + i] / 4
            elif Mtp[n,2] == 1:
                e_g[3 * n + i] = e_g[3 * n + i] / 2
                M_mm[3 * n + i] = M_mm[3 * n + i] / 2
                sigma[3 * n + i] = sigma[3 * n + i] / 2

        for i in range(2):
            if Mtp[n,2] == 0:
                M_qq[2 * n + i] = M_qq[2 * n + i] / 4
            elif Mtp[n,2] == 1:
                M_qq[2 * n + i] = M_qq[2 * n + i] / 2

    return e_g, M_qq, M_mm, sigma
