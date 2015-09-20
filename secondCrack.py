import sys, getopt
import numpy as np
import scipy as sp
from scipy import stats
import csv
import matplotlib.pyplot as plt

def readDataFile(dataCSVFile):
    closingPrices = []
    with open(dataCSVFile) as stockData:
        reader = csv.DictReader(stockData)
        for row in reader:
            closingPrices.append(float(row['Adj Close']))

    dataPoints = range(0, len(closingPrices))
    return (dataPoints, closingPrices)
	
def linearRegression(dataCSVFile, extrapolate):
    dataPoints, closingPrices = readDataFile(dataCSVFile)
    slope, intercept, r_value, p_value, std_err = stats.linregress(dataPoints, closingPrices)
	
    predictedDataPoints = []
    for x in dataPoints:
        predictedDataPoints.append(slope*x + intercept)
        
    for x in range(dataPoints[-1] + 1, dataPoints[-1] + extrapolate + 1):
        predictedDataPoints.append(slope*x + intercept)

    plt.plot(dataPoints, closingPrices, 'r--',
             range(0, len(predictedDataPoints)),
             predictedDataPoints, 'bs')
    plt.show()

def polynomialFit(dataCSVFile, degree):
    dataPoints, closingPrices = readDataFile(dataCSVFile)
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

def main(argv):
    
    print("Starting program...")
    dataCSVFile = 'table.csv'
    degree = 1
    extrapolate = 0
    try:
        opts, args = getopt.getopt(argv, "ideh", ["ifile=", "degree=",
                                                  "extrapolate=" "help"])
    except getopt.GetoptError:
        print("firstCrack.py -i <CSV file> -d <Poly deg> -t <# time units to exrapolate>")
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print("firstCrack.py -i <CSV file> -d <Poly deg> -t <# time units to exrapolate>")
            sys.exit()
        elif opt in ("-i", "--ifile"):
            dataCSVFile = arg
        elif opt in ("-d", "--degree"):
            try:
                degree = int(arg)
            except ValueError:
                print("Could not convert degree to integer")
                sys.exit(2)
            if degree < 1:
                print("Error: polynomial degree must be a positive integer")
                sys.exit(2)
        elif opt in ("-e", "--extrapolate"):
            try:
                extrapolate = max(int(arg), 0)
            except:
                print("Error: Improper extrapolate argument")
                sys.exit(2)

    print("Using CSV file: " + dataCSVFile)
    try:
        fHandle = open(dataCSVFile)
        fHandle.close()
    except IOError as e:
        print("I/O error({0}): {1}".format(e.errno, e.strerror))
        sys.exit(2)
    except:
        print("Unexpected error:", sys.exc_info()[0])
        sys.exit(2)

    if degree == 1:
        print("Running linear regression")
        linearRegression(dataCSVFile, extrapolate)
    else:
        print("Running polynomial least squares fit with degree " + str(degree))
        polynomialFit(dataCSVFile, degree)

    fHandle.close()

    sys.exit(0)

if __name__ is "__main__":
    main(sys.argv[1:])
        
