# YOUR PROJECT TITLE
#### Video Demo: https://youtu.be/lz_VF2US5aI
#### Description:

The finite element method (FEM) algorithm in this project calculates the nodal displacements of a thin rectangular plate under a uniformly distributed transverse load. It is based on the principle of potential energy, allowing for accurate modelling of the plate’s response under load. Each edge of the plate can be configured with various boundary conditions, tailored to specific structural scenarios.

The algorithm proceeds by approximating the nodal displacements of the plate, which are then used to calculate other parameters such as bending moments, shear forces, stresses, and strains. These computed values give a comprehensive understanding of the plate’s structural behaviour under the applied load.

Upon completion, the program generates an output file in Tecplot format, containing all calculated characteristics of the plate, facilitating both numerical and visual analysis. In addition to Tecplot compatibility, the algorithm includes built-in visualization features, offering users an immediate graphical representation of the plate’s response.

 The input parameters provided include the plate's geometric properties, material characteristics, load distribution, boundary constraints, and mesh density. These are summarized as follows:

**Plate Dimensions:** 𝑎 (length along the 𝑥-axis) in m, 𝑏 (length along the 𝑦-axis) in m, and 𝑡 (thickness along the 𝑧-axis) in m.
**Material Properties:** Young’s modulus, E in MPa and Poisson’s ratio, v.
**Load Application:**
  - Centered at relative coordinates (x, y)
  - Distributed over the entire surface area with relative dimensions (c/a, d/b)
  - Load intensity p_0 in Pa
**Boundary Conditions:**
  - "1": free;
  - "2": simply supported;
  - "2": built-in;
  - "4": symmetry.
**Mesh Density:** n_x points along the x-axis and n_y points along the y-axis

The programs writes an output file in tecplot format with the following characteristics:
  - Spatial coordinates: x[m], y[m]
  - Deflection and slopes: w[m], t_x[rad], t_y[rad]
  - Strains: e_x, e_y, e_xy
  - Shear forces: Q_x[N], Q_y[N]
  - Moments: M_x[Nm], M_y[Nm], M_xy[Nm]
  - Stresses: s_x[MPa], s_y[MPa], s_xy[MPa]
Also the possibility to have a 3D represention of this characteristics is given to the user.

The program allows the user to specify a custom input file using the "-i" argument followed by the input file name, and a custom output file using the "-o" argument followed by the output file name. Both files should be in ".txt" format. For example:

        python project.py -i <input.txt> -o <output.txt>
