import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np
style.use('ggplot')

web_stats = {
    'Day':[1,2,3,4,5,6],
    'Visitors':[13,222,32,43,55,64],
    'Bounce':[133,2422,332,423,552,643]
}

df = pd.DataFrame(web_stats)
df.set_index('Day',inplace=True)
# print(df.head())
# print(df['Visitors'])
# print(df[['Visitors','Bounce']])

# print(df.Visitors.tolist())
# print(np.array(df[['Visitors','Bounce']]))

df2 = pd.DataFrame(np.array(df[['Visitors','Bounce']]))

print(df2)