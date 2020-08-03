import numpy as np

if __name__ == "__main__":
    rows = eval(input("Please input the number of rows of the lattice: "))
    columns = eval(input("Please input the number of columns of the lattice: "))
    hi = np.zeros(rows * columns)
    for i in range(rows * columns):
        hi[i] = eval(input("Please input the value of h{}: ".format(i)))
    np.savetxt("Data/hi", hi, fmt = "%f", delimiter = " ")