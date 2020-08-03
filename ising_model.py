import numpy as np
import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation

class ising_model:
    """Define Ising Model class"""
    def __init__(self, rows, columns, temperature_start = 1e3, temperature_end = 1e-3, rate = 0.95, inner_iteration = 1000000):
        #Initializing the rows and columns of 2-D Ising model.
        self.r = rows
        self.c = columns
        #Randomly initialize the state of spins.
        self.spins = 2 * np.random.randint(2, size = (rows, columns)) - 1
        #Parameters of SA.
        self.T_start = temperature_start
        self.T_end = temperature_end
        self.alpha = rate
        self.iteration = inner_iteration
        #Load the pre-defined parameters Jij and hi.
        self.J_ij = np.loadtxt("Data/Jij")
        self.h_i = np.loadtxt("Data/hi")
    
    def spin_flip_position(self):
        #Randomly select the position of the spin to be flipped.
        r_n = random.randint(0, self.r - 1)
        c_n = random.randint(0, self.c - 1)
        return r_n, c_n

    def energy_change(self, r_i, c_i):
        #Computing the energy change when a spin flip.
        delta_H = 2 * self.spins[r_i][c_i] * self.h_i[r_i * self.c + c_i]
        for j in range(self.r * self.c):
            if j != r_i * self.c + c_i:
                r_j = j // self.c
                c_j = j % self.c
                if j < r_i * self.c + c_i:
                    delta_H += 2 * self.J_ij[j][r_i * self.c + c_i] * self.spins[r_i][c_i] * self.spins[r_j][c_j]
                elif j > r_i * self.c + c_i:
                    delta_H += 2 * self.J_ij[r_i * self.c + c_i][j] * self.spins[r_i][c_i] * self.spins[r_j][c_j]
        return delta_H

    def total_energy(self):
        #Computing the total energy of the Ising system.
        total_Hamiltonian = 0
        for i in range(self.r * self.c):
            r_i = i // self.c
            c_i = i % self.c
            for j in range(self.r * self.c):
                r_j = j // self.c
                c_j = j % self.c
                if i != j:
                    if i < j:
                        total_Hamiltonian -= self.J_ij[i][j] * self.spins[r_i][c_i] * self.spins[r_j][c_j]
                    elif i > j:
                        total_Hamiltonian -= self.J_ij[j][i] * self.spins[r_i][c_i] * self.spins[r_j][c_j]
        total_Hamiltonian = total_Hamiltonian / 2
        for m in range(self.r * self.c):
            r_m = m // self.c
            c_m = m % self.c
            total_Hamiltonian -= self.h_i[m] * self.spins[r_m][c_m]
        return total_Hamiltonian

    def run(self):
        #The main process of SA.
        T = self.T_start
        while T >= self.T_end:
            for i in range(self.iteration):
                x, y = self.spin_flip_position()
                d_H = self.energy_change(x, y)
                if d_H <= 0:
                    self.spins[x][y] *= -1
                elif np.exp(-d_H / T) > np.random.rand():
                    self.spins[x][y] *= -1
            print(sum_Hamiltonian = self.total_energy)
            T *= self.alpha

if __name__ == "__main__":
    ex = ising_model(20, 20)
    ex.run()
    pass