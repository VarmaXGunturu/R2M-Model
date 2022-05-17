import pandas as pd
import numpy as np
from matplotlib import pyplot as plt 
"The parameters you can change"
"————————————————————————————————————————————"
file_name = 'con_gen_data3.csv'  # The name is the file name of output file
"————————————————————————————————————————————"

prefix = r'..\..\Output_Data\EnergyFlux_data'
path = prefix  + '\\' + file_name

"Surplus in a day ( average for a year) without battery"
con_gen_curve = pd.read_csv(path,engine = "python" )
day_surplus=np.zeros(24)
for y in range(len(con_gen_curve)):
    for i in range(24):
        h=y%24 
        if h == i:
            day_surplus[i] += con_gen_curve.loc[y,'surplus']
day_surplus=day_surplus/365
x1=range(24)
x2=day_surplus
string='Average surplus in a day'
plt.title(string) 
plt.xlabel("Time h") 
plt.ylabel("Surplus Wh")
plt.plot(x1,x2)
plt.savefig(string+'.png')
plt.close()

"Surplus in a month ( average for a year)"
month_surplus=np.zeros(24*30)
for y in range(len(con_gen_curve)):
    for i in range(24*30):
        h=y%(24*30) 
        if h == i:
            month_surplus[i] += con_gen_curve.loc[y,'surplus']
month_surplus=month_surplus/12

x3=range(24*30)
x4=month_surplus
string='Average surplus in a month without battery'
plt.title(string) 
plt.xlabel("Time h") 
plt.ylabel("Surplus Wh")
plt.plot(x3,x4)
plt.savefig(string+'.png')
plt.close()

"power consumption without battery in a day"
day_con=np.zeros(24)
day_grid=np.zeros(24)
day_pv=np.zeros(24)
for y in range(len(con_gen_curve)):
    for i in range(24):
        h=y%24 
        if h == i:
            day_surplus[i] += con_gen_curve.loc[y,'surplus']
            day_con[i] += con_gen_curve.loc[y,'consumption'] 
            day_pv[i] += con_gen_curve.loc[y,'generation_pv'] 
            day_grid[i] += con_gen_curve.loc[y,'consumption']  - con_gen_curve.loc[y,'generation_pv'] + con_gen_curve.loc[y,'surplus']          
day_con=day_con/365
day_pv=day_pv/365
day_grid = day_grid/365
day_surplus=day_surplus/365
x5=day_con
x6=day_grid
x7=day_pv

string='Average consumption&PV&Grid consumption over a day without battery'
plt.title(string) 
plt.plot(x1,x5,label='Total consumption')
plt.plot(x1,x6,label='Grid consumption')
plt.plot(x1,x7,label='PV')
plt.xlabel("Time h") 
plt.ylabel("Energy Consumption Wh")
plt.legend()
plt.savefig(string+'.png')
plt.close()
  

"power consumption without battery in a month"              
month_con=np.zeros(24*30)
month_grid=np.zeros(24*30)
month_pv=np.zeros(24*30)
for y in range(len(con_gen_curve)):
    for i in range(24*30):
        h=y%(24*30) 
        if h == i:
            month_con[i] += con_gen_curve.loc[y,'consumption'] 
            month_pv[i] += con_gen_curve.loc[y,'generation_pv'] 
            month_grid[i] += con_gen_curve.loc[y,'consumption']  - con_gen_curve.loc[y,'generation_pv'] + con_gen_curve.loc[y,'surplus']          
month_con = month_con/12
month_pv = month_pv/12
month_grid = month_grid/12
x8=month_con
x9=month_grid
x10=month_pv
string='Average consumption&PV&Grid consumption over a month without battery'
plt.title(string) 
plt.plot(x3,x8,label='Total consumption')
plt.plot(x3,x9,label='Grid consumption')
plt.plot(x3,x10,label='PV')
plt.xlabel("Time h") 
plt.ylabel("Energy Consumption Wh")
plt.legend(loc=2)
plt.savefig(string+'.png')
plt.close()

"power consumption with battery in a day"         
day_dump=np.zeros(24)
for y in range(len(con_gen_curve)):
    for i in range(24):
        h=y%24 
        if h == i:
            day_dump[i] += con_gen_curve.loc[y,'en_dump1']
day_dump=day_dump/365
x11=range(24)
x12=day_dump
string='Dumped energy over a day(with battery)'
plt.title(string) 
plt.xlabel("Time h") 
plt.ylabel("Dumped energy Wh")
plt.plot(x11,day_surplus,'--',label='Surplus')
plt.plot(x11,x12,label='Dumped energy')
plt.legend()
plt.savefig(string+'.png')
plt.close()

"power consumption with battery in a month"              
month_con_b=np.zeros(24*30)
month_grid_b=np.zeros(24*30)
month_pv_b=np.zeros(24*30)
for y in range(len(con_gen_curve)):
    for i in range(24*30):
        h=y%(24*30) 
        if h == i:
            month_con_b[i] += con_gen_curve.loc[y,'consumption'] 
            month_pv_b[i] += con_gen_curve.loc[y,'generation_pv'] 
            month_grid_b[i] += con_gen_curve.loc[y,'use_power_grid1']       
month_con_b = month_con_b/12
month_pv_b = month_pv_b/12
month_grid_b = month_grid_b/12
x13=month_con_b
x14=month_grid_b
x15=month_pv_b
string='Average consumption&PV&Grid consumption over a month with battery'
plt.title(string) 
plt.plot(x3,x13,label='Total consumption')
plt.plot(x3,x14,label='Grid consumption')
plt.plot(x3,x15,label='PV')
plt.xlabel("Time h") 
plt.ylabel("Energy Consumption Wh")
plt.legend(loc=2)
plt.savefig(string+'.png')
plt.close()

"power consumption with battery in a day"              
day_con_b=np.zeros(24)
day_grid_b=np.zeros(24)
day_pv_b=np.zeros(24)
for y in range(len(con_gen_curve)):
    for i in range(24):
        h=y%(24) 
        if h == i:
            day_con_b[i] += con_gen_curve.loc[y,'consumption'] 
            day_pv_b[i] += con_gen_curve.loc[y,'generation_pv'] 
            day_grid_b[i] += con_gen_curve.loc[y,'use_power_grid1']       
day_con_b = day_con_b/365
day_pv_b = day_pv_b/365
day_grid_b = day_grid_b/365
x16=day_con_b
x17=day_grid_b
x18=day_pv_b
string='Average consumption&PV&Grid consumption over a day with battery'
plt.title(string) 
plt.plot(x1,x16,label='Total consumption')
plt.plot(x1,x17,label='Grid consumption')
plt.plot(x1,x18,label='PV')
plt.xlabel("Time h") 
plt.ylabel("Energy Consumption Wh")
plt.legend(loc=2)
plt.savefig(string+'.png')
plt.close()

"battery status in a day"        
day_b=np.zeros(24)
for y in range(len(con_gen_curve)):
    for i in range(24):
        h=y%(24) 
        if h == i:
            day_b[i] += con_gen_curve.loc[y,'battery_stat1'] 
      
day_b = day_b/365
x19 = day_b
string='battery status in a day'
plt.title(string) 
plt.plot(x1,x19,label='battery status')
plt.xlabel("Time h") 
plt.ylabel("Battery status Wh")
plt.legend(loc=2)
plt.savefig(string+'.png')
plt.close()


"battery status in a month"        
month_b=np.zeros(24*30)
for y in range(len(con_gen_curve)):
    for i in range(24*30):
        h=y%(24*30) 
        if h == i:
            month_b[i] += con_gen_curve.loc[y,'battery_stat1'] 
      
month_b = month_b/12
x20 = month_b
string='battery status in a month'
plt.title(string) 
plt.plot(x3,x20,label='battery status')
plt.xlabel("Time h") 
plt.ylabel("Battery status Wh")
plt.legend(loc=2)
plt.savefig(string+'.png')
plt.close()


'''Hourly-wise data'''


def get_hour_wise(data):
    hourly_con, hourly_gen, hourly_pow, hourly_sur = [], [], [], []
    for hour in range(1, 25):
        hourly_df = data[data['time_day'] == hour]
        hourly_con.append(hourly_df['consumption'].mean())
        hourly_gen.append(hourly_df['generation_pv'].mean())
        hourly_pow.append(hourly_df['use_power_grid1'].mean())
        hourly_sur.append(hourly_df['surplus'].mean())

    # change the order
    hourly_con = [hourly_con[-1]] + hourly_con[:-1]
    hourly_gen = [hourly_gen[-1]] + hourly_gen[:-1]
    hourly_pow = [hourly_pow[-1]] + hourly_pow[:-1]
    hourly_sur = [hourly_sur[-1]] + hourly_sur[:-1]

    return hourly_con, hourly_gen, hourly_pow, hourly_sur


def plot_hour_wise(hourly_con, hourly_gen, hourly_pow, month_idx):
    x = range(24)
    plt.plot(x, hourly_con, label='Customer usage')
    plt.plot(x, hourly_gen, label='PV')
    plt.plot(x, hourly_pow, label='Grid consumption')
    plt.xlabel("hour of day/h")
    plt.ylabel("Energy Consumption/Wh")
    plt.legend(loc=1)
    plt.ylim(ymin=0)
    plt.xlim(xmin=0)
    plt.title(f'Average hourly data in Month {month_idx}')
    plt.savefig(f'hourly_of_month{month_idx}.png')
    plt.close()


HOURS = 24
MONTH_DAYS = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

"hourly wise data with battery"

for m, _ in enumerate(MONTH_DAYS):
    if m == 0:
        st, ed = m, HOURS * MONTH_DAYS[m]
    else:
        st, ed = np.sum(MONTH_DAYS[:m]) * HOURS, np.sum(MONTH_DAYS[:m + 1]) * HOURS
    monthly_data = data[st:ed]
    hourly_con, hourly_gen, hourly_pow, hourly_sur = get_hour_wise(monthly_data)
    plot_hour_wise(hourly_con, hourly_gen, hourly_pow, m + 1)



"hourly wise data without battery"
grid_con = []


def plot_hour_wise_nobat(hourly_con, hourly_gen, grid_con, month_idx):
    x = range(24)
    plt.plot(x, hourly_con, label='Customer usage')
    plt.plot(x, hourly_gen, label='PV')
    plt.plot(x, grid_con, label='Grid consumption')
    plt.xlabel("hour of day/h")
    plt.ylabel("Energy Consumption/Wh")
    plt.legend(loc=1)
    plt.ylim(ymin=0)
    plt.xlim(xmin=0)
    plt.title(f'Average hourly data in Month {month_idx}')
    plt.savefig(f'NB hourly_of_month{month_idx}.png')
    plt.close()


for m, _ in enumerate(MONTH_DAYS):
    if m == 0:
        st, ed = m, HOURS * MONTH_DAYS[m]
    else:
        st, ed = np.sum(MONTH_DAYS[:m]) * HOURS, np.sum(MONTH_DAYS[:m + 1]) * HOURS
    monthly_data = data[st:ed]
    hourly_con, hourly_gen, hourly_pow, hourly_sur = get_hour_wise(monthly_data)
    # grid_con = hourly_con - hourly_gen + hourly_sur
    grid_con = list(np.array(hourly_con) - np.array(hourly_gen) + np.array(hourly_sur))
    plot_hour_wise_nobat(hourly_con, hourly_gen, grid_con, m + 1)

all_hourly_con, all_hourly_gen, all_hourly_pow, all_hourly_sur = get_hour_wise(data)
all_grid_con =list(np.array(all_hourly_con) - np.array(all_hourly_gen) + np.array(all_hourly_sur))
plot_hour_wise(all_hourly_con, all_hourly_gen, all_grid_con, 'all')
