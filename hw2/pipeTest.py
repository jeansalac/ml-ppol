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
	fillMissingVals(credit_df, credit_df.median())


if __name__ == '__main__':
	main()