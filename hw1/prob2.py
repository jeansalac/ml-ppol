import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import json
import requests


def main():
	# url_prefix = "https://api.census.gov/data/"
	# #Pull total population, Bachelor's degree, population in poverty
	# url_suffix = "/acs/acs5/subject?get=NAME,S0101_C01_001E,S1501_C01_012E,S0601_C01_048E&for=zip%20code%20tabulation%20area:*" 

	# for i in range(2015, 2017):
	# 	url = url_prefix+str(i)+url_suffix
	# 	#print(url)
	# 	json_stream = requests.get(url, allow_redirects=True)
	# 	json_filename = str(i)+"_data.json"
	# 	open(json_filename, 'wb').write(json_stream.content)

	json_data= open("2015_data.json", "r")
	data_15 = json.load(json_data)
	json_data.close()

	json_data= open("2016_data.json", "r")
	data_16 = json.load(json_data)
	json_data.close()
	
	#Iterate over data sets to populate dictionaries of zipcodes and variable
	pop15 = {"Far North":0,"Northwest":0,"North":0,"West":0,"Central":0,"South":0,"Southwest":0,"Far Southwest":0,"Far Southeast":0}
	pop16 = {"Far North":0,"Northwest":0,"North":0,"West":0,"Central":0,"South":0,"Southwest":0,"Far Southwest":0,"Far Southeast":0}
	deg15 = {"Far North":0,"Northwest":0,"North":0,"West":0,"Central":0,"South":0,"Southwest":0,"Far Southwest":0,"Far Southeast":0}
	deg16 = {"Far North":0,"Northwest":0,"North":0,"West":0,"Central":0,"South":0,"Southwest":0,"Far Southwest":0,"Far Southeast":0}
	pov15 = {"Far North":0,"Northwest":0,"North":0,"West":0,"Central":0,"South":0,"Southwest":0,"Far Southwest":0,"Far Southeast":0}
	pov16 = {"Far North":0,"Northwest":0,"North":0,"West":0,"Central":0,"South":0,"Southwest":0,"Far Southwest":0,"Far Southeast":0}
	#http://chicago-zone.blogspot.com/2014/03/chicago-zip-code-map-locate-chicago.html
	far_north = [60626,60645, 60659, 60660,60640,60625,60630,60631,60656]
	northwest = [60618,60634, 60641,60607,60639]
	north = [60618, 60613,60657, 60613,60614, 60610,60647]
	west =[60651, 60622,60612, 60623, 60642,60639, 60644,60624,60612,60607,60608,60616]
	central = [60610,60601, 60602, 60603, 60604, 60605,60606, 60607, 60661,60616]
	south = [60609,60616,60653,60615,60637,60649,60608,60620,60619]
	southwest =[60632,60608, 60609,60629,60638,60621,60636]
	far_SW = [60652,60620,60643,60655]
	far_SE = [60619,60617,60628,60643,60633,60827,60633,60638]

	#Populate data for 2015
	for i in range(1, len(data_15)):
		#Check if it's in Chicago
		zipCode = int(data_15[i][4])
		if zipCode in far_north:
			pop15["Far North"] = pop15["Far North"]+int(data_15[i][1])
			deg15["Far North"] = deg15["Far North"]+int(data_15[i][2])
			pov15["Far North"] = pov15["Far North"]+int(data_15[i][3])
		
		if zipCode in northwest:
			pop15["Northwest"] = pop15["Northwest"]+int(data_15[i][1])
			deg15["Northwest"] = deg15["Northwest"]+int(data_15[i][2])
			pov15["Northwest"] = pov15["Northwest"]+int(data_15[i][3])
		
		if zipCode in north:
			pop15["North"] = pop15["North"]+int(data_15[i][1])
			deg15["North"] = deg15["North"]+int(data_15[i][2])
			pov15["North"] = pov15["North"]+int(data_15[i][3])
		
		if zipCode in west:
			pop15["West"] = pop15["West"]+int(data_15[i][1])
			deg15["West"] = deg15["West"]+int(data_15[i][2])
			pov15["West"] = pov15["West"]+int(data_15[i][3])
		
		if zipCode in central:
			pop15["Central"] = pop15["Central"]+int(data_15[i][1])
			deg15["Central"] = deg15["Central"]+int(data_15[i][2])
			pov15["Central"] = pov15["Central"]+int(data_15[i][3])
		
		if zipCode in south:
			pop15["South"] = pop15["South"]+int(data_15[i][1])
			deg15["South"] = deg15["South"]+int(data_15[i][2])
			pov15["South"] = pov15["South"]+int(data_15[i][3])

		if zipCode in southwest:
			pop15["Southwest"] = pop15["Southwest"]+int(data_15[i][1])
			deg15["Southwest"] = deg15["Southwest"]+int(data_15[i][2])
			pov15["Southwest"] = pov15["Southwest"]+int(data_15[i][3])

		if zipCode in far_SW:
			pop15["Far Southwest"] = pop15["Far Southwest"]+int(data_15[i][1])
			deg15["Far Southwest"] = deg15["Far Southwest"]+int(data_15[i][2])
			pov15["Far Southwest"] = pov15["Far Southwest"]+int(data_15[i][3])

		if zipCode in far_SE:
			pop15["Far Southeast"] = pop15["Far Southeast"]+int(data_15[i][1])
			deg15["Far Southeast"] = deg15["Far Southeast"]+int(data_15[i][2])
			pov15["Far Southeast"] = pov15["Far Southeast"]+int(data_15[i][3])

	# print(pop15)
	# print(deg15)
	# print(pov15)
	# plt.bar(pop15.keys(),pop15.values())
	# plt.show()

		#Populate data for 2016
	for i in range(1, len(data_16)):
		#Check if it's in Chicago
		zipCode = int(data_16[i][4])
		if zipCode in far_north:
			pop16["Far North"] = pop16["Far North"]+int(data_16[i][1])
			deg16["Far North"] = deg16["Far North"]+int(data_16[i][2])
			pov16["Far North"] = pov16["Far North"]+int(data_16[i][3])
		
		if zipCode in northwest:
			pop16["Northwest"] = pop16["Northwest"]+int(data_16[i][1])
			deg16["Northwest"] = deg16["Northwest"]+int(data_16[i][2])
			pov16["Northwest"] = pov16["Northwest"]+int(data_16[i][3])
		
		if zipCode in north:
			pop16["North"] = pop16["North"]+int(data_16[i][1])
			deg16["North"] = deg16["North"]+int(data_16[i][2])
			pov16["North"] = pov16["North"]+int(data_16[i][3])
		
		if zipCode in west:
			pop16["West"] = pop16["West"]+int(data_16[i][1])
			deg16["West"] = deg16["West"]+int(data_16[i][2])
			pov16["West"] = pov16["West"]+int(data_16[i][3])
		
		if zipCode in central:
			pop16["Central"] = pop16["Central"]+int(data_16[i][1])
			deg16["Central"] = deg16["Central"]+int(data_16[i][2])
			pov16["Central"] = pov16["Central"]+int(data_16[i][3])
		
		if zipCode in south:
			pop16["South"] = pop16["South"]+int(data_16[i][1])
			deg16["South"] = deg16["South"]+int(data_16[i][2])
			pov16["South"] = pov16["South"]+int(data_16[i][3])

		if zipCode in southwest:
			pop16["Southwest"] = pop16["Southwest"]+int(data_16[i][1])
			deg16["Southwest"] = deg16["Southwest"]+int(data_16[i][2])
			pov16["Southwest"] = pov16["Southwest"]+int(data_16[i][3])

		if zipCode in far_SW:
			pop16["Far Southwest"] = pop16["Far Southwest"]+int(data_16[i][1])
			deg16["Far Southwest"] = deg16["Far Southwest"]+int(data_16[i][2])
			pov16["Far Southwest"] = pov16["Far Southwest"]+int(data_16[i][3])

		if zipCode in far_SE:
			pop16["Far Southeast"] = pop16["Far Southeast"]+int(data_16[i][1])
			deg16["Far Southeast"] = deg16["Far Southeast"]+int(data_16[i][2])
			pov16["Far Southeast"] = pov16["Far Southeast"]+int(data_16[i][3])
	
	# print(pop16)
	# print(deg16)
	# print(pov16)

	first15 = "2015-01-01"
	last15 = "2015-12-31"
	first16 = "2016-01-01"
	last16 = "2016-12-31"

	#Vacated and Abandomed Buildings for 2015
	build_zip15 = open("build_zip15.csv", "w+")

	buildings = pd.read_csv("~/Documents/buildings.csv",dtype = object)
	buildings["DATE SERVICE REQUEST WAS RECEIVED"]=pd.to_datetime(buildings["DATE SERVICE REQUEST WAS RECEIVED"])
	build_2015 = (buildings["DATE SERVICE REQUEST WAS RECEIVED"]>=first15)&(buildings["DATE SERVICE REQUEST WAS RECEIVED"]<=last15)
	buildings = buildings.loc[build_2015]

	(buildings['SERVICE REQUEST TYPE'].groupby([buildings['ZIP CODE']]).agg({'count'})).to_csv("build_zip15.csv")

	#Reset dataframe
	buildings = pd.DataFrame(buildings).reset_index()
	buildings.to_csv("buildings.csv")

	#Vacated and Abandomed Buildings for 2016
	build_zip16 = open("build_zip16.csv", "w+")

	buildings = pd.read_csv("~/Documents/buildings.csv",dtype = object)
	buildings["DATE SERVICE REQUEST WAS RECEIVED"]=pd.to_datetime(buildings["DATE SERVICE REQUEST WAS RECEIVED"])
	build_2016 = (buildings["DATE SERVICE REQUEST WAS RECEIVED"]>=first15)&(buildings["DATE SERVICE REQUEST WAS RECEIVED"]<=last16)
	buildings = buildings.loc[build_2016]

	(buildings['SERVICE REQUEST TYPE'].groupby([buildings['ZIP CODE']]).agg({'count'})).to_csv("build_zip16.csv")

	#Reset dataframe
	buildings = pd.DataFrame(buildings).reset_index()
	buildings.to_csv("buildings.csv")

	#Lights Out in Alleys for 2015
	alleys_zip15 = open("alleys_zip15.csv", "w+")

	alleys = pd.read_csv("~/Documents/alleys.csv", dtype = object)
	alleys["Creation Date"] = pd.to_datetime(alleys["Creation Date"])
	alleys_2015 = (alleys["Creation Date"]>=first15)&(alleys["Creation Date"]<=last15)
	alleys = alleys.loc[alleys_2015]

	(alleys['Type of Service Request'].groupby([alleys['ZIP Code']]).agg({'count'})).to_csv("alley_zip15.csv")

	#Lights Out in Alleys for 2016
	alleys_zip16 = open("alleys_zip16.csv", "w+")

	alleys = pd.read_csv("~/Documents/alleys.csv", dtype = object)
	alleys["Creation Date"] = pd.to_datetime(alleys["Creation Date"])
	alleys_2016 = (alleys["Creation Date"]>=first16)&(alleys["Creation Date"]<=last16)
	alleys = alleys.loc[alleys_2016]

	(alleys['Type of Service Request'].groupby([alleys['ZIP Code']]).agg({'count'})).to_csv("alley_zip16.csv")






if __name__ == '__main__':
	main()