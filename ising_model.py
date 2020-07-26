import numpy as np
import random


class ising_model:
    """Define Ising Model class"""
    def __init__(self, rows, columns):
        #Initializing the rows and columns of 2-D Ising model.
        self.r = rows
        self.c = columns
        self.spins = 2 * np.random.randint(2, size = (rows, columns)) - 1

if __name__ == "__main__":
    #ex = ising_model(20, 20)
    #print(ex.spins)
    pass