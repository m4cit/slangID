def info():
    print('\n Please pass "train all" to train all the models, or "train number" to train a specific model, e.g.:\n ************************************\n python slangID_demo.py "train all" *\n',
    'or                                 *\n python slangID_demo.py "train 1"   *\n',
    '************************************\n\n', '1 for Linear SVM\n 2 for Decision Tree\n 3 for Naive Bayes (Gaussian)\n 4 for Naive Bayes (Multinomial)\n 5 for Logistic Regression\n\n',
    'Then pick a classifier you want to use, e.g.:\n **************************\n python slangID_demo.py 1 *\n **************************\n')

def info2():
    print(' You can also type "info" to display your input options again.\n')

def in_opt():
    print('\n 1. "svm" for Linear SVM\n 2. "dec tree" for Decision Tree\n 3. "naive gauss" for Naive Bayes (Gaussian)\n 4. "naive multi" for Naive Bayes (Multinomial)\n 5. "log reg" for Logistic Regression\n')
