import os
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
# import plotly.tools as tls
from collections import Counter

plt.style.use('seaborn')

# Get path of the csv of today's date
os.chdir('Data')
csv_filename = os.listdir()[0]
os.chdir('..')
csv_path = os.path.join('Data', csv_filename)
df = pd.read_csv(csv_path, encoding = "ISO-8859-1", engine='python')
# df = pd.read_csv('Data/test.csv')

# Time stamps
mod_time = os.stat(csv_path).st_mtime
ts = datetime.fromtimestamp(mod_time)
# Print the Timestamp of the file
# print(ts)
# Create the DateOffset
day = pd.tseries.offsets.DateOffset(n = 1)
# Substract the dateoffset to the given timestamp
new_timestamp = ts - day
# Print the timestamp of the previous day
print("All the data is updated until ",new_timestamp.strftime('%d/%m/%Y'))

# Filters
filter = df['FECHA_DEF'] != '9999-99-99'
deaths = df.where(filter).dropna()
# print(deaths)
number_of_deaths = deaths.shape[0]
print('Total number of deaths',number_of_deaths)

ages_deaths = deaths['EDAD']
ages_deaths = ages_deaths.astype('int64')
print(ages_deaths)
# print(ages_deaths.index)
# print(len(ages_deaths.index)) # This must be the same as number_of_deaths
# end of filtering

# instances of Counter
ages_counter = Counter()
ages_num = df['EDAD']
for row in ages_num:
    ages_counter.update([row])

ages_d_counter = Counter()
for row in ages_deaths:
    ages_d_counter.update([row])

print("Total ages:",ages_counter)
print()
print("Total ages of dead people:",ages_d_counter)
print()

ages_counter_ls = ages_counter.most_common(30).copy()
print('Unordered list',ages_counter_ls[:])
ages_counter_ls.sort(key=lambda x:x[0])
print('Ordered list', ages_counter_ls)
ages_d_counter_ls = ages_d_counter.most_common(30).copy()
print('\nUnordered list',ages_d_counter_ls[:])
ages_d_counter_ls.sort(key=lambda x:x[0])
print('Ordered list', ages_d_counter_ls)


print(ages_num.mean())
print(ages_num.median())
print(ages_deaths.mean())
print(ages_deaths.median())

bins_range = [0,10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]
fig = plt.figure()
plt.hist(ages_num, bins=bins_range, edgecolor='black', label='Ages of all population under research')
plt.hist(ages_deaths, bins=bins_range, edgecolor='black', label='Deaths', color='tab:red')
plt.axvline(ages_num.mean(), color='tab:cyan', label='Age Mean of population', linewidth=2)
plt.axvline(ages_num.median(), color='tab:olive', label='Age Median of population', linewidth=2)
plt.axvline(ages_deaths.mean(), color='tab:purple', label='Age Mean of people who passed away', linewidth=2)
plt.axvline(ages_deaths.median(), color='tab:orange', label='Age Median of people who passed away', linewidth=2)
plt.legend()
plt.title('Ages Distribution')
plt.xlabel('Ages')
plt.ylabel('Frequency')

plt.tight_layout()

# Export png
os.chdir('..')
os.chdir('png')
plt.savefig('Ages_Histogram.png')
plt.show()
# os.chdir('Figs/html')
# # Export to plotly
# plotly_fig = tls.mpl_to_plotly(fig) # This translate object to plotly to modify certain parameters
# plotly_fig['layout']['showlegend'] = True
# plotly_fig.write_html('Ages_Distribution.html') # py.iplot(plotly_fig)  for IPython