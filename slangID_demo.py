import sys
from misc.information import info, info2, in_opt
from classifiers.log_regression import log_reg, train_log
from classifiers.linear_svm import lin_svm, train_svm
from classifiers.decision_tree import dec_tree, train_dt
from classifiers.gaussian_nb import naive_g, train_nbg
from classifiers.multinomial_nb import naive_m, train_nbm

# Prints a message if no argument is passed
try:
    input = sys.argv[1]
except IndexError:
    print("\n No arguments passed!")

try:
# argument options and executions
    if input == "train all":
        train_svm()
        train_nbg()
        train_dt()
        train_nbm()
        train_log()
    elif input == "train 1":
        train_svm()
    elif input == "train 2":
        train_dt()
    elif input == "train 3":
        train_nbg()
    elif input == "train 4":
        train_nbm()
    elif input == "train 5":
        train_log()
    elif input == "1":
        lin_svm()
    elif input == "2":
        log_reg()
    elif input == "3":
        dec_tree()
    elif input == "4":
        naive_g()
    elif input == "5":
        naive_m()
    elif input == "info":
        in_opt()
    else:
        info()
        info2()
except FileNotFoundError:
    print('\nTrain the models first with "train"!\n')
