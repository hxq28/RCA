import numpy as np
import pandas as pd
x_0_0 = """313.09
350.87
383.43
452.03
499.74
566.73
634.37"""

x_0_1 = """1.24
1.33
1.35
1.48
1.54
1.62
1.75"""


x_1 = """100946
106975
111384
113191
103275
111799
125058"""

x_2 = """13015.63
14169.88
15676.75
17606.13
19677.93
22143.58
24393.11"""
r = 0.5
x_0_0 = [float(item) for item in x_0_0.split("\n")]
x_0_1 = [float(item) for item in x_0_1.split("\n")]
x_1 = [float(item) for item in x_1.split("\n")]
x_2 = [float(item) for item in x_2.split("\n")]

x_0 = [x_0_0[i] / x_0_1[i] * 100 for  i in range(len(x_0_0))]
data = np.array([x_0, x_1, x_2])
df = pd.DataFrame(data)
print(f'原始矩阵\n{df}')

for i in range(df.shape[0]):
    df.iloc[i] = df.iloc[i] / df.iloc[i, 0]

print(f'规划化后的矩阵\n{df}')

df_ = np.abs(df - df.iloc[0, :])
global_max = df_.max().max()
global_min = df_.min().min()

df_r = (global_min + r * global_max) / (df_ + r * global_max)
print('-----')
print(df_r)
print('-----')
print(df_r.mean(axis=1))
