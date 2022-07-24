def info():
    print('Please pass "train" first to train the models:\npredict_main.py train\nThen a number for whichever classifier you want to use, and the sentence you want to evaluate, like this:\npredict_main.py number "sentence"\n\n',
    '1 for Linear SVM\n 2 for Decision Tree\n 3 for Naive Bayes (Gaussian)\n 4 for Naive Bayes (Multinomial)\n 5 for Logistic Regression\n 6 for all classifiers\n')

def info2():
    print('You can also write -info to display your input options again.\n')

def in_opt():
    print('\n 1 for Linear SVM\n 2 for Decision Tree\n 3 for Naive Bayes (Gaussian)\n 4 for Naive Bayes (Multinomial)\n 5 for Logistic Regression\n 6 for all classifiers\n')
