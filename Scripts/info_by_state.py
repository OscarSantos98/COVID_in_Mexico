import os
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib import dates as mpl_dates
from datetime import datetime, timedelta
import plotly.offline
import plotly.tools as tls

plt.style.use('seaborn')

os.chdir(r'C:\Users\oscar\Documents\Hackatones\CdeCMX Challenge\Datos')
df_confirmed = pd.read_csv('Casos_Diarios_Estado_Nacional_Confirmados_20200806.csv')
df_suspicious = pd.read_csv('Casos_Diarios_Estado_Nacional_Sospechosos_20200812.csv')
df_deaths = pd.read_csv('Casos_Diarios_Estado_Nacional_Defunciones_20200812.csv')
df_negative = pd.read_csv('Casos_Diarios_Estado_Nacional_Negativos_20200812.csv')

population = df_confirmed['poblacion'].iloc[:-1]
state = df_confirmed['nombre'].iloc[:-1]

# for i in range(0,len(state)):
#     if i % 2 == 0:
#         plt.barh(state[i],population[i],color=cm.tab20b(1.*i/len(state)))
#     else:
#         plt.barh(state[i],population[i],color=cm.tab20(1.*i/len(state)))

# plt.barh(state,population)
# plt.title('Population of México')
# plt.xlabel('Population')
# plt.tight_layout()
# plt.show()

dates_confirmed = df_confirmed.iloc[:-1,3:205]  # Get all required columns (excluding national) from day 1 until 31 July
dates_confirmed_ls = []
dates_suspicious = df_suspicious.iloc[:-1,3:188]  # Get all required columns (excluding national) from day 1 until 31 July
dates_suspicious_ls = []
dates_deaths = df_deaths.iloc[:-1,3:140]  # Get all required columns (excluding national) from day 1 until 31 July
dates_deaths_ls = []
dates_negative = df_negative.iloc[:-1,3:217]  # Get all required columns (excluding national) from day 1 until 31 July
dates_negative_ls = []

print(dates_confirmed.shape)
print(dates_suspicious.shape)
print(dates_deaths.shape)
print(dates_negative.shape)

# pos=0
# Create the DateOffset
# day = pd.tseries.offsets.DateOffset(n = 1)
for date in dates_confirmed:
    # print(date)
    dates_confirmed_ls.append(pd.to_datetime(date, dayfirst=True))
    # tmstmp = pd.to_datetime(date, dayfirst=True)
    # Adding the dateoffset to the given timestamp
    # new_timestamp = tmstmp - day
    # dates_confirmed_ls.append(new_timestamp)
    # dates_confirmed_ls.append(date)
    # pos+=1
# print(dates_confirmed_ls)
# pos=0
for date in dates_suspicious:
    # print(date)
    dates_suspicious_ls.append(pd.to_datetime(date, dayfirst=True))
    # tmstmp = pd.to_datetime(date, dayfirst=True)
    # Adding the dateoffset to the given timestamp
    # new_timestamp = tmstmp - day
    # dates_suspicious_ls.append(new_timestamp)
    # dates_suspicious_ls.append(date)
    # pos+=1
# print(dates_suspicious_ls)
# pos=0
for date in dates_deaths:
    # print(date)
    dates_deaths_ls.append(pd.to_datetime(date, dayfirst=True))
    # tmstmp = pd.to_datetime(date, dayfirst=True)
    # Adding the dateoffset to the given timestamp
    # new_timestamp = tmstmp - day
    # dates_deaths_ls.append(new_timestamp)
    # dates_deaths_ls.append(date)
    # pos+=1
# print(dates_deaths_ls)
# pos=0
for date in dates_negative:
    # print(date)
    dates_negative_ls.append(pd.to_datetime(date, dayfirst=True))
    # tmstmp = pd.to_datetime(date, dayfirst=True)
    # Adding the dateoffset to the given timestamp
    # new_timestamp = tmstmp - day
    # dates_negative_ls.append(new_timestamp)
    # dates_negative_ls.append(date)
    # pos+=1
# print(dates_negative_ls)

# print(len(state))
# print(state)
# print(len(dates_confirmed.index))
# print(len(dates_suspicious.index))
# print(len(dates_deaths.index))
# print(len(dates_negative.index))
# print(dates_confirmed.head())
# print(dates_suspicious)
# print(dates_deaths)
# print(dates_negative)

os.chdir(r'C:\Users\oscar\Documents\Hackatones\CdeCMX Challenge\Scripts\Figs\html')
urls = []
# print("Confirmed: ",dates_confirmed.iloc[0,201])
# print("Total: ",df_confirmed.iloc[-1,204])
# percent = (dates_confirmed.iloc[0,201]/df_confirmed.iloc[-1,204])*100
# print("Percentage: ",percent)
# confirmed_sum = 0
# for i in range(dates_confirmed.shape[1]):
#     confirmed_sum += dates_confirmed.iloc[0,i]
# print("Acumulated confirmated cases: ",confirmed_sum)
confirmed_total_sum = 0
for i in range(dates_confirmed.shape[1]):
    confirmed_total_sum += df_confirmed.iloc[-1,i+3]
print("Acumulated Total: ",confirmed_total_sum)
# acc_percent = (confirmed_sum/confirmed_total_sum)*100
# print("Percentage: ",acc_percent)
# Total Deaths
deaths_total_sum = 0
for i in range(dates_deaths.shape[1]):
    deaths_total_sum += df_deaths.iloc[-1,i+3]
print("Acumulated Total: ",deaths_total_sum)

for i in range(len(state)): # Iterate over all states
    # plt.plot(dates_confirmed_ls, dates_confirmed.iloc[i]) # Normal plot
    fig,ax = plt.subplots()
    ax.plot_date(dates_confirmed_ls, dates_confirmed.iloc[i], linestyle = 'solid', label = 'Confirmed', color='tab:red', markersize=5)
    ax.plot_date(dates_suspicious_ls, dates_suspicious.iloc[i], linestyle = 'dotted', label = 'Suspicious', color='tab:orange', markersize=5)
    ax.plot_date(dates_deaths_ls, dates_deaths.iloc[i], linestyle = 'dashdot', label = 'Deaths', color='tab:brown', markersize=5)
    ax.plot_date(dates_negative_ls, dates_negative.iloc[i], linestyle = 'dashed', label = 'Negative', color='tab:blue', markersize=5)
    plt.gcf().autofmt_xdate()   # gcf stands for get current figure, and we apply autoformat to that object
    date_format = mpl_dates.DateFormatter('%d-%b')
    plt.gca().xaxis.set_major_formatter(date_format)   # gca stands for get current axes
    plt.title('Daily cases in ' + state[i].capitalize())
    plt.xlabel('Dates')
    plt.ylabel('Cases')
    plt.tight_layout()
    # plt.legend(fontsize='xx-large', loc='upper left')
    # Export plot to plotly
    filename = state[i].lower() + '_fig.html'
    # print(filename)
    # urls.append(plotly.offline.plot_mpl(fig, filename=filename))  # this export directly
    # plotly_fig = tls.mpl_to_plotly(fig) # This translate object to plotly to modify certain parameters
    # plotly_fig['layout']['showlegend'] = True
    # plotly_fig.write_html(filename) # py.iplot(plotly_fig)  for IPython
    # del fig
    # percent = (dates_confirmed.iloc[i,201]/df_confirmed.iloc[-1,204])*100
    confirmed_sum = 0
    for j in range(dates_confirmed.shape[1]):
        confirmed_sum += dates_confirmed.iloc[i,j]
    print(f"Acumulated confirmated cases in {state[i]}: {confirmed_sum}")
    acc_c_percent = (confirmed_sum/confirmed_total_sum)*100
    print("Percentage: ",acc_c_percent)
    # print(f'{state[i]} corresponds to the {percent}% of the contagious of the country')
    deaths_sum = 0
    for j in range(dates_deaths.shape[1]):
        deaths_sum += dates_deaths.iloc[i,j]
    print(f"Acumulated deaths in {state[i]}: {deaths_sum}")
    acc_d_percent = (deaths_sum/deaths_total_sum)*100
    print("Percentage: ",acc_d_percent)

    # plt.plot_date(dates_confirmed_ls, dates_confirmed.iloc[i], linestyle = '--', markersize=4)    # All states

# print(urls)
# plt.plot_date(dates_confirmed_ls, dates_confirmed.iloc[0], linestyle = 'solid')   # example

# plt.gcf().autofmt_xdate()   # gcf stands for get current figure, and we apply autoformat to that object

# date_format = mpl_dates.DateFormatter('%d-%b')

# plt.gca().xaxis.set_major_formatter(date_format)   # gca stands for get current axes

# plt.xlabel('Dates')
# plt.ylabel('Cases')
# plt.legend(state, fontsize='small', loc='upper left', ncol=2)    # This uses the label arguement in plt.plot
# plt.tight_layout()
# plt.show()
