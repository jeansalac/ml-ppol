from pipeLib import * 
import sys
import seaborn as sns

def main():
	credit_df = readCSV(sys.argv[1])
	print(dataSummary(credit_df, 'age'))
	varDist(credit_df, 'age')
	corrSummary(credit_df)
	varList = ["SeriousDlqin2yrs","RevolvingUtilizationOfUnsecuredLines","age","zipcode"]
	plotCorr(credit_df,varList)


if __name__ == '__main__':
	main()