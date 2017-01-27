import numpy as np
import scipy as sp
from scipy import stats
import csv
import matplotlib.pyplot as plt

def readDataFile():
	closingPrices = []
	with open('../../Downloads/table.csv') as twitterStock:
		reader = csv.DictReader(twitterStock)
		for row in reader:
			closingPrices.append(float(row['Adj Close']))

	dataPoints = range(0, len(closingPrices))
	return (dataPoints, closingPrices)
	
def linearRegression():
	dataPoints, closingPrices = readDataFile()
	slope, intercept, r_value, p_value, std_err = stats.linregress(dataPoints, closingPrices)
	
	predictedDataPoints = []
	for x in dataPoints:
		predictedDataPoints.append(slope*x + intercept)

	plt.plot(dataPoints, closingPrices, 'r--', dataPoints, predictedDataPoints, 'bs')
	plt.show()

def polynomialFit(degree):
	dataPoints, closingPrices = readDataFile()
	p = np.polyfit(dataPoints, closingPrices, degree)
	predictedDataPoints = []
	for x in dataPoints: 
		predictedDataPoints.append(polyReg(x, p, degree))
	print(predictedDataPoints)
	plt.plot(dataPoints, closingPrices, 'r--', dataPoints, predictedDataPoints, 'bs')
	plt.show()

def polyReg(x, polyCoefficients, degree):
	accumulator = 0
	for arg in range(0, degree+1):
		accumulator += x**arg*polyCoefficients[degree-arg]
	return accumulator

polynomialFit(101)
