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

gender_deaths = deaths['SEXO']
gender_deaths = gender_deaths.astype('int64')
print(gender_deaths)
# print(gender_deaths.index)
# print(len(gender_deaths.index)) # This must be the same as number_of_deaths
# end of filtering

# instances of Counter
gender_counter = Counter()
gender_num = df['SEXO']
for row in gender_num:
    gender_counter.update([row])

gender_d_counter = Counter()
for row in gender_deaths:
    gender_d_counter.update([row])

print("Total gender:",gender_counter)
print()
print("Total gender of dead people:",gender_d_counter)
print()

gender_counter_ls = gender_counter.most_common(30).copy()
print('Unordered list',gender_counter_ls[:])
gender_counter_ls.sort(key=lambda x:x[0])
print('Ordered list', gender_counter_ls)
gender_d_counter_ls = gender_d_counter.most_common(30).copy()
print('\nUnordered list',gender_d_counter_ls[:])
gender_d_counter_ls.sort(key=lambda x:x[0])
print('Ordered list', gender_d_counter_ls)

bins_range = [1,1.5,2]
fig = plt.figure()
plt.hist(gender_num, bins=bins_range, edgecolor='black', label='Gender of all population under research')
plt.hist(gender_deaths, bins=bins_range, edgecolor='black', label='Deaths according to gender', color='tab:red')
# gen_label = ['Female','None','Male']
plt.xticks([])
plt.legend(loc='center')
plt.title('Gender Distribution')
plt.xlabel('Gender (Left-Female, Right-Male)')
plt.ylabel('Frequency')

plt.tight_layout()

# Export png
os.chdir('..')
os.chdir('png')
plt.savefig('Gender_Histogram.png')
plt.show()
# os.chdir('Figs/html')
# # Export to plotly
# plotly_fig = tls.mpl_to_plotly(fig) # This translate object to plotly to modify certain parameters
# plotly_fig['layout']['showlegend'] = True
# plotly_fig.write_html('gender_Distribution.html') # py.iplot(plotly_fig)  for IPython