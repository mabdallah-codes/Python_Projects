# -*- coding: utf-8 -*-
"""Line Pots_Series_Dataframe

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1PHptJT8TNxa-HUBTZ2FVoSXfquPOWeXL

Visualizing Data using Matplotlib

Matplotlib.Pyplot

One of the core aspects of Matplotlib is matplotlib.pyplot. It is Matplotlib's scripting layer which we studied in details in the videos about Matplotlib. Recall that it is a collection of command style functions that make Matplotlib work like MATLAB. Each pyplot function makes some change to a figure: e.g., creates a figure, creates a plotting area in a figure, plots some lines in a plotting area, decorates the plot with labels, etc. In this lab, we will work with the scripting layer to learn how to generate line plots. In future labs, we will get to work with the Artist layer as well to experiment first hand how it differs from the scripting layer.
"""

# Commented out IPython magic to ensure Python compatibility.
# we are using the inline backend
# %matplotlib inline 

import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd

print ('Matplotlib version: ', mpl.__version__) # >= 2.0.0

# Apply a style to Matplotlib

print(plt.style.available)
mpl.style.use(['ggplot']) # optional: for ggplot-like style

# Import Date Set

# Import Canada Imigration Dataset

url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/Canada.xlsx"
df_canada = pd.read_excel(url, sheet_name='Canada by Citizenship',
        skiprows=range(20),
        skipfooter=2)
df_canada.columns = list(map(str, df_canada.columns))
# [print (type(x)) for x in df_can.columns.values] #<-- uncomment to check type of column headers

# useful for plotting later on
years = list(map(str, range(1980, 2014)))
years

"""Plotting in pandas

Fortunately, pandas has a built-in implementation of Matplotlib that we can use. Plotting in pandas is as simple as appending a .plot() method to a series or dataframe.

Documentation:

    Plotting with Series
    Plotting with Dataframes

Line Pots (Series/Dataframe)

What is a line plot and why use it?

A line chart or line plot is a type of plot which displays information as a series of data points called 'markers' connected by straight line segments. It is a basic type of chart common in many fields. Use line plot when you have a continuous data set. These are best suited for trend-based visualizations of data over a period of time.

Let's start with a case study:

In 2010, Haiti suffered a catastrophic magnitude 7.0 earthquake. The quake caused widespread devastation and loss of life and aout three million people were affected by this natural disaster. As part of Canada's humanitarian effort, the Government of Canada stepped up its effort in accepting refugees from Haiti. We can quickly visualize this effort using a Line plot:

Question: Plot a line graph of immigration from Haiti using df.plot().

"""

# First, Extract the data series for Haiti.

haiti = df_canada.loc["Haiti", years] # passing in years 1980 - 2013 to exclude the 'total' column

haiti.head()

haiti.plot()

aiti.index = haiti.index.map(int) # let's change the index values of Haiti to type integer for plotting
haiti.plot(kind='line')

plt.title('Immigration from Haiti')
plt.ylabel('Number of immigrants')
plt.xlabel('Years')

plt.show() # need this line to show the updates made to the figure

# We can clearly notice how number of immigrants from Haiti spiked up from 2010 as Canada stepped up its efforts to accept refugees from Haiti. Let's annotate this spike in the plot by using the plt.text() method.

haiti.plot(kind='line')

plt.title('Immigration from Haiti')
plt.ylabel('Number of Immigrants')
plt.xlabel('Years')

# annotate the 2010 Earthquake. 
# syntax: plt.text(x, y, label)
plt.text(2000, 6000, '2010 Earthquake') # see note below

plt.show()