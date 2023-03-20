import pandas as pd
import numpy as np

# 导入数据
data = pd.DataFrame(np.random.random((5,5)))

# 构建rca矩阵
row_sum = data.sum(axis=1)
column_sum = data.sum(axis=0)

rca_matrix = np.zeros((5,5))
for i in range(5):
    for j in range(5):
        rca_matrix[i,j] = data[j][i]/np.sqrt(row_sum[i]*column_sum[j])

# 输出rca矩阵
print(rca_matrix)
