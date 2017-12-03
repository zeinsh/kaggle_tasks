import numpy as np
def convert_to_one_hot(Y, C):
    Y = np.eye(C)[Y.values.reshape(-1)].T
    return Y

