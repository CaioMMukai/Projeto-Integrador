x# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 12:31:07 2020

@author: caio.mukai
"""
# =============================================================================
# Teste Api Google
# =============================================================================
import pandas as pd
import googlemaps
from utils.utils import *

estacao = read_csv("data/estacao.csv")
df=estacao

gmaps_key = googlemaps.Client(key = "")

# df["LAT"] = None
# df["LON"] = None

for i in range(0, len(df), 1):
    geocode_result = gmaps_key.geocode(df.iat[i, 0])
    #geocode_result = gmaps_key.geocode("Term. Jabaquara  São Paulo  Brazil")
    try:
        lat = geocode_result[0]["geometry"]["location"]["lat"]
        lon = geocode_result[0]["geometry"]["location"]["lng"]
        df.iat[i,df.columns.get_loc("LAT")]= lat
        df.iat[i,df.columns.get_loc("LON")]= lon
    except:
        lat = None
        lon = None
        
save_as_csv(df, 'data/Address_to_GPS.csv')

# =============================================================================
# Teste de adress to geolocation
# =============================================================================
        
from utils.utils import *
from geopy.geocoders import Nominatim 
import pandas as pd

df_aps=read_csv('aps.csv')

x=df_aps['Endereço'].unique()


nom = Nominatim()
for i in x :
    n=nom.geocode("R. Cel. Joaquim Ferreira Lôbo, 305 - Vila Nova Conceição")
    print(i,n.latitude, n.longitude)


# =============================================================================
# Teste Calculo de distancia 
# =============================================================================
from geopy import distance
from utils.utils import *
estacao = read_csv("data/estacao.csv")
#house = read_csv("data/Data_set.csv")

house = ([-23.5701325,-46.6573532],[-23.593657,-46.6846833],[-23.5973664,-46.6863424],[-23.5995101,-46.6766726],[-23.5302546,-46.6789501])
for i in range(0, 10):
    print (i)
    house = house[1]
    lat = (estacao['latitude'][3])
    lat = (-23.6244547)
    lon = (-46.6379525)
    lon = (estacao['longitude'][3])
    metro=(lat,lon)
    print(distance.distance(house, metro).km)

# house = (-23.5701325,-46.6573532)
# metro = (-23.6244547,-46.6379525)
#print(distance.distance(wellington, salamanca).km)
print(distance.distance(house, metro).km)



