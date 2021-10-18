#!/usr/bin/env python
# coding: utf-8

# In[8]:


from matplotlib import pyplot as plt
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
x = [1,4,-1,0,-2]
y = [2,7,3,-1,-3]
colors = ['r','g','y','b','c']
shapes = ['o','*','s','^','p']
ax.set_xlabel('X AXIS')
ax.set_ylabel('Y AXIS')
for i in range(len(x)):
    ax.scatter(x[i],y[i], color=colors[i], marker=shapes[i])
ax.set_title('scatter plot')
plt.show()


# In[ ]:





# In[ ]:




