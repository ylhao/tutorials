# coding: utf-8


import numpy as np
import pandas as pd
get_ipython().run_line_magic('matplotlib', 'inline  # 在 jupyter notebook 中使用 matplotlib')
import matplotlib.pyplot as plt


"""
如果只向 plot() 命令提供单个列表或数组，则 matplotlib 假定它是一个 y 值序列，并自动为你生成 x 值序列。
生成的 x 值序列具有与 y 相同的长度，但从 0 开始。
所以这里生成的 x 值序列实际上为 [0, 1, 2, 3]
"""
plt.plot([1, 2, 3, 4])
plt.show()


"""
提供 x值 序列和 y 值序列
"""
plt.plot([0, 1, 2, 3], [1, 2, 3, 4])
plt.show()


"""
提供 x值 序列和 y 值序列并设置样式
fmt = '[color][marker][line]'
"""
plt.plot([0, 1, 2, 3], [1, 2, 3, 4], 'b-')
plt.show()


"""
提供 x值 序列和 y 值序列并设置样式
fmt = '[color][marker][line]'
"""
plt.plot([0, 1, 2, 3], [1, 2, 3, 4], 'bo')
plt.show()


"""
提供 x值 序列和 y 值序列并设置样式
fmt = '[color][marker][line]'
"""
plt.plot([0, 1, 2, 3], [1, 2, 3, 4], 'bo--')
plt.show()


"""
在一条命令中绘制多个线条
"""
t = np.arange(0., 2., 0.1)
plt.plot(t, t**2, 'bs')  # red dashes
plt.plot(t, t**3, 'g^')  # blue squares
plt.plot(t, t, 'r--')  # green triangles
plt.show()


"""
在一条命令中绘制多个线条
"""
t = np.arange(0., 2., 0.1)
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')  # red dashes, blue squares and green triangles
plt.show()
