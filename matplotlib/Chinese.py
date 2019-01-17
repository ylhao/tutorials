#!/usr/bin/env python
# coding: utf-8

# ## Linux 系统 matplotlib 正常使用中文
# 
# - 在该实验中用到的 Linux 系统是 Ubuntu 16.04。
# - [下载中文字体 simhei.ttf](http://fontzone.net/download/simhei)。
# - 搜索 matplotlib 的字体安装位置：`locate -b '\mpl-data'`。由于我创建了虚拟环境，得到的路径为：
# ```
# /home/yilonghao/ml/venv/lib/python3.5/site-packages/matplotlib/mpl-data
# ```
# - 切换到目标路径下（注意命令末尾的/fonts/ttf）：
# ```
# cd /home/yilonghao/ml/venv/lib/python3.5/site-packages/matplotlib/mpl-data/fonts/ttf
# ```
# - 将下载的字体拷贝到该路径下。
# - 删除当前用户的 matplotlib 缓存。
# ```
# cd ~/.cache/matplotlib
# rm -rf *.*
# ```

# ## Windows 系统 matplotlib 使用中文
# 
# Windows 系统 matplotlib 可以直接通过在代码中添加 `matplotlib.rcParams['font.sans-serif'] = ['SimHei']` 使用中文。

# In[6]:


import matplotlib
import matplotlib.pyplot as plt
matplotlib.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文


# In[8]:


fig = plt.figure(figsize=(8, 6))
x_axis = ['星期一', '星期二', '星期三', '星期四', '星期五', '星期六', '星期日']
y_axis = [100, 200, 300, 400, 300, 200, 100]
plt.bar(range(len(y_axis)), y_axis, width=1., color='rgb',tick_label=x_axis)
plt.ylabel('销量（KG）')
plt.title('水果销量统计图')
plt.savefig('./水果销量统计图（中文版）.png')
plt.show()


# In[ ]:




