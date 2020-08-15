import os
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.animation import FuncAnimation
from datetime import datetime
import plotly.offline
from collections import Counter

plt.style.use('seaborn')

# Get path of the csv of today's date
os.chdir('Data')
csv_filename = os.listdir()[0]
os.chdir('..')
# print(os.getcwd())
csv_path = os.path.join('Data', csv_filename)
# print(csv_path)

df = pd.read_csv(csv_path, encoding = "ISO-8859-1", engine='python')
# df = pd.read_csv('Data/test.csv')
# print(df.info())
# overwriting data after changing format
# df["FECHA_ACTUALIZACION"] = pd.to_datetime(df["FECHA_ACTUALIZACION"]).dt.strftime('%d/%m/%Y')
# print(df.info())
# print(df['FECHA_ACTUALIZACION'])

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

sector_deaths = deaths['SECTOR']
sector_deaths = sector_deaths.astype('int64')
print(sector_deaths)
# print(sector_deaths.index)
# print(len(sector_deaths.index)) # This must be the same as number_of_deaths
# end of filtering

# instances of Counter
sector_counter = Counter()
sector_num = df['SECTOR']
for row in sector_num:
    sector_counter.update([row])

sector_d_counter = Counter()
for row in sector_deaths:
    sector_d_counter.update([row])

print("Total in each sector:",sector_counter)
print()
print("Total deaths in each sector:",sector_d_counter)
print()
# print(sector_counter.most_common(13))
# print(sector_d_counter.most_common(13))

# Append counters to lists
sector_ls = []
frequency = []
sector_d_ls = []
frequency_d = []

# print(type(sector_counter.most_common(13)))
# print('Unordered list',sector_counter.most_common(13)[:3])
sector_counter_ls = sector_counter.most_common(13).copy()
print('Unordered list',sector_counter_ls[:3])
sector_counter_ls.sort(key=lambda x:x[0])
print('Ordered list', sector_counter_ls)
d = dict(sector_counter_ls)
low, high = 1, 13
fill_sector_counter_ls = [(i, d.get(i)) for i in range(low, high + 1)]
print('Filled',fill_sector_counter_ls)
# print(type(fill_sector_counter_ls))

sector_d_counter_ls = sector_d_counter.most_common(13).copy()
print('\nUnordered list',sector_d_counter_ls[:3])
sector_d_counter_ls.sort(key=lambda x:x[0])
print('Ordered list', sector_d_counter_ls)
d_2 = dict(sector_d_counter_ls)
low_2, high_2 = min(d_2), max(d_2)
fill_sector_d_counter_ls = [(i, d_2.get(i)) for i in range(low_2, high_2 + 1)]
print('Filled',fill_sector_d_counter_ls)

for item in fill_sector_counter_ls:
    sector_ls.append(item[0])
    if not item[1]:
        frequency.append(0)
        continue
    frequency.append(item[1])

for item in sector_d_counter_ls:
    sector_d_ls.append(item[0])
    frequency_d.append(item[1])

print('\nLists of the total')
print(f'Sectors: {sector_ls} Frequencies: {frequency}')
print('Lists of the total deaths')
print(f'Sectors: {sector_d_ls} Frequencies: {frequency_d}')

key_s = ['1-CRUZ ROJA', '2-DIF', '3-ESTATAL', '4-IMSS', '5-IMSS-BIENESTAR', '6-ISSSTE', '7-MUNICIPAL', '8-PEMEX', '9-PRIVADA', '10-SEDENA', '11-SEMAR', '12-SSA', '13-UNIVERSITARIO', '99-NO ESPECIFICADO']
mpl_fig = plt.figure()
# for i in range(0,len(sector_ls)):
    # plt.bar(sector_ls[i],frequency[i],color=cm.Set1(1.*i/len(sector_ls)), label=key_s[i])

plt.bar(sector_d_ls,frequency_d, color='#2F4F4F', label='Deaths')
plt.legend(loc='upper left')
sec_label = [1,2,3,4,5,6,7,8,9,10,11,12,13]
plt.xticks(ticks=sec_label, labels=sec_label)
plt.title('Deaths within each health sector')
plt.xlabel('Sector')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

# Export to plotly
os.chdir('..')
os.chdir('html')
# mpl_fig.update_layout(showlegend=True)
unique_url = plotly.offline.plot_mpl(mpl_fig, filename='deaths_by_sector.html')
print(unique_url)