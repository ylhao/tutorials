# coding: utf-8


import numpy as np
import pandas as pd
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt


plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro')
plt.axis([0, 6, 0, 20])  # 接收 [xmin, xmax, ymin, ymax] 的列表，并指定轴域的可视区域
plt.show()


plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro')
xmin, xmax, ymin, ymax = plt.axis()  # 获取指定轴域的可视范围
print(xmin, xmax, ymin, ymax)
plt.show()
