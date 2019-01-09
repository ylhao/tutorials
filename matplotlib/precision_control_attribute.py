# coding: utf-8


import numpy as np
import pandas as pd
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt


"""
线条颜色：

plot 方法的关键字参数 color（或c） 用来设置线的颜色。

eg:
    plt.plot(x, y, color='blue')
    plt.plot(x, y, c='blue')

常用取值为:
    b: blue
    g: green
    r: red
    c: cyan
    m: magenta
    y: yellow
    k: black
    w: white

可以参考：
    https://matplotlib.org/api/_as_gen/matplotlib.pyplot.plot.html
"""
plt.plot([1, 2, 3, 4], [1, 4, 9, 16], color='r')
plt.show()


"""
线条样式：

plot 方法的关键字参数 linestyle（或ls） 用来设置线的样式。

eg:
    plt.plot(x, y, linestyle=':')
    plt.plot(x, y, ls=':')

常用取值为:
-   solid
--  dashed
-.  dashdot
：  dotted

可以参考：
    https://matplotlib.org/api/_as_gen/matplotlib.pyplot.plot.html
"""
plt.plot([1, 2, 3, 4], [1, 4, 9, 16], color='r', ls=':')
plt.show()


"""
线条宽度：

plot 方法的关键字参数 linewidth（或ls） 用来设置线的宽度，其值为浮点数。

eg:
    plt.plot(x, y, linewidth=2.0)
    plt.plot(x, y, lw=2.0)
"""
plt.plot([1, 2, 3, 4], [1, 4, 9, 16], color='r', ls=':', lw=3.6)
plt.show()


"""
折点属性：
marker                    折点形状
markersize 或 ms          折点大小
markeredgecolor 或 mec    折点外边颜色
markeredgewidth 或 mew    折点线宽
markerfacecolor 或 mfc    折点实心颜色
"""
plt.plot([1, 2, 3, 4], [1, 4, 9, 16], color='r', ls=':', lw=2.0, marker='s')
plt.show()


plt.plot([1, 2, 3, 4], [1, 4, 9, 16], color='r', ls=':', lw=2.0, marker='s', markersize=8.0)
plt.show()


plt.plot([1, 2, 3, 4], [1, 4, 9, 16], color='r', ls=':', lw=2.0, marker='s', markersize=8.0, markeredgecolor='c')
plt.show()


plt.plot([1, 2, 3, 4], [1, 4, 9, 16], color='r', ls=':', lw=2.0, marker='s', markersize=8.0, markeredgecolor='c', markeredgewidth=2.0)
plt.show()


plt.plot([1, 2, 3, 4], [1, 4, 9, 16], color='r', ls=':', lw=2.0, marker='s', markersize=8.0, markeredgecolor='c', markeredgewidth=2.0,
        markerfacecolor='g')
plt.show()


"""
透明度：

plot 方法的关键字参数 alpha 用来设置线条的透明度，取值范围为 [0, 1]
"""


plt.plot([1, 2, 3, 4], [1, 4, 9, 16], color='r', ls=':', lw=2.0, marker='s', markersize=8.0, markeredgecolor='c', markeredgewidth=2.0,
        markerfacecolor='g', alpha=0)
plt.show()


plt.plot([1, 2, 3, 4], [1, 4, 9, 16], color='r', ls=':', lw=2.0, marker='s', markersize=8.0, markeredgecolor='c', markeredgewidth=2.0,
        markerfacecolor='g', alpha=1)
plt.show()


plt.plot([1, 2, 3, 4], [1, 4, 9, 16], color='r', ls=':', lw=2.0, marker='s', markersize=8.0, markeredgecolor='c', markeredgewidth=2.0,
        markerfacecolor='g', alpha=0.5)
plt.show()
