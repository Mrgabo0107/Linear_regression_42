import os
import subprocess


def enter_mileage():
    while True:
        try:
            mileage = float(input("Please insert the mileage of"
                                  " your car (int or float value)\n"))
            return mileage
        except ValueError:
            pass


def train_options():
    options = [False, False, False]
    see_data_repartition = True
    while see_data_repartition:
        see_points = input("Do you want to see the repartition "
                           "of points in a graph? (y/n)\n")
        if see_points == "y":
            options[0] = True
            see_calculated_line = True
            while see_calculated_line:
                see_line = input("Do you want to see the line "
                                 "calculated in the regression? (y/n)\n")
                if see_line == "y":
                    options[1] = True
                    see_calculated_line = False
                elif see_line == "n":
                    see_calculated_line = False
                else:
                    pass
            see_data_repartition = False
        elif see_points == "n":
            see_data_repartition = False
        else:
            pass
    see_algorithm_report = True
    while see_algorithm_report:
        see_report = input("Do you want to see a report of the algorithm "
                           "accurancy? (y/n)\n")
        if see_report == "y":
            options[2] = True
            see_algorithm_report = False
        elif see_report == "n":
            see_algorithm_report = False
        else:
            pass
    return options


def train_model():
    train_or_not = True
    while train_or_not:
        train = input("Do you want to train the model? (y/n)\n")
        if train == "y":
            options = train_options()
            subprocess.run(['python', 'training.py'] + options,
                           capture_output=True,
                           text=True)
            train_or_not = False
        elif train == "n":
            train_or_not = False
        else:
            pass


def predict_price():
    print("Usage:\n\n"
          "You will be asked to enter a mileage; please enter a valid\n"
          " number (float).\n\n"
          "If the model has not been trained, it will default to the line\n"
          "'price = 0 * mileage + 0', resulting in a price of zero for any\n"
          "mileage. Therefore, it is highly recommended to train the model\n"
          "if this is your first use or if the underlying database has\n"
          "changed.\n\n"
          "When deciding to train the model, you will also be asked if\n"
          "you want to:\n"
          "    - Plot the data used for the estimation.\n"
          "    - Plot the calculated line defining the estimation on the\n"
          "      same graph.\n"
          "    - View a report on the accuracy of the algorithm using\n"
          "      various methods applied to linear regressions.\n\n")
    mileage = enter_mileage()
    theta0 = 0.0
    theta1 = 0.0
    train_model()


if __name__ == "__main__":
    predict_price()
