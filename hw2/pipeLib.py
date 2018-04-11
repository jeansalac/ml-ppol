import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy.stats import norm
from sklearn.preprocessing import StandardScaler
from scipy import stats
import warnings
warnings.filterwarnings('ignore')

#Read in CSV 
def readCSV(fileName):
	return pd.read_csv(fileName)

#Provide summary statistics from the given data frame and variable
def dataSummary(dataFrame, var):
	return dataFrame[var].describe()

#Provide variable distribution
def varDist(dataFrame,var):
	sns.distplot(dataFrame[var])
	return plt.show()

#Provide summary of correlations through heatmap
def corrSummary(dataFrame):
	corrmat = dataFrame.corr()
	f, ax = plt.subplots(figsize=(12, 9))
	sns.heatmap(corrmat, vmax=.8, square=True)
	return plt.show()

#Provide scatter plot b/w desired variables in list
def plotCorr(dataFrame, list):
	sns.set()
	sns.pairplot(dataFrame[list], size = 2.5)
	return plt.show()

#Find univariate outliers for var 
def findLowOutliers(dataFrame, var):
	df_scaled = StandardScaler().fit_transform(dataFrame[var][:,np.newaxis])
	low_range = df_scaled[df_scaled[:,0].argsort()][:10]
	return low_range

def findHighOutliers(dataFrame, var):
	df_scaled = StandardScaler().fit_transform(dataFrame[var][:,np.newaxis])
	high_range= df_scaled[df_scaled[:,0].argsort()][-10:]
	return high_range

#Find bivariate outliers for var X and var Y
def findBivariateOutliers(dataFrame,varX,varY):
	data = pd.concat([dataFrame[varX], dataFrame[varY]], axis=1)
	data.plot.scatter(x=varX, y=varY, ylim=(0,80000))
	return plt.show()

#Fill in missing values with var
def fillMissingVals(dataFrame, var):
	return dataFrame.fillna(var)

#Discretize continuous variables
def discretize(dataFrame, var, num):
	return pd.cut(dataFrame[var],num,retbins=True)

#Create dummy variables from categorical variables
def createDummy(dataFrame, var):
	return pd.get_dummies(dataFrame[var])