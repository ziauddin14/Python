import pandas as pd 

df = pd.read_csv('fue_station.csv')

print(df.head(2))
print(df.shape)

# Kaunsa fuel sabse zyada hai?
fuel_type = df['Fuel Type Code'].value_counts()
print(fuel_type)
# us fuel type ka naam 
print(fuel_type.index[0])

#Kaunsa fuel type konsy state mein sabse zyada hai?
state_fuel = df.groupby('State')['Fuel Type Code'].value_counts()
print(state_fuel)

# Kis state mein sabse zyada stations hain? + us state ka naam 
state = df['State'].value_counts()
print(state.index[0])

# Public stations kitni hain?
public_stations = df[df['Groups With Access Code'] == 'Public']
print(public_stations.shape[0])

#kaunsy state mein sabse zyada public stations hain? 
public_state = df[df['Groups With Access Code'] == 'Public']['State'].value_counts()
print(public_state.index[0]) 
    
# EV stations kitni hain?
ev_stations = df[df['Fuel Type Code'] == 'ELEC']
print(ev_stations.shape[0])

# Kitni stations 24/7 hain?
twenty_four_seven_stations = df[df['Access Days Time'] == '24 hours daily']
print(twenty_four_seven_stations.shape[0])

# Kitni stations last 5 years mein update hui hain?
recent_stations = df[df['Updated At'] >= '2022-01-01']
print(recent_stations.shape[0])