# coding: utf-8


import numpy as np
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt


def f(t):
    return np.cos(2 * np.pi * t)


"""
subplot() 命令指定 numrows, numcols, fignum，如果不手动指定任何轴域，则默认创建 subplot(111)
其中 fignum 的范围是从 1 到 numrows * numcols。
如果 numrows * numcols < 10，则 subplot 命令中的逗号是可选的。因此，子图 subplot(211) 与 subplot(2, 1, 1) 相同。
"""
t1 = np.arange(0.0, 5.0, 0.1)
t2 = np.arange(0.0, 5.0, 0.1)

plt.figure(1)  # figure() 命令是可选的，因为默认情况下将创建 figure(1)

plt.subplot(211)
plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')

plt.subplot(212)
plt.plot(t2, f(t2), 'r--')

plt.show()


plt.figure(1)

plt.subplot(2, 1, 1)
plt.plot([0, 1], [0, 1])

plt.subplot(2, 3, 4)
plt.plot([0, 1], [0, 1])

plt.subplot(2, 3, 5)
plt.plot([0, 1], [0, 1])

plt.subplot(2, 3, 6)
plt.plot([0, 1], [0, 1])

plt.show()


"""
subplot2grid
"""

plt.figure(1)

# figure 分成 5 行 3 列, 取得第 1 个子图的句柄, 第 1 个子图跨度为 1 行 3 列, 起点是表格(0, 0)
ax1 = plt.subplot2grid((5, 3), (0, 0), rowspan=1, colspan = 3)
ax1.plot([0, 1], [0, 1])
ax1.set_title('ax1')

ax2 = plt.subplot2grid((5, 3), (2, 0), rowspan=1, colspan=2)
ax2.plot([0, 1], [0, 1])
ax2.set_title('ax2')

ax3 = plt.subplot2grid((5, 3), (2, 2), rowspan=1, colspan=2)
ax3.plot([0, 1], [0, 1])
ax3.set_title('ax3')

ax4 = plt.subplot2grid((5, 3), (4, 0), rowspan=1, colspan=3)
ax4.plot([0, 1], [0, 1])
ax4.set_title('ax4')

plt.show()


"""
matplotlib.gridspec
gridspec.GridSpec
"""


import matplotlib.gridspec as gridspec


plt.figure(1)

gs = gridspec.GridSpec(5, 3)
ax1 = plt.subplot(gs[0, :])
ax2 = plt.subplot(gs[2, 0:2])
ax3 = plt.subplot(gs[2, 2])
ax4 = plt.subplot(gs[4, :])

ax1.set_title('ax1')
ax2.set_title('ax2')
ax3.set_title('ax3')
ax4.set_title('ax4')

# 绘制图像
ax1.plot([0, 1], [0, 1])
ax2.plot([0, 1], [0, 1])
ax3.plot([0, 1], [0, 1])
ax4.plot([0, 1], [0, 1])

plt.show()


fig = plt.figure(1, figsize=(8, 6))

x = np.arange(1, 6)
y = np.arange(1, 6)

plt.plot(x, y, 'r-')
plt.xlabel('x')
plt.ylabel('y')
plt.title('plt.plot')


left, bottom, width, height = 0.2, 0.5, 0.25, 0.25
ax1 = fig.add_axes([left, bottom, width, height], facecolor='c')
ax1.plot(x, y, 'bo')
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_title('ax1')


left, bottom, width, height = 0.6, 0.2, 0.25, 0.25
plt.axes([left, bottom, width, height], facecolor='g')
plt.plot(x, y, 'r')
plt.xlabel('x')
plt.ylabel('y')
plt.title('ax2')


plt.show()
