import numpy as np


# Calculation of the element's stiffness matrix, K_e
def stiffness_matrix_element(k1, k2, k3, k4, M_r, v, E, t, d_x, d_y):

    print("Calculating element's stiffness matrix......")
    K_e = np.empty((12,12), dtype = float)
    K_e = np.add(np.add(k1, k2), np.add(np.dot(k3, v), np.dot(k4, (1 - v) / 2)))
    K_e = np.dot(np.dot(M_r, K_e), M_r)
    K_e = (E * 10**6) * (t**3) / (180 * d_x * d_y * (1 - v**2)) * K_e

    return K_e


# Calculation of the plate's stiffness matrix, K_g
def stiffness_matrix_plate(n_p, n_e, M_l, K_e):

    print("Calculating plate's stiffness matrix......")
    K_g = np.zeros((3 * n_p, 3 * n_p))

    for n in range(n_e):
        for i in range(4):
            for j in range(4):
                for k in range(3):
                    for l in range(3):
                        K_g[3 * M_l[n, i] + k, 3 * M_l[n, j] + l] += K_e[
                            3 * i + k, 3 * j + l
                        ]
    return K_g


# Calculation of the element's vector of external nodal forces
def nodal_force_element(c, d, x_c, y_c, d_x, d_y, p_0, n_e, Mpt, M_l):

    print("Calculating element's vetor of external nodal forces......")
    Q_e_1 = np.zeros((n_e, 4))
    Q_e_2 = np.zeros((n_e, 4))
    Q_e_3 = np.zeros((n_e, 4))

    for n in range(n_e):
        for j in range(4):
            h = d_x * (Mpt[M_l[n,j],0] - 1)
            f = d_y * (Mpt[M_l[n,j],1] - 1)
            if ((x_c - c / 2) <= h <= (x_c + c / 2)) and (
                (y_c - d / 2) <= f <= (y_c + d / 2)
            ):
                Q_e_1[n,j] = (p_0 * d_x * d_y) / 4

    return Q_e_1, Q_e_2, Q_e_3


# Calculation of the plate's vector of external nodal forces
def nodal_force_plate(n_e, n_p, M_l, Q_e_1, Q_e_2, Q_e_3):

    print("Calculating plate's vetor of external nodal forces......")
    Q_g = np.zeros(3 * n_p)

    for n in range(n_e):
        for j in range(4):
            Q_g[3 * M_l[n,j] + 0] += Q_e_1[n,j]
            Q_g[3 * M_l[n,j] + 1] += Q_e_2[n,j]
            Q_g[3 * M_l[n,j] + 2] += Q_e_3[n,j]

    return Q_g


# Build reduced stiffness matrix, K_r, and reduced vector of nodal forces, Q_r
def reduce_matrix_vector(V_r_l, Q_g, K_g):

    print("Building reduced stiffness matrix and nodal forces vetor......")

    mask = (V_r_l == 0)

    Q_r = Q_g[mask]

    K_r = K_g[np.ix_(mask, mask)]

    return np.array(Q_r), np.array(K_r)


# Calculation of the reduced nodal displacement vector, delta_r,
# and construction of the global nodal displacement vector, delta_g
def global_deslocation_vector(n_p, Q_r, K_r, V_r_l):

    print("Calculating global nodal deslcation vector......")

    # Calculation of the reduced nodal displacement vector, delta_r
    delta_r = np.linalg.solve(K_r, Q_r)

    # Construction of the global nodal displacement vector, delta_g
    delta_g = np.zeros(3 * n_p)

    delta_g[V_r_l == 0] = delta_r

    return delta_g
