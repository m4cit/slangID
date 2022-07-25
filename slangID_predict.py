import sys
from ignore_predict import train_svm, predictor_svm
from ignore_predict import train_log, predictor_log
from ignore_predict import train_dt, predictor_dec
from ignore_predict import train_nbg, predictor_naive_g
from ignore_predict import train_nbm, predictor_naive_m
from misc.pd_information import info, info2, in_opt

try:
    opt = sys.argv[1] # classifiers
    input = [sys.argv[2]] # string to evaluate
except (IndexError, NameError, TypeError):
    print()
    info()
    info2()

try:
    if opt == "train all":
        train_svm()
        train_dt()
        train_nbg()
        train_nbm()
        train_log()
    elif opt == "train 1":
        train_svm()
    elif opt == "train 2":
        train_dt()
    elif opt == "train 3":
        train_nbg()
    elif opt == "train 4":
        train_nbm()
    elif opt == "train 5":
        train_log()
    elif opt == "1":
        predictor_svm(input)
    elif opt == "2":
        predictor_dec(input)
    elif opt == "3":
        predictor_naive_g(input)
    elif opt == "4":
        predictor_naive_m(input)
    elif opt == "5":
        predictor_log(input)
    elif opt == "6":
        predictor_svm(input)
        predictor_dec(input)
        predictor_naive_g(input)
        predictor_naive_m(input)
        predictor_log(input)
        print()
    elif opt == "info":
        in_opt()
except (IndexError, NameError, TypeError):
    pass
