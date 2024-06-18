import sys
import csv

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

def gen_report():
    print("txt with results")

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
            sys.exit[1]
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