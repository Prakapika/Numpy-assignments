#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
z = np.zeros(10)
z[4] = 1
print(z)


# Range from 10 to 50

# In[3]:


import numpy as np
z = np.arange(10,50)
print(z)


# 3x3 matrix

# In[5]:


import numpy as np
z = np.arange(9).reshape(3,3)
print(z)


# non-zero elements

# In[6]:


import numpy as np
n = np.nonzero([1,2,0,0,4,0])
print(n)


# 10x10 array

# In[10]:


import numpy as np
z = np.random.random((10,10))
zmin, zmax = z.min(), z.max()
print(zmin, zmax)


# mean value

# In[11]:


import numpy as np
z = np.random.random(30)
m = z.mean()
print(m)


# In[ ]:




