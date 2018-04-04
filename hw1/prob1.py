import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import json
import requests

# def csv_to_dict(csvFile, data_dict):
# 	file = open(csvFile, "r")
# 	lines = file.readlines()
# 	for i in range(1, len(lines)):
		



def main():
	first = "2017-01-01"
	last = "2017-12-31"

	#Graffiti Removal
	# graf_time = open("graf_time.txt", "w+")
	# graf_zip = open("graf_zip.txt", "w+")
	# graf_resp = open("graf_resp.txt","w+")
	graf_time = open("graf_time.csv", "w+")
	graf_zip = open("graf_zip.csv", "w+")
	graf_resp = open("graf_resp.csv","w+")
	

	graffiti = pd.read_csv("~/Documents/graffiti.csv",dtype=object)
	graffiti["Creation Date"] = pd.to_datetime(graffiti["Creation Date"])
	graffiti["Completion Date"] = pd.to_datetime(graffiti["Completion Date"])

	#Get data only for 2017. Source: https://stackoverflow.com/questions/29370057/select-dataframe-rows-between-two-dates/41802199
	graf_2017 = (graffiti["Creation Date"]>=first)&(graffiti["Creation Date"]<=last)
	graffiti = graffiti.loc[graf_2017]

	# print>>graf_time, graffiti['Type of Service Request'].groupby([graffiti['Creation Date'].dt.month]).agg({'count'})
	# print>>graf_zip, graffiti['Type of Service Request'].groupby([graffiti['ZIP Code']]).agg({'count'})
	# graffiti['Response Time'] = (graffiti['Completion Date']-graffiti['Creation Date'])
	# print>>graf_resp, graffiti['Type of Service Request'].groupby([graffiti['Response Time']]).agg({'count'})
	(graffiti['Type of Service Request'].groupby([graffiti['Creation Date'].dt.month]).agg({'count'})).to_csv("graf_time.csv")
	(graffiti['Type of Service Request'].groupby([graffiti['ZIP Code']]).agg({'count'})).to_csv("graf_zip.csv")
	graffiti['Response Time'] = (graffiti['Completion Date']-graffiti['Creation Date'])
	(graffiti['Type of Service Request'].groupby([graffiti['Response Time']]).agg({'count'})).to_csv("grad_resp.csv")

	#Reset dataframe
	graffiti = pd.DataFrame(graffiti).reset_index()
	graffiti.to_csv("graffiti.csv")


	#Vacated and Abandomed Buildings
	# build_time = open("build_time.txt", "w+")
	# build_zip = open("build_zip.txt", "w+")
	build_time = open("build_time.csv", "w+")
	build_zip = open("build_zip.csv", "w+")


	buildings = pd.read_csv("~/Documents/buildings.csv",dtype = object)
	buildings["DATE SERVICE REQUEST WAS RECEIVED"]=pd.to_datetime(buildings["DATE SERVICE REQUEST WAS RECEIVED"])
	build_2017 = (buildings["DATE SERVICE REQUEST WAS RECEIVED"]>=first)&(buildings["DATE SERVICE REQUEST WAS RECEIVED"]<=last)
	buildings = buildings.loc[build_2017]

	# print>>build_time, buildings['SERVICE REQUEST TYPE'].groupby([buildings['DATE SERVICE REQUEST WAS RECEIVED'].dt.month]).agg({'count'})
	# print>>build_zip, buildings['SERVICE REQUEST TYPE'].groupby([buildings['ZIP CODE']]).agg({'count'})
	(buildings['SERVICE REQUEST TYPE'].groupby([buildings['DATE SERVICE REQUEST WAS RECEIVED'].dt.month]).agg({'count'})).to_csv("build_time.csv")
	(buildings['SERVICE REQUEST TYPE'].groupby([buildings['ZIP CODE']]).agg({'count'})).to_csv("build_zip.csv")

	#Reset dataframe
	buildings = pd.DataFrame(buildings).reset_index()
	buildings.to_csv("buildings.csv")


	#Lights Out in Alleys
	# alleys_time = open("alleys_time.txt", "w+")
	# alleys_zip = open("alleys_zip.txt", "w+")
	# alleys_resp = open("alleys_resp.txt","w+")
	alleys_time = open("alleys_time.csv", "w+")
	alleys_zip = open("alleys_zip.csv", "w+")
	alleys_resp = open("alleys_resp.csv","w+")

	alleys = pd.read_csv("~/Documents/alleys.csv", dtype = object)
	alleys["Creation Date"] = pd.to_datetime(alleys["Creation Date"])
	alleys["Completion Date"] = pd.to_datetime(alleys["Completion Date"])

	#Get data only for 2017. Source: https://stackoverflow.com/questions/29370057/select-dataframe-rows-between-two-dates/41802199
	alleys_2017 = (alleys["Creation Date"]>=first)&(alleys["Creation Date"]<=last)
	alleys = alleys.loc[alleys_2017]

	(alleys['Type of Service Request'].groupby([alleys['Creation Date'].dt.month]).agg({'count'})).to_csv("alleys_time.csv")
	(alleys['Type of Service Request'].groupby([alleys['ZIP Code']]).agg({'count'})).to_csv("alleys_zip.csv")
	alleys['Response Time'] = (alleys['Completion Date']-alleys['Creation Date'])
	(alleys['Type of Service Request'].groupby([alleys['Response Time']]).agg({'count'})).to_csv("alleys_resp.csv")

	#Read in data into dictionaries for plotting
	# graf_time_file = open("graf_time.csv", "r")
	# graf_time_dict = {}

	# for line in graf_time_file:
	# 	lineParts = line.split(",")
	# 	if len(lineParts)>1:
	# 		graf_time_dict[lineParts[0]]=graf_time_dict[lineParts[1]]
	# print(graf_time_dict)



if __name__ == '__main__':
	main()
