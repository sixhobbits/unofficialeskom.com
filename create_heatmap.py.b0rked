import matplotlib as mpl
mpl.rcParams['figure.dpi'] = 300
mpl.rcParams['ytick.labelsize'] = 'x-small'

import calmap
import pandas as pd
import requests

from datetime import datetime

# read ESP's CSV
r = requests.get("https://docs.google.com/spreadsheets/d/1ZpX_twP8sFBOAU6t--Vvh1pWMYSvs60UXINuD5n-K08/gviz/tq?tqx=out:csv&sheet=EskomSePush_history")
with open("loadshedding.csv", "wb") as f:
    f.write(r.content)
df = pd.read_csv("loadshedding.csv")

# add a new row for today with the most recent stage
new_row = {'created_at': datetime.now().strftime("%Y-%m-%d %H:00:00"), 'stage': df.iloc[0]['stage']}
new_row = pd.DataFrame(new_row,index=[0])

df = pd.concat([new_row, df.loc[:]])

# convert to date time
df['created_at'] = pd.to_datetime(df['created_at'])
df['stage'] = df['stage'].astype(int)

# round all changes to 30 minutes
df['created_at'] = df['created_at'].dt.floor('30T')

# sort with oldest data first
df = df.sort_values(by=['created_at'])

# create all 30 minute dates in range
oldest = list(df.head(1)['created_at'])[0]
newest = list(df.tail(1)['created_at'])[0]
all_dates = pd.DataFrame(pd.date_range(oldest, newest, freq="30min"), columns=['created_at'])

# use the previous change to fill out missing data
all_dates = pd.merge(df, all_dates, how='right').fillna(method="ffill")

# add some useful grouping shortcuts
all_dates['year_week'] = all_dates['created_at'].map(lambda x: x.strftime('%Y-%V'))
all_dates['year_month'] = all_dates['created_at'].map(lambda x: x.strftime('%Y-%m'))
all_dates['year'] = all_dates['created_at'].map(lambda x: x.strftime('%Y'))
all_dates['month'] = all_dates['created_at'].map(lambda x: x.strftime('%m'))
all_dates['week'] = all_dates['created_at'].map(lambda x: x.strftime('%V'))
all_dates['year_month_day'] = all_dates['created_at'].map(lambda x: x.strftime('%Y-%m-%d'))

# write out to a CSV for more fun later
all_dates.to_csv("out.csv")

events = all_dates[['created_at','stage']]
events.set_index('created_at', inplace=True)
events = events.squeeze()



for year in [2023]:
    yearplot = calmap.yearplot(events, year=year, how='max')
    yearplot.get_figure().savefig(f"docs/heatmap/img/{year}.png", bbox_inches='tight')
    yearplot.clear()
