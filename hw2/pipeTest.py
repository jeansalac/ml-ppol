from pipeLib import * 
import sys
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy.stats import norm
from sklearn.preprocessing import StandardScaler
from scipy import stats
import warnings
warnings.filterwarnings('ignore')
import statsmodels.api as sm
from patsy import dmatrices
from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import train_test_split
from sklearn import metrics
from sklearn.cross_validation import cross_val_score

def main():
	#Read in the csv from command line
	credit_df = readCSV(sys.argv[1])

	#Data Summary
	print(dataSummary(credit_df, 'age'))

	#Give the distribution of the age variable
	varDist(credit_df, 'age')

	#Create a heatmap for the correlations among variables in credit_df
	corrSummary(credit_df)

	#Plot correlations between the variables in varList
	varList = ["RevolvingUtilizationOfUnsecuredLines","NumberOfOpenCreditLinesAndLoans","NumberRealEstateLoansOrLines"]
	plotCorr(credit_df,varList)

	#Finding outliers
	print(findLowOutliers(credit_df, "SeriousDlqin2yrs"))
	print(findHighOutliers(credit_df, "SeriousDlqin2yrs"))
	findBivariateOutliers(credit_df, "age", "NumberOfDependents", 10)

	#Fill in Continuous Variables
	contVars = ['RevolvingUtilizationOfUnsecuredLines','age','NumberOfTime30-59DaysPastDueNotWorse',
	'DebtRatio','MonthlyIncome','NumberOfOpenCreditLinesAndLoans','NumberOfTimes90DaysLate',
	'NumberRealEstateLoansOrLines','NumberOfTime60-89DaysPastDueNotWorse','NumberOfDependents']
	for var in contVars:
		fillMissing(credit_df, var, credit_df[var].median())

	#Fill in Categorical variables
	catVars = ['zipcode']
	for var in catVars:
		fillMissing(credit_df, var, 0)

	#Discretize age
	print(discretize(credit_df, 'age', 5))

	#Create Dummy variables for zipcode
	print(createDummy(credit_df, 'zipcode'))

	#Classifier: Logistic Regression
	DVs = ['RevolvingUtilizationOfUnsecuredLines','age','zipcode','NumberOfTime30-59DaysPastDueNotWorse',
	'DebtRatio','MonthlyIncome','NumberOfOpenCreditLinesAndLoans','NumberOfTimes90DaysLate',
	'NumberRealEstateLoansOrLines','NumberOfTime60-89DaysPastDueNotWorse','NumberOfDependents']
	print(logReg(credit_df, "SeriousDlqin2yrs", DVs))


if __name__ == '__main__':
	main()