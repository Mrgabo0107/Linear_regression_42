import sys
import json
import csv


def read_csv_file(file_path):
    data = []
    try:
        with open(file_path, mode='r') as file:
            csv_reader = csv.reader(file)
            next(csv_reader)
            for row in csv_reader:
                data.append(row)
    except FileNotFoundError:
        print(f"El archivo '{file_path}' no se encontró.")
        return None
    return data


def new_theta0(learning_rate, data, theta0, theta1):
    m = len(data)
    my_sum = 0
    for i in range(m):
        my_sum += theta0 + (data[i][0] * theta1) - data[i][1]
    return (learning_rate * (my_sum / m))


def new_theta1(learning_rate, data, theta0, theta1):
    m = len(data)
    my_sum = 0
    for i in range(m):
        my_sum += (theta0 + (data[i][0] * theta1) - data[i][1]) * data[i][0]
    return (learning_rate * (my_sum) / m)


def train(lerning_rate, iterations, see_graph, see_line, see_report):
    file_path = 'data.csv'
    data = read_csv_file(file_path)
    # The method is started with theta0 and theta1 set to 0
    # because the project requires it.
    # Normally, we can choose the starting point of the method,
    # such as the number of iterations or the learning rate.
    theta0 = 0.0
    theta1 = 0.0
    for _ in range(iterations):
        theta0 = new_theta0(lerning_rate, data, theta0, theta1)
        theta1 = new_theta1(lerning_rate, data, theta0, theta1)
    dic = {"theta0": theta0, "theta1": theta1}
    filename = "parameters.json"
    try:
        with open(filename, 'w') as json_file:
            json.dump(dic, json_file)
        print(f"Archivo {filename} creado exitosamente.")
    except Exception as e:
        print(f"Ocurrió un error al crear el archivo {filename}: {e}")


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
