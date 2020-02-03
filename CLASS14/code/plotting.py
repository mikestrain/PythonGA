# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
from IPython import get_ipython

# %%
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# %matplotlib inline

# set the plots to display in the Jupyter notebook
# get_ipython().run_line_magic('matplotlib', 'inline')

# change plotting colors per client request
plt.style.use('ggplot')

# Increase default figure and font sizes for easier viewing.
plt.rcParams['figure.figsize'] = (8, 6)
plt.rcParams['font.size'] = 14


# %%
foot = pd.read_csv('../data/international_football_results.csv')
avo = pd.read_csv('../data/avocado.csv')
choc = pd.read_csv('../data/chocolate_ratings.csv')


# %%
foot.head()


# %%
foot.dtypes


# %%
pd.to_datetime(foot["date"])


# %%
foot['datetime'] = pd.to_datetime(foot["date"]) # create a new datetime column


# %%
foot.dtypes


# %%
foot


# %%
foot['datetime'].dt.year


# %%
foot


# %%
foot['month'] = foot['datetime']


# %%
foot


# %%
foot["month"] = foot["datetime"].dt.month
foot["year"] = foot["datetime"].dt.year
foot


# %%
pd.to_datetime('2020-01-10 1:20')


# %%
foot['year'].value_counts()


# %%
foot['year'].value_counts().sort_index()


# %%
foot['year'].value_counts().plot()


# %%
foot['year'].value_counts().plot(kind='barh')


# %%
data_to_plot = foot['year'].value_counts().sort_index()

plt.figure(figsize=(20,10))
plt.xlabel('Year')
data_to_plot.plot(kind='bar')


# %%



# %%
data_to_plot2 = foot['month'].value_counts().sort_index()

plt.figure(figsize=(20,10))
plt.xlabel('Month')
plt.ylabel('Number of Games')
#plt.xticks(['jan','jan','jan','jan','jan','jan','jan','jan','jan','jan','jan','jan'])
plot2 = data_to_plot2.plot(kind='bar')


# %%



# %%

new_data = foot['home_team'].value_counts()
new_data.head(20).plot(kind='bar')







# %%
foot


# %%
choc


# %%
choc.columns


# %%
newList = ['Company', 'Bean',
       'REF', 'Year', 'Cocoa', 'Location', 'Rating',
       'Bean_Type', 'Origin']
choc.columns = newList
choc


# %%
slice1 = choc.iloc[:,5] # this is the location column
slice2 = choc.iloc[1,:] # this is the first row


# %%
len(choc['Rating'].unique()) # this is the number of unique companies from this column


# %%
choc.iloc[:,1].unique()


# %%
choc['Rating'].plot(kind='hist')
plt.xlabel('Rating of Chocolate')
plt.ylabel('Number of Entries')


# %%

#plt.hist([choc['Rating'],choc['Year']])
plt.hist(choc['Rating'])
plt.xlabel('X')
plt.ylabel('Y')
plt.hist(choc['Cocoa'])



# %%
#choc["Cocoa"] = choc['Cocoa'].str.replace('%','')
#choc["Cocoa"] = choc["Cocoa"].astype(float)
#choc.dtypes

plt.hist(choc['Cocoa'], color='blue')
plt.hist([1,2,3,4,5,6,7,7,7,7,7,7,7,7,100], color='red')
plt.xlabel('Cocoa Percentage')
plt.ylabel('Frequency')
plt.title('hello world')
plt.legend(['thing1','thing2'])


# %%
home_score = foot["home_score"]
plt.hist(home_score)


# %%
max(home_score)


# %%
mask = foot["home_score"] > 30
foot[mask]


# %%
mask = foot["home_score"] < 10
foot[mask]["home_score"].plot(kind='hist',color='blue',alpha=.8)

mask = foot["away_score"] < 10
foot[mask]["away_score"].plot(kind='hist',color='#148f55',alpha=.5) # can also take hexidecimal
plt.title("HOME TEAM VS AWAY TEAM SCORE")
plt.ylabel("Freq.")
plt.xlabel("Score")


# %%
choc['Rating'].plot(kind='hist', bins=20)


# %%
#NEW SECTION


# %%
avo.dtypes


# %%
plt.scatter(avo['Total Volume'],avo['Total Bags'])
plt.scatter(avo['Total Volume'],avo['AveragePrice']*1e7)


# %%
avo.plot(kind='scatter',x='Total Volume',y='Total Bags', s=3,c=10)


# %%
matrix = avo.select_dtypes(include='number').iloc[:,-5:-1]
pd.plotting.scatter_matrix(matrix) # dataframe for this can only have numeric data!


# %%
import seaborn as sns
sns.pairplot(avo)

