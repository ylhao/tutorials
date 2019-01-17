
# coding: utf-8

# In[2]:


import matplotlib.pyplot as plt


# In[9]:


fig = plt.figure(figsize=(8, 6))
x_axis = ['Mon.', 'Tue.', 'Wed.', 'Thu.', 'Fri.', 'Sat.', 'Sun.']
y_axis = [100, 200, 300, 400, 300, 200, 100]
plt.bar(range(len(y_axis)), y_axis, width=1., color='rgb',tick_label=x_axis)
plt.ylabel('Sales (KG)')
plt.title('Fruit sales statistics')
plt.savefig('./水果销量统计图（英文版）.png')
plt.show()

