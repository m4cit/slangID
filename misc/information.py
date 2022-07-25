def info():
    print('\n First, pass "train" to train the models, like this:\n',
    'python slangID_demo.py train\n\n Then choose a classifier by passing one of the following numbers like this:\n python slangID_demo.py number\n\n',
        '1 for Linear SVM\n 2 for Decision Tree\n 3 for Naive Bayes (Gaussian)\n 4 for Naive Bayes (Multinomial)\n 5 for Logistic Regression\n')

def info2():
    print(' You can also type -info to display your input options again.\n')

def in_opt():
    print('\n 1. "svm" for Linear SVM\n 2. "dec tree" for Decision Tree\n 3. "naive gauss" for Naive Bayes (Gaussian)\n 4. "naive multi" for Naive Bayes (Multinomial)\n 5. "log reg" for Logistic Regression\n')
