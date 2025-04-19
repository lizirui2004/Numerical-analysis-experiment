import numpy as np

Coefficient = np.array([
    [1, 8e-6, -2, 2],
    [0.4, 3e-6, -1, 0.1],
    [2, -60, -3, 1],
    [-1, 5, 1, 3]
])

Constant = np.array([1, 1, 1, 1])

Augmented = np.hstack((Coefficient, Constant.reshape(-1, 1)))

np.save("target_matrix.npy",Augmented)
