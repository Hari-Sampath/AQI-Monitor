import pandas as pd

df=pd.read_csv("aqi_checkpoints.csv")
def getsub_index(value,pollutant):
  



print("Enter the measured values for all the pollutants: ")
values=[]
values.append(float(input("Enter the value for PM2.5: ")))
values.append(float(input("Enter the value for PM10: ")))
values.append(float(input("Enter the value for NO2: ")))
values.append(float(input("Enter the value for O3: ")))
values.append(float(input("Enter the value for CO: ")))
values.append(float(input("Enter the value for SO2: ")))
values.append(float(input("Enter the value for NH3: ")))
values.append(float(input("Enter the value for Pb: ")))
list=["PM2.5","PM10","NO2","O3","CO","SO2","NH3","Pb"]
aqi_values=[]
for i in range(8):
    value=value[i]
    pollutant=list[i]
    sub_index=getsub_index(value,pollutant)
    aqi_values.append(sub_index)
