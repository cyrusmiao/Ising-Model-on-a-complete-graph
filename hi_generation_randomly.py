import numpy as np

if __name__ == "__main__":
    rows = eval(input("Please input the number of rows of the lattice: "))
    columns = eval(input("Please input the number of columns of the lattice: "))
    hi = np.random.uniform(-10, 10, rows * columns)
    print(hi)
    np.savetxt("Data/hi", hi, fmt = "%f", delimiter = " ")