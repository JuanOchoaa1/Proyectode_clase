#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats


# In[2]:


effects_covid_19 = pd.read_csv('effects-of-covid-19-on-trade-at-15-december-2021-provisional.csv')
effects_covid_19


# In[3]:


#se encuentra que los casos presentados los dias viernes
effects_covid_19[effects_covid_19['Weekday'] == 'Friday']


# In[4]:



#resumen de los datos de año valor y valor acumulado; se puede hallar el valor total de los efectos por covid desde el 2015 hasta el 2021.

effects_covid_19.describe()


# In[5]:


# se encuentra que en momentos del 2020 es donde se presentó el mayor gastos con respecto a otros dias del resto de años.

scatter_plot = sns.scatterplot(x='Year', y='Value', data=effects_covid_19)
scatter_plot.set_title('Year vs Value')
scatter_plot.set_xlabel('Year')
scatter_plot.set_ylabel('Yalue')
sns.lmplot(x='Year', y='Value', data=effects_covid_19)


# In[6]:


#se halla que los casos de exportacion a lo largo de los años ha sido mucho mayores a los demás y encontrando mayores movimientos en el año 2020.

contab_freq=pd.crosstab(
effects_covid_19['Direction'],
effects_covid_19['Year'],
margins=True 
)
contab_freq


# In[7]:


sns.kdeplot(x='Cumulative', hue='Year', data=effects_covid_19, shade=True);


# In[8]:



contab_freq=pd.crosstab(
effects_covid_19['Weekday'],
effects_covid_19['Year'],
margins=True 
)
contab_freq


# In[9]:


effects_covid_19['Weekday']=="Monday"


# In[10]:


effects_covid_19[effects_covid_19['Weekday']=="Monday"]


# In[29]:


sns.boxplot(x=effects_covid_19['Value'], y=effects_covid_19['Cumulative'], showmeans=True)


# In[31]:


time = effects_covid_19['Year']
value = effects_covid_19['Value']
plt.plot(time,value)


# In[33]:


sns.lmplot(x='Value', y='Cumulative', data=effects_covid_19)


# In[35]:


histogram_effects_covid_19= sns.histplot (x=effects_covid_19['Value'])


# In[37]:


#SE ENCUENTRA QUE LOS COSTOS PROMEDIOS POR EFECTOS DEL COVID ESTAN CERCANOS A LOS 29'057.500 MILLONES DE DOLARES.
effects_covid_19.describe()

