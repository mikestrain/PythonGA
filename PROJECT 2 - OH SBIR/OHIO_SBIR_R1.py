# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
from IPython import get_ipython

# %%
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import geocoder
import geopy.distance as gp

# set the plots to display in the Jupyter notebook
get_ipython().run_line_magic('matplotlib', 'inline')

# change plotting colors per client request
plt.style.use('ggplot')


# %%
OH = pd.read_csv('OHIO_SBIR_Full2.csv', encoding='ISO-8859-1')


# %%
cities = list(OH['City'])


# %%
dist_list = []
for i in range(len(cities)):

    city = cities[i]

    city_state = city + ', OH'
    coordinates = geocoder.arcgis(city_state).latlng
    lat = coordinates[0]
    lng = coordinates[1]

    coords_1 = (lat, lng)
    coords_2 = (40.2062389,-83.2271377)
    dist = gp.vincenty(coords_1, coords_2).miles
    print(city,'   ',dist)
    dist_list.append(dist)


# %%

OH["Distance"] = dist_list
OH = OH.sort_values(by='Distance')
OH.to_csv('OH1.csv',index=False)

#filter out for commutes that are less than 70 miles
OH2 = OH[OH['Distance'] < 70]
OH2.to_csv('OH2_70miles.csv',index=False)


# %%
