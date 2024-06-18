import sys
import json
import csv
import matplotlib.pyplot as plt
import numpy as np
import subprocess


def plot_data_and_regression_line(data, m=None, b=None, show_line=False):
    x = np.array([row[0] for row in data])
    y = np.array([row[1] for row in data])
    plt.scatter(x, y, color='blue', label="Data", s=5)
    if show_line and m is not None and b is not None:
        plt.plot(x, m * x + b, color='red', linewidth=1,
                 label='Regression line')
    plt.xlabel('Mileage')
    plt.ylabel('Price')
    plt.legend()
    plt.savefig('data_and_regression.png')
    plt.clf() 

def read_csv_file(file_path):
    data = []
    try:
        with open(file_path, mode='r') as file:
            csv_reader = csv.reader(file)
            next(csv_reader)
            for row in csv_reader:
                data.append([float(row[0]), float(row[1])])
    except FileNotFoundError:
        print(f"File '{file_path}' not found")
        return None
    return data


def update_thetas(learning_rate, data, theta0, theta1):
    m = len(data)
    sum_errors0 = sum(theta0 + theta1 * x - y for x, y in data)
    sum_errors1 = sum((theta0 + theta1 * x - y) * x for x, y in data)
    theta0 -= learning_rate * sum_errors0 / m
    theta1 -= learning_rate * sum_errors1 / m
    return theta0, theta1


def normalize_data(data):
    mileage_column = np.array([row[0] for row in data])
    price_column = np.array([row[1] for row in data])
    minx = np.min(mileage_column)
    maxx = np.max(mileage_column)
    miny = np.min(price_column)
    maxy = np.max(price_column)
    normalized_data = []
    for row in data:
        normalized_data.append([(row[0] - minx) / (maxx - minx),
                                (row[1] - miny) / (maxy - miny)])
    return normalized_data, minx, maxx, miny, maxy


def rescale(theta0, theta1, minx, maxx, miny, maxy):
    theta1 = theta1 * (maxy - miny) / (maxx - minx)
    theta0 = (theta0 * (maxy - miny)) + miny - theta1 * minx
    return theta0, theta1


def train(lerning_rate, iterations, see_graph, see_line, see_report):
    file_path = 'data.csv'
    data = read_csv_file(file_path)
    if data is None:
        return
    normalized_data, minx, maxx, miny, maxy = normalize_data(data)
    # The method is started with theta0 and theta1 set to 0
    # because the project requires it.
    # Normally, we can choose the starting point of the method,
    # such as the number of iterations or the learning rate.
    theta0, theta1 = 0.0, 0.0
    for _ in range(iterations):
        theta0, theta1 = update_thetas(lerning_rate, normalized_data,
                                       theta0, theta1)
    theta0, theta1 = rescale(theta0, theta1, minx, maxx, miny, maxy)
    dic = {"theta0": theta0, "theta1": theta1}
    filename = "parameters.json"
    try:
        with open(filename, 'w') as json_file:
            json.dump(dic, json_file)
        print(f"File {filename} created succesfully.")
    except Exception as e:
        print(f"Error creating file {filename}: {e}")
    if see_graph:
        plot_data_and_regression_line(data, theta1, theta0, see_line)
    if see_report:
        subprocess.run(['python', 'gen_report.py', file_path, str(theta0), str(theta1)])


def set_good_boolean(str):
    s = str.lower()
    if s == 'true':
        return True
    elif s == 'false':
        return False
    else:
        raise ValueError


if __name__ == "__main__":
    if len(sys.argv) != 6:
        print("Usage: python training.py <lerning rate>(positive float), \n"
              "<interations> (positive integer), \n"
              "<see graph of points> (True or Flase), \n"
              "<see line in the graph of points> (True or False, \n"
              "will be set to False if <see graph of points is False>), \n"
              "<see algorithm accurancy repport> (True or False)\n")
        sys.exit(1)
    else:
        try:
            lerning_rate = float(sys.argv[1])
        except ValueError:
            print("Error with the learning rate")
            sys.exit(1)
        try:
            iterations = int(sys.argv[2])
        except ValueError:
            print("Error with the number of iterations")
            sys.exit(1)
        try:
            see_graph = set_good_boolean(sys.argv[3])
        except ValueError:
            print("Error with \"see graph\" boolean")
            sys.exit(1)
        try:
            see_line = set_good_boolean(sys.argv[4])
            if see_graph is False:
                see_line = False
        except ValueError:
            print("Error with \"see line\" boolean")
            sys.exit(1)
        try:
            see_report = set_good_boolean(sys.argv[5])
        except ValueError:
            print("Error with \"see accuracy repport\" boolean")
            sys.exit(1)
    train(lerning_rate, iterations, see_graph, see_line, see_report)
