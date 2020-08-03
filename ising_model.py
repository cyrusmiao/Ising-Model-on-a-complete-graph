import numpy as np
import random
import matplotlib.pyplot as plt
import matplotlib.animation as manimation

class ising_model:
    """Define Ising Model class"""
    def __init__(self, rows, columns, temperature_start = 1e3, temperature_end = 1e-3, rate = 0.95, inner_iteration = 1e6):
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
    
    #def energy_change():
        

if __name__ == "__main__":
    ex = ising_model(20.5, 20.5)
    print(ex.spins)
    print(ex.iteration)
    print(type(ex.spins))
    print(len(ex.spins))
    print(ex.spins.size)
    pass