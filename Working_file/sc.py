from Tariff_df import *
import pandas as pd
import numpy as np
import os


user = input("which type of customer are you: ",  )
if user == "Business":
    Tariffs_3      = np.array(['P1','P2','P3','P4','P5','P6'])
    Energy_term_3  = np.array([0.387, 0.350, 0.319, 0.293, 0.266, 0.253]) #EUR/KWh
    Power_term_3   = np.array([0.045671833, 0.033543392, 0.016257762, 0.013830986, 0.009228504, 0.005896482])   # Euro per kw per day
    Billed_power_3 = np.array([18, 18, 18, 18, 18, 18])  ## in KW
    cons_p = []
    for i in Tariffs_3:
        cons_p6 = np.sum(r3[t2_np == i])
        cons_p.append(cons_p6)
    cons_np = np.array(cons_p)/1000
    tot_energy = np.sum(cons_np * Energy_term_3)/12
    tot_power = np.sum(Power_term_3 * Billed_power_3)* 30
    
    pv_energy_terms = 0.12
    pv_ppa = np.sum(r6)*pv_energy_terms/(12*1000)
    R2M = 6*10    # Euro / month

elif user == "Residential" or user == "Homeowner":
    Tariffs_2 = np.array(['P1','P2','P3'])
    Energy_term_2  = np.array([0.407, 0.320, 0.262])  #EUR/KWh
    Power_term_2   = np.array([0.081583562, 0.008432877])    # Euro per KW per day
    Billed_power_2 = np.array([3, 2])   ## in KW
    cons_p = []
    for i in Tariffs_2:
        cons_p6 = np.sum(r3[t1_np == i])
        cons_p.append(cons_p6)
    cons_np = np.array(cons_p)/1000
    tot_energy = np.sum(cons_np * Energy_term_2)/(12*19)+1  # for each household
    tot_power = (2/3)*(Power_term_2[0] * Billed_power_2[0])* 30 + (1/3)*(Power_term_2[1] * Billed_power_2[1])*30
    pv_energy_terms = 0.12
    pv_ppa = np.sum(r6)*pv_energy_terms/(12*1000*19)
    R2M = 2    # Euro / month
else:
    print("Please enter a valid customer type")



tax_electricity = 0.051127
meter_rent  = 0.81*30     # in Euro per month
em_service  = 2.06      # in Euro per month

IVA = 0.21       # 21 Percent

tot = (tot_energy + tot_power) * (1 + tax_electricity)
bef_iva = tot+R2M+em_service+meter_rent+pv_ppa
tot_inv = bef_iva * (1 + IVA)

## String Variables

monthly_energy = str(round(np.sum(cons_np)/12 , 2))
tot_energy = str(round(tot_energy, 2))
tot_power = str(round(tot_power, 2))
tot = str(round(tot, 2))
pv_ppa = str(round(pv_ppa, 2))
meter_rent = str(round(meter_rent, 2))
em_service = str(round(em_service, 2))
R2M = str(round(R2M, 2))
bef_iva = str(round(bef_iva, 2))
tot_inv = str(round(tot_inv, 2))


file = open("Energy_Bill_with_sc.txt", "w")
file.write("Energy Consumption per month in MWh : " + monthly_energy + "\n")
file.write("Invoiced Energy per month in Euro : " + tot_energy + "\n")
file.write("Invoiced Power per month in Euro : " + tot_power + "\n")
file.write("Invoice after Electricity tax: " + tot + "\n")
file.write("PV-PPA Without Electricity tax:" + pv_ppa + "\n")
file.write("Metered Equipment rental: in Euro " + meter_rent + "\n")
file.write("Electrical emergency service in Eur : " + em_service + "\n")
file.write("R2M compensation : " + R2M + "\n")
file.write("Invoice before IVA: " + bef_iva + "\n")
file.write("Total Invoice in Euros: " + tot_inv + "\n")

file.close()