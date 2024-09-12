import sys
import numpy as np
from training import read_csv_file

np.seterr(over='raise', invalid='raise')


# SSE: Sum of square errors
# MSE: Mean of square errors
# RMSE: Square root of MSE
# SST: Sum of squares of total errors
# SAE: Sum of absolute errors
# MAE: Mean of absolute errors
def gen_report(data, theta0, theta1):
    try:
        length = len(data)
        SSE = sum((y - (theta0 + theta1 * x))**2 for x, y in data)
        MSE = SSE / length
        observed_mean = sum(y for _, y in data) / length
        SST = sum((y - observed_mean)**2 for _, y in data)
        determination_coef = 1 - (SSE/SST)
        SAE = sum(np.abs(y - (theta0 + theta1 * x)) for x, y in data)
        MAE = SAE / length
        print('MAE: ', MAE)
        print('RMSE: ', np.sqrt(MSE))
        print('R^2: ', determination_coef)
    except FloatingPointError as e:
        print(f"Error: {e}")
        print("Impossible to create repport")
        sys.exit(1)
    except OverflowError as e:
        print(f"Error: {e}")
        print("Impossible to create repport")
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python gen_report.py <data path>,\n"
              "<theta0 (bias)> (valid float),\n"
              "<theta1 (weight)> (valid float)\n")
        sys.exit(1)
    else:
        data = read_csv_file(sys.argv[1])
        if data is None:
            print(f"Error trying to read the path: {sys.argv[1]}")
            sys.exit(1)
        try:
            theta0 = float(sys.argv[2])
        except ValueError:
            print("Error with the bias (theta0)")
            sys.exit(1)
        try:
            theta1 = float(sys.argv[3])
        except ValueError:
            print("Error with the weight (theta1)")
            sys.exit(1)
    gen_report(data, theta0, theta1)
