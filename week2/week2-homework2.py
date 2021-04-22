#!/usr/bin/env python
# coding: utf-8

# In[4]:


# 4. Create notebook, import libraries and read the dataset
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
get_ipython().run_line_magic('matplotlib', 'inline')
titanic_data = pd.read_csv('gender_submission.csv')
print(titanic_data.head(10))
titanic_data.describe()


# In[5]:


titanic_data.info()


# In[7]:


titanic_data.shape


# In[10]:


# 7. Read and describing dataset 
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
get_ipython().run_line_magic('matplotlib', 'inline')
fraud_recorded = pd.read_csv('creditcard.csv')
print(fraud_recorded.head(3))


# In[11]:


fraud_recorded.describe()


# In[12]:


fraud_recorded.info()


# In[13]:


fraud_recorded.shape


# In[14]:


viz = fraud_recorded.head(20)[['Time', 'V1']]
viz.hist()
plt.show()


# In[ ]:




