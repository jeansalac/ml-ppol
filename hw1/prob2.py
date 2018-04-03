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
	pop15 = {}
	pop16 = {}
	deg15 = {}
	deg16 = {}
	pov15 = {}
	pov16 = {}
	#http://chicago-zone.blogspot.com/2014/03/chicago-zip-code-map-locate-chicago.html
	far_north = []
	northwest = []
	north = []
	west =[]
	central = []
	south = []
	southwest =[]
	far_south = []
	far_SW = []
	far_SE = []

	for i in range(1, len(data_15)):
		#Check if it's in Chicago
		zipCode = int(data_15[i][4])
		if 60600 < zipCode and zipCode < 60720:
			pop15[zipCode] = int(data_15[i][1])
			deg15[zipCode] = int(data_15[i][2])
			pov15[zipCode] = int(data_15[i][3])

	pop15_sort = sorted(pop15.items()) # sorted by key, return a list of tuples
	x, y = zip(*pop15_sort) # unpack a list of pairs into two tuples
	plt.bar(x,y)
	plt.show()

	for i in range(1, len(data_16)):
		#Check if it's in Chicago
		zipCode = int(data_16[i][4])
		if 60600 < zipCode and zipCode < 60720:
			pop16[zipCode] = int(data_16[i][1])
			deg16[zipCode] = int(data_16[i][2])
			pov16[zipCode] = int(data_16[i][3])






if __name__ == '__main__':
	main()