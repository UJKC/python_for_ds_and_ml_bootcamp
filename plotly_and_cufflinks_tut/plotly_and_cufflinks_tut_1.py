from plotly import __version__
import numpy as np
import pandas as pd
import cufflinks as cf
import plotly.offline as pyo
#download_plotlyjs, init_notebook_mode, plot, iplot
import matplotlib.pyplot as mplpp
import plotly.graph_objects as go

pyo.init_notebook_mode(connected= True) #connect js to python

cf.go_offline() #be offline

#data
df = pd.DataFrame(np.random.randn(100, 4), columns= ["A", "B", "C", "D"])
#print(df)

df2 = pd.DataFrame({'categories': ["A", "B", "C"], "Values": ["32", "43", "50"]})
#print(df2)

#plot

#1
df.plot()
mplpp.show()

#2

#trace
trace = go.Scatter(x= df.index, y= df)

#layout
layout = go.Layout(title='Offline Plot', xaxis=dict(title='X-axis'), yaxis=dict(title='Y-axis'))

#Figure
fig = go.Figure(data=[trace], layout=layout)

#plot
pyo.iplot(fig)
mplpp.show()