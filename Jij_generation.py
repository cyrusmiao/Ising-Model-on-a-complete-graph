import numpy as np

if __name__ == "__main__":
    rows = eval(input("Please input the number of rows of the lattice: "))
    columns = eval(input("Please input the number of columns of the lattice: "))
    Jij = np.zeros([rows * columns, rows * columns])
    for i in range(rows):
        for j in range(columns):
            for x in range(rows):
                for y in range(columns):
                    a = i * columns + j
                    b = x * columns + y
                    if a < b:
                        Jij[a][b] = eval(input("Please input the value of J{}{}: ".format(a, b)))
                        
    np.savetxt("Data/Jij", Jij, fmt = "%f", delimiter = " ")