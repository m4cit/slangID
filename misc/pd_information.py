def info():
    print(' Please pass "train all" to train all the models, or "train number" to train a specific model, e.g.:\n ***************************************\n',
    'python slangID_predict.py "train all" *\n or                                    *\n python slangID_predict.py "train 1"   *\n',
    '***************************************\n\n',
    '1 for Linear SVM\n 2 for Decision Tree\n 3 for Naive Bayes (Gaussian)\n 4 for Naive Bayes (Multinomial)\n 5 for Logistic Regression\n 6 for all classifiers\n\n',
    'Then pick a classifier you want to use, and the sentence you want to evaluate, e.g.:\n',
    '**********************************************\n python slangID_predict.py 1 "I like turtles" *\n',
    '**********************************************\n')

def info2():
    print(' You can also type "info" to display your input options again.\n')

def in_opt():
    print('\n 1 for Linear SVM\n 2 for Decision Tree\n 3 for Naive Bayes (Gaussian)\n 4 for Naive Bayes (Multinomial)\n 5 for Logistic Regression\n 6 for all classifiers\n')
