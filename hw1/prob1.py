import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import json
import requests


def main():
	graf_time = open("graf_time.txt", "w+")
	graf_zip = open("graf_zip.txt", "w+")
	graffiti = pd.read_csv("~/Documents/graffiti.csv",dtype=object)
	graffiti["Creation Date"] = pd.to_datetime(graffiti["Creation Date"])
	graffiti["Completion Date"] = pd.to_datetime(graffiti["Completion Date"])
	print>>graf_time, graffiti['Type of Service Request'].groupby([graffiti['Creation Date'].dt.year]).agg({'count'})
	print>>graf_zip, graffiti['Type of Service Request'].groupby([graffiti['ZIP Code']]).agg({'count'})
	graffiti['Response Time'] = (graffiti['Completion Date'] -graffiti['Creation Date'])
	graf_resp = graffiti['Response Time'].groupby([graffiti['Response Time'], graffiti['ZIP Code']]).agg({'count'})

	build_time = open("build_time.txt", "w+")
	build_zip = open("build_zip.txt", "w+")
	buildings = pd.read_csv("~/Documents/buildings.csv",dtype = object)
	buildings["DATE SERVICE REQUEST WAS RECEIVED"]=pd.to_datetime(buildings["DATE SERVICE REQUEST WAS RECEIVED"])
	print>>build_time, buildings['SERVICE REQUEST TYPE'].groupby([buildings['DATE SERVICE REQUEST WAS RECEIVED'].dt.year]).agg({'count'})
	print>>build_zip, buildings['SERVICE REQUEST TYPE'].groupby([buildings['ZIP CODE']]).agg({'count'})
	
	alleys_time = open("alleys_time.txt", "w+")
	alleys_zip = open("alleys_zip.txt", "w+")
	alleys = pd.read_csv("~/Documents/alleys.csv", dtype = object)
	alleys["Creation Date"] = pd.to_datetime(alleys["Creation Date"])
	print>>alleys_time, alleys['Type of Service Request'].groupby([alleys['Creation Date'].dt.year]).agg({'count'})
	print>>alleys_zip, alleys['Type of Service Request'].groupby([alleys['ZIP Code']]).agg({'count'})
	


if __name__ == '__main__':
	main()
