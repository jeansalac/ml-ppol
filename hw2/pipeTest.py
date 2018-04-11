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

def main():
	credit_df = readCSV(sys.argv[1])
	# print(dataSummary(credit_df, 'age'))
	# varDist(credit_df, 'age')
	# corrSummary(credit_df)
	# varList = ["SeriousDlqin2yrs","RevolvingUtilizationOfUnsecuredLines","age","zipcode"]
	# plotCorr(credit_df,varList)
	# print(findLowOutliers(credit_df, "SeriousDlqin2yrs"))
	# print(findHighOutliers(credit_df, "SeriousDlqin2yrs"))
	# findBivariateOutliers(credit_df, "age", "zipcode")
	#print(credit_df)
	#print(fillMissingVals(credit_df, credit_df.median()))
	#print(discretize(credit_df, 'age', 5))
	print(createDummy(credit_df, 'MonthlyIncome'))


if __name__ == '__main__':
	main()