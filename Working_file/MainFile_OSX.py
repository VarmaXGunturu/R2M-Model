from PV_OSX import *
from Consumption_OSX import *
from Energy_flux_OSX import *
import pandas as pd
import time
import numpy as np
import os
import csv

"The Main file is the only file you need to run"

"The parameters you can change"
"————————————————————————————————————————————"
"Adjusting PV parameters"
area = 2.576 # m^2
panel_efficiency = 0.203
loss = 0.8
number_panels = 40

"Adjusting battery parameters"
deep_battery = 0.05  #The maximum allowed charge deepth 
bat_charge_speed = 1400 #charging speed, Wh

"Adjusting charging time"
char_time_start = 3  #charging start time
char_time_stop = 4   #charging stop time

"Capacity of  battery"
capacity_battery = [3000,2000,1000,3000] #batter's capacity_battery, Wh

"————————————————————————————————————————————"
"The number of components have to match the number of customers"
pv_allocation = pd.read_csv(r'../Input_Data/PV_split/Pv_split.csv')

"The parameters you do not need to change"
n_coustomer = number_customers() # number of customers, depend on number of consumptions files you upload
pv = PV(area,panel_efficiency,loss,number_panels)
"Creating Energy flux data file"
for i in range(n_coustomer):
    parameters_consumption = [1,capacity_battery[i],deep_battery,bat_charge_speed,char_time_start,char_time_stop]
    in_file_prefix = r'../Input_Data/customer_consumption/consumption_data'
    in_file_name = in_file_prefix + str(i) + '.csv' 
    out_file_prefix = r'../Output_Data/EnergyFlux_data/con_gen_data'
    out_file_name = out_file_prefix + str(i) + '.csv' 
    parameters_consumption[0] =  pv_allocation.iloc[:,i]
    with open(out_file_name, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(consumer_profile(in_file_name,pv,parameters_consumption))

#long process here
time.sleep(6)
done = True

"Billing Customers"

from Tariff_df_OSX import *

"The parameters you can change"
"————————————————————————————————————————————"
"Updating Tariffs"  

"3.0 TD"

Energy_term_3  = np.array([0.387, 0.350, 0.319, 0.293, 0.266, 0.253]) # EUR/MWh
Power_term_3   = np.array([0.045671833, 0.033543392, 0.016257762, 0.013830986, 0.009228504, 0.005896482])   # Euro per kw per day
Billed_power_3 = np.array([18, 18, 18, 18, 18, 18])  # in KW

"2.0 TD"

Energy_term_2  = np.array([0.407, 0.320, 0.262])  # EUR/MWh
Power_term_2   = np.array([0.081583562, 0.008432877])    # Euro per kw per day
Billed_power_2 = np.array([4, 4])  # in KW

"————————————————————————————————————————————"

# These might vary with the location.
tax_electricity = 0.051127  # 5.11 percentage ,  Electricity tax
meter_rent  = 0.81*30      # in Euro per month ,  Metered equipment rental
em_service  = 2.06      # in Euro per month , Electrical Emergancy service
IVA = 0.21       # 21 Percent, equivalent to VAT (Value Added Tax)
pv_energy_terms = 0.12, # EUR/KWh , Power purchase agreement

User_input = input("Are you a self-consumer [Yes/No]: ")  # Answer "Yes" or "No"

if User_input == "Yes":
    from sc_OSX import *

elif User_input == "No":
    from not_sc_OSX import *

else:
    print("Please Answer with Yes or No")