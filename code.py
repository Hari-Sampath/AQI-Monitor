import pandas as pd

df=pd.read_csv("aqi_checkpoints.csv")
df1=pd.read_csv("aqi_categories.csv")
def find_cat(AQI):
   row=df1[(df1["AQI_Low"]<=AQI)&(AQI<=df1["AQI_High"])]
   if row.empty:
      return "Out of range","Unknown"
   ans1=row.iloc[0]["Category"]
   ans2=row.iloc[0]["Color"]
   return ans1,ans2

def getsub_index(value,pollutant):
  #getting the correct row
  row=df[(df["Pollutant"]==pollutant)&(df["Conc_Low"]<=value)&(value<=df["Conc_High"])]
  #found the rown within that range
  if row.empty:
     return 0
  y1=row.iloc[0]["AQI_Low"]
  y2=row.iloc[0]["AQI_High"]
  x1=row.iloc[0]["Conc_Low"]
  x2=row.iloc[0]["Conc_High"]
  return y1+ (value-x1)*(y2-y1)/(x2-x1)




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
pollutants=["PM2.5","PM10","NO2","O3","CO","SO2","NH3","Pb"]
aqi_values=[]
for i in range(8):
    value=values[i]
    pollutant=pollutants[i]
    sub_index=getsub_index(value,pollutant)
    aqi_values.append(sub_index)

AQI=round(max(aqi_values))
cat,color=find_cat(AQI)
print("Category: ",cat)
print("Color: ",color)

