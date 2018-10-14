#!/usr/bin/env python
# coding: utf-8

# In[186]:


import pandas as pd
# import numpy as np
import matplotlib.pyplot as plt
# import seaborn as sns


# In[187]:


# %matplotlib inline


# In[188]:


from urllib.request import urlopen
from bs4 import BeautifulSoup


# In[256]:


url = "https://www.formula1.com/en/results.html/2018/drivers/KIMRAI01/kimi-raikkonen.html"
html = urlopen(url)


# In[257]:


soup = BeautifulSoup(html, 'lxml')
type(soup)


# In[258]:


title = soup.title
print(title)


# In[259]:


rows = soup.find_all('tr')


# In[260]:


list_rows = []
for row in rows:
    row_td = row.find_all('td')
    # print(row_td)
    list_rows.append(row_td)
list_rows = list_rows[1:]


# In[261]:


races = []
for row in list_rows:
    str_cell = str(row)
    clean_str = BeautifulSoup(str_cell, 'lxml').get_text()
    races.append(clean_str)


# In[262]:


df = pd.DataFrame(races)
df1 = df[0].str.split(',', expand = True)
df1.head(20)


# In[263]:


labels = soup.find_all('th')
clean_lab = BeautifulSoup(str(labels), 'lxml').get_text()
header = []
header.append(clean_lab)
print(header)


# In[264]:


df2 = pd.DataFrame(header)
df2.head()


# In[265]:


df3 = df2[0].str.split(',', expand = True)
df3.head()


# In[266]:


frames = [df3,df1]
df4= pd.concat(frames)
df4.head(20)


# In[267]:


df5 = df4.rename(columns=df4.iloc[0])
df5.head()


# In[268]:


df5.reset_index(inplace = True, drop = True)
df5.head(20)


# In[269]:


df5.info()
df5.shape


# In[270]:


df6 = df5.drop(df5.index[0])
df6.head(20)


# In[271]:


points = df6[' PTS']
type(points)
print(points)


# In[272]:


plt.rcParams['figure.figsize'] = [15, 7]


# In[275]:


y = []
for i in points:
    y.append(int(i))
x = df6[' Grand Prix']
axes = plt.gca()
axes.set_ylim([0,25])
plt.plot(x, y, label = 'Points')
plt.title('Kimi Raikkonen')
plt.legend()
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:




