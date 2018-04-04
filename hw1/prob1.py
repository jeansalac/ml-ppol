import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import json
import requests


def main():
	first = "2017-01-01"
	last = "2017-12-31"

	#Graffiti Removal
	graf_time = open("graf_time.txt", "w+")
	graf_zip = open("graf_zip.txt", "w+")
	graf_resp = open("graf_resp.txt","w+")
	

	graffiti = pd.read_csv("~/Documents/graffiti.csv",dtype=object)
	graffiti["Creation Date"] = pd.to_datetime(graffiti["Creation Date"])
	graffiti["Completion Date"] = pd.to_datetime(graffiti["Completion Date"])

	#Get data only for 2017. Source: https://stackoverflow.com/questions/29370057/select-dataframe-rows-between-two-dates/41802199
	graf_2017 = (graffiti["Creation Date"]>=first)&(graffiti["Creation Date"]<=last)
	graffiti = graffiti.loc[graf_2017]

	print>>graf_time, graffiti['Type of Service Request'].groupby([graffiti['Creation Date'].dt.month]).agg({'count'})
	print>>graf_zip, graffiti['Type of Service Request'].groupby([graffiti['ZIP Code']]).agg({'count'})
	graffiti['Response Time'] = (graffiti['Completion Date']-graffiti['Creation Date'])
	print>>graf_resp, graffiti['Type of Service Request'].groupby([graffiti['Response Time']]).agg({'count'})

	#Reset dataframe
	graffiti = pd.DataFrame(graffiti).reset_index()
	graffiti.to_csv("graffiti.csv")


	#Vacated and Abandomed Buildings
	build_time = open("build_time.txt", "w+")
	build_zip = open("build_zip.txt", "w+")

	buildings = pd.read_csv("~/Documents/buildings.csv",dtype = object)
	buildings["DATE SERVICE REQUEST WAS RECEIVED"]=pd.to_datetime(buildings["DATE SERVICE REQUEST WAS RECEIVED"])
	build_2017 = (buildings["DATE SERVICE REQUEST WAS RECEIVED"]>=first)&(buildings["DATE SERVICE REQUEST WAS RECEIVED"]<=last)
	buildings = buildings.loc[build_2017]

	print>>build_time, buildings['SERVICE REQUEST TYPE'].groupby([buildings['DATE SERVICE REQUEST WAS RECEIVED'].dt.month]).agg({'count'})
	print>>build_zip, buildings['SERVICE REQUEST TYPE'].groupby([buildings['ZIP CODE']]).agg({'count'})

	#Reset dataframe
	buildings = pd.DataFrame(buildings).reset_index()
	buildings.to_csv("buildings.csv")


	#Lights Out in Alleys
	alleys_time = open("alleys_time.txt", "w+")
	alleys_zip = open("alleys_zip.txt", "w+")
	alleys_resp = open("alleys_resp.txt","w+")

	alleys = pd.read_csv("~/Documents/alleys.csv", dtype = object)
	alleys["Creation Date"] = pd.to_datetime(alleys["Creation Date"])
	alleys["Completion Date"] = pd.to_datetime(alleys["Completion Date"])

	#Get data only for 2017. Source: https://stackoverflow.com/questions/29370057/select-dataframe-rows-between-two-dates/41802199
	alleys_2017 = (alleys["Creation Date"]>=first)&(alleys["Creation Date"]<=last)
	alleys = alleys.loc[alleys_2017]

	print>>alleys_time, alleys['Type of Service Request'].groupby([alleys['Creation Date'].dt.month]).agg({'count'})
	print>>alleys_zip, alleys['Type of Service Request'].groupby([alleys['ZIP Code']]).agg({'count'})
	alleys['Response Time'] = (alleys['Completion Date']-alleys['Creation Date'])
	print>>alleys_resp, graffiti['Type of Service Request'].groupby([graffiti['Response Time']]).agg({'count'})


if __name__ == '__main__':
	main()
