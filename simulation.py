import numpy as np
import matplotlib.pyplot as plt

path = "mass_placement.csv"

data = np.loadtxt(path, delimiter=",")

x_data    = data[:, 0] # [m]
mass_data = data[:, 1] # [kg]

# Tolerances are +/- unless otherwise defined
x_tolerance    = 2/1000 # [m]
mass_tolerance = 0.1    # [kg]

# debugging
# x_tolerance    = 0
# mass_tolerance = 0

def x_cg(masses, m_tolerance, x_distances, x_tolerance):
    N = np.size(masses)

    m = masses + np.random.uniform(low=-m_tolerance, high=m_tolerance, size=N)
    x = x_distances + np.random.uniform(low=-x_tolerance, high=x_tolerance, size=N)
    x_cg = m @ x / np.sum(m)

    return x_cg

def main():
    N = 1000
    x_cg_list = np.array([])

    for i in range(N):
        x_cg_list = np.append(x_cg_list, x_cg(mass_data, mass_tolerance, x_data, x_tolerance))

    fig, ax = plt.subplots()
    ax.hist(x_cg_list, bins=50)
    plt.show()

if __name__ == "__main__":
    main()