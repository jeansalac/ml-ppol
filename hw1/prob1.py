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
	# first = "2017-01-01"
	# last = "2017-12-31"

	# #Graffiti Removal
	# # graf_time = open("graf_time.txt", "w+")
	# # graf_zip = open("graf_zip.txt", "w+")
	# # graf_resp = open("graf_resp.txt","w+")
	# graf_time = open("graf_time.csv", "w+")
	# graf_zip = open("graf_zip.csv", "w+")
	# graf_resp = open("graf_resp.csv","w+")
	

	# graffiti = pd.read_csv("~/Documents/graffiti.csv",dtype=object)
	# graffiti["Creation Date"] = pd.to_datetime(graffiti["Creation Date"])
	# graffiti["Completion Date"] = pd.to_datetime(graffiti["Completion Date"])

	# #Get data only for 2017. Source: https://stackoverflow.com/questions/29370057/select-dataframe-rows-between-two-dates/41802199
	# graf_2017 = (graffiti["Creation Date"]>=first)&(graffiti["Creation Date"]<=last)
	# graffiti = graffiti.loc[graf_2017]

	# # print>>graf_time, graffiti['Type of Service Request'].groupby([graffiti['Creation Date'].dt.month]).agg({'count'})
	# # print>>graf_zip, graffiti['Type of Service Request'].groupby([graffiti['ZIP Code']]).agg({'count'})
	# # graffiti['Response Time'] = (graffiti['Completion Date']-graffiti['Creation Date'])
	# # print>>graf_resp, graffiti['Type of Service Request'].groupby([graffiti['Response Time']]).agg({'count'})
	# (graffiti['Type of Service Request'].groupby([graffiti['Creation Date'].dt.month]).agg({'count'})).to_csv("graf_time.csv")
	# (graffiti['Type of Service Request'].groupby([graffiti['ZIP Code']]).agg({'count'})).to_csv("graf_zip.csv")
	# graffiti['Response Time'] = (graffiti['Completion Date']-graffiti['Creation Date'])
	# (graffiti['Type of Service Request'].groupby([graffiti['Response Time']]).agg({'count'})).to_csv("grad_resp.csv")

	# #Reset dataframe
	# graffiti = pd.DataFrame(graffiti).reset_index()
	# graffiti.to_csv("graffiti.csv")


	# #Vacated and Abandomed Buildings
	# # build_time = open("build_time.txt", "w+")
	# # build_zip = open("build_zip.txt", "w+")
	# build_time = open("build_time.csv", "w+")
	# build_zip = open("build_zip.csv", "w+")


	# buildings = pd.read_csv("~/Documents/buildings.csv",dtype = object)
	# buildings["DATE SERVICE REQUEST WAS RECEIVED"]=pd.to_datetime(buildings["DATE SERVICE REQUEST WAS RECEIVED"])
	# build_2017 = (buildings["DATE SERVICE REQUEST WAS RECEIVED"]>=first)&(buildings["DATE SERVICE REQUEST WAS RECEIVED"]<=last)
	# buildings = buildings.loc[build_2017]

	# # print>>build_time, buildings['SERVICE REQUEST TYPE'].groupby([buildings['DATE SERVICE REQUEST WAS RECEIVED'].dt.month]).agg({'count'})
	# # print>>build_zip, buildings['SERVICE REQUEST TYPE'].groupby([buildings['ZIP CODE']]).agg({'count'})
	# (buildings['SERVICE REQUEST TYPE'].groupby([buildings['DATE SERVICE REQUEST WAS RECEIVED'].dt.month]).agg({'count'})).to_csv("build_time.csv")
	# (buildings['SERVICE REQUEST TYPE'].groupby([buildings['ZIP CODE']]).agg({'count'})).to_csv("build_zip.csv")

	# #Reset dataframe
	# buildings = pd.DataFrame(buildings).reset_index()
	# buildings.to_csv("buildings.csv")


	# #Lights Out in Alleys
	# # alleys_time = open("alleys_time.txt", "w+")
	# # alleys_zip = open("alleys_zip.txt", "w+")
	# # alleys_resp = open("alleys_resp.txt","w+")
	# alleys_time = open("alleys_time.csv", "w+")
	# alleys_zip = open("alleys_zip.csv", "w+")
	# alleys_resp = open("alleys_resp.csv","w+")

	# alleys = pd.read_csv("~/Documents/alleys.csv", dtype = object)
	# alleys["Creation Date"] = pd.to_datetime(alleys["Creation Date"])
	# alleys["Completion Date"] = pd.to_datetime(alleys["Completion Date"])

	# #Get data only for 2017. Source: https://stackoverflow.com/questions/29370057/select-dataframe-rows-between-two-dates/41802199
	# alleys_2017 = (alleys["Creation Date"]>=first)&(alleys["Creation Date"]<=last)
	# alleys = alleys.loc[alleys_2017]

	# (alleys['Type of Service Request'].groupby([alleys['Creation Date'].dt.month]).agg({'count'})).to_csv("alleys_time.csv")
	# (alleys['Type of Service Request'].groupby([alleys['ZIP Code']]).agg({'count'})).to_csv("alleys_zip.csv")
	# alleys['Response Time'] = (alleys['Completion Date']-alleys['Creation Date'])
	# (alleys['Type of Service Request'].groupby([alleys['Response Time']]).agg({'count'})).to_csv("alleys_resp.csv")

	#Read in data into dictionaries for plotting
	#Requests over Time
	graf_time_file = open("graf_time.csv", "r")
	graf_time_dict = {}

	graf_time_lines = graf_time_file.readlines()
	for x in range(1, len(graf_time_lines)):
		lineParts = graf_time_lines[x].split(",")
		graf_time_dict[int(lineParts[0])] = int(lineParts[1].strip())
	
	lists = sorted(graf_time_dict.items())
	x, y = zip(*lists) # unpack a list of pairs into two tuples
	plt.plot(x,y)
	plt.xlabel("Months of 2017")
	plt.ylabel("Number of Graffiti Removal Requests")
	plt.show()

	build_time_file = open("build_time.csv", "r")
	build_time_dict = {}

	build_time_lines = build_time_file.readlines()
	for x in range(1, len(build_time_lines)):
		lineParts = build_time_lines[x].split(",")
		build_time_dict[int(lineParts[0])] = int(lineParts[1].strip())
	
	lists = sorted(build_time_dict.items())
	x, y = zip(*lists) # unpack a list of pairs into two tuples
	plt.plot(x,y)
	plt.xlabel("Months of 2017")
	plt.ylabel("Number of Vacant and Abandoned Buildings Reported")
	plt.show()

	alleys_time_file = open("alleys_time.csv", "r")
	alleys_time_dict = {}

	alleys_time_lines = alleys_time_file.readlines()
	for x in range(1, len(alleys_time_lines)):
		lineParts = alleys_time_lines[x].split(",")
		alleys_time_dict[int(lineParts[0])] = int(lineParts[1].strip())
	
	lists = sorted(alleys_time_dict.items())
	x, y = zip(*lists) # unpack a list of pairs into two tuples
	plt.plot(x,y)
	plt.xlabel("Months of 2017")
	plt.ylabel("Number of Alley Lights Out Reported")
	plt.show()

	#Requests per neighborhood
	graf_zip_file = open("graf_zip.csv", "r")
	graf_zip_dict = {"Far North":0,"Northwest":0,"North":0,"West":0,"Central":0,"South":0,"Southwest":0,"Far Southwest":0,"Far Southeast":0}
	build_zip_file = open("build_zip.csv", "r")
	build_zip_dict = {"Far North":0,"Northwest":0,"North":0,"West":0,"Central":0,"South":0,"Southwest":0,"Far Southwest":0,"Far Southeast":0}
	alleys_zip_file = open("alleys_zip.csv", "r")
	alleys_zip_dict = {"Far North":0,"Northwest":0,"North":0,"West":0,"Central":0,"South":0,"Southwest":0,"Far Southwest":0,"Far Southeast":0}

	#From: http://chicago-zone.blogspot.com/2014/03/chicago-zip-code-map-locate-chicago.html
	far_north = [60626,60645, 60659, 60660,60640,60625,60630,60631,60656]
	northwest = [60618,60634, 60641,60607,60639]
	north = [60618, 60613,60657, 60613,60614, 60610,60647]
	west =[60651, 60622,60612, 60623, 60642,60639, 60644,60624,60612,60607,60608,60616]
	central = [60610,60601, 60602, 60603, 60604, 60605,60606, 60607, 60661,60616]
	south = [60609,60616,60653,60615,60637,60649,60608,60620,60619]
	southwest =[60632,60608, 60609,60629,60638,60621,60636]
	far_SW = [60652,60620,60643,60655]
	far_SE = [60619,60617,60628,60643,60633,60827,60633,60638]

	graf_zip_lines = graf_zip_file.readlines()
	for x in range(1, len(graf_zip_lines)):
		lineParts = graf_zip_lines[x].split(",")
		zipCode = int(lineParts[0])
		if zipCode in far_north:
			graf_zip_dict["Far North"] = graf_zip_dict["Far North"]+int(lineParts[1].strip())

		if zipCode in northwest:
			graf_zip_dict["Northwest"] = graf_zip_dict["Northwest"]+int(lineParts[1].strip())
		
		if zipCode in north:
			graf_zip_dict["North"] = graf_zip_dict["North"]+int(lineParts[1].strip())
		
		if zipCode in west:
			graf_zip_dict["West"] = graf_zip_dict["West"]+int(lineParts[1].strip())
		
		if zipCode in central:
			graf_zip_dict["Central"] = graf_zip_dict["Central"]+int(lineParts[1].strip())
		
		if zipCode in south:
			graf_zip_dict["South"] = graf_zip_dict["South"]+int(lineParts[1].strip())

		if zipCode in southwest:
			graf_zip_dict["Southwest"] = graf_zip_dict["Southwest"]+int(lineParts[1].strip())


		if zipCode in far_SW:
			graf_zip_dict["Far Southwest"] = graf_zip_dict["Far Southwest"]+int(lineParts[1].strip())

		if zipCode in far_SE:
			graf_zip_dict["Far Southeast"] = graf_zip_dict["Far Southeast"]+int(lineParts[1].strip())

	lists = sorted(graf_zip_dict.items())
	x, y = zip(*lists) # unpack a list of pairs into two tuples
	plt.bar(x,y)
	plt.xlabel("Community Areas")
	plt.ylabel("Number of Graffiti Removal Requests")
	plt.show()

	build_zip_lines = build_zip_file.readlines()
	for x in range(1, len(build_zip_lines)):
		lineParts = build_zip_lines[x].split(",")
		zipCode = int(lineParts[0])
		if zipCode in far_north:
			build_zip_dict["Far North"] = build_zip_dict["Far North"]+int(lineParts[1].strip())

		if zipCode in northwest:
			build_zip_dict["Northwest"] = build_zip_dict["Northwest"]+int(lineParts[1].strip())
		
		if zipCode in north:
			build_zip_dict["North"] = build_zip_dict["North"]+int(lineParts[1].strip())
		
		if zipCode in west:
			build_zip_dict["West"] = build_zip_dict["West"]+int(lineParts[1].strip())
		
		if zipCode in central:
			build_zip_dict["Central"] = build_zip_dict["Central"]+int(lineParts[1].strip())
		
		if zipCode in south:
			build_zip_dict["South"] = build_zip_dict["South"]+int(lineParts[1].strip())

		if zipCode in southwest:
			build_zip_dict["Southwest"] = build_zip_dict["Southwest"]+int(lineParts[1].strip())

		if zipCode in far_SW:
			build_zip_dict["Far Southwest"] = build_zip_dict["Far Southwest"]+int(lineParts[1].strip())

		if zipCode in far_SE:
			build_zip_dict["Far Southeast"] = build_zip_dict["Far Southeast"]+int(lineParts[1].strip())

	lists = sorted(build_zip_dict.items())
	x, y = zip(*lists) # unpack a list of pairs into two tuples
	plt.bar(x,y)
	plt.xlabel("Community Areas")
	plt.ylabel("Number of Vacant and Abandoned Buildings Reported")
	plt.show()

	alleys_zip_lines = alleys_zip_file.readlines()
	for x in range(1, len(alleys_zip_lines)):
		lineParts = alleys_zip_lines[x].split(",")
		zipCode = int(lineParts[0])
		if zipCode in far_north:
			alleys_zip_dict["Far North"] = alleys_zip_dict["Far North"]+int(lineParts[1].strip())

		if zipCode in northwest:
			alleys_zip_dict["Northwest"] = alleys_zip_dict["Northwest"]+int(lineParts[1].strip())
		
		if zipCode in north:
			alleys_zip_dict["North"] = alleys_zip_dict["North"]+int(lineParts[1].strip())
		
		if zipCode in west:
			alleys_zip_dict["West"] = alleys_zip_dict["West"]+int(lineParts[1].strip())
		
		if zipCode in central:
			alleys_zip_dict["Central"] = alleys_zip_dict["Central"]+int(lineParts[1].strip())
		
		if zipCode in south:
			alleys_zip_dict["South"] = alleys_zip_dict["South"]+int(lineParts[1].strip())

		if zipCode in southwest:
			alleys_zip_dict["Southwest"] = alleys_zip_dict["Southwest"]+int(lineParts[1].strip())

		if zipCode in far_SW:
			alleys_zip_dict["Far Southwest"] = alleys_zip_dict["Far Southwest"]+int(lineParts[1].strip())

		if zipCode in far_SE:
			alleys_zip_dict["Far Southeast"] = alleys_zip_dict["Far Southeast"]+int(lineParts[1].strip())

	lists = sorted(alleys_zip_dict.items())
	x, y = zip(*lists) # unpack a list of pairs into two tuples
	plt.bar(x,y)
	plt.xlabel("Community Areas")
	plt.ylabel("Number of Alley Lights Out Reported")
	plt.show()

	graf_resp_file = open("graf_resp.csv", "r")
	graf_resp_dict = {}

	graf_resp_lines = graf_resp_file.readlines()
	for x in range(1, len(graf_resp_lines)):
		lineParts = graf_resp_lines[x].split(",")
		respParts = lineParts[0].split()
		graf_resp_dict[int(respParts[0])] = int(lineParts[1].strip())
	
	lists = sorted(graf_resp_dict.items())
	x, y = zip(*lists) # unpack a list of pairs into two tuples
	plt.plot(x,y)
	plt.xlabel("Response Time (days)")
	plt.ylabel("Graffiti Removal Requests")
	plt.show()

	alleys_resp_file = open("alleys_resp.csv", "r")
	alleys_resp_dict = {}

	alleys_resp_lines = alleys_resp_file.readlines()
	for x in range(1, len(alleys_resp_lines)):
		lineParts = alleys_resp_lines[x].split(",")
		respParts = lineParts[0].split()
		alleys_resp_dict[int(respParts[0])] = int(lineParts[1].strip())
	
	lists = sorted(alleys_resp_dict.items())
	x, y = zip(*lists) # unpack a list of pairs into two tuples
	plt.plot(x,y)
	plt.xlabel("Response Time (days)")
	plt.ylabel("Number of Alley Lights Out Reported")
	plt.show()





if __name__ == '__main__':
	main()
