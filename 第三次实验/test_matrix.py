import numpy as np

Coefficient = np.array([
    [1, 2, -2, 0],
    [1, 1, 1, 0],
    [2, 2, 1, 0],
    [0, 0, 1, 3]
])

Constant = np.array([1, 1, 1, 1])

Augmented = np.hstack((Coefficient, Constant.reshape(-1, 1)))

np.save("target_matrix.npy",Augmented)
