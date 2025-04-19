import numpy as np
import gaussian_elimination as ge

matrix_path = "target_matrix.npy"
Augmented = np.load(matrix_path)
Coefficient = Augmented[:,:-1]
Constant = Augmented[:,-1]
slt_ges = ge.gaussian_elimination_seq(Coefficient, Constant)
slt_gep = ge.gaussian_elimination_partial_pivoting(Coefficient, Constant)
print(f"顺序高斯消元法解向量:{slt_ges}")
print(f"主元高斯消元法解向量:{slt_gep}")