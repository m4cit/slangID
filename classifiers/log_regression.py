from sklearn.linear_model import LogisticRegression
from .modifiers.splitting import train_y, test_x, test_y, vect_train_x, vect_test_x
from sklearn.metrics import f1_score
import pickle

# function to train the classifier
def train_log():
    clf_log = LogisticRegression(C=32, fit_intercept=False, solver='newton-cg')
    clf_log.fit(vect_train_x, train_y)
    # saving trained classifier
    with open('classifiers/models/log_regression_classifier.pkl', 'wb') as f:
        pickle.dump(clf_log,f)
    print('\nLogistic Regression trained...\n')

# function to predict the test set and list the sentences, as well as the predictions
def log_reg():
    # loading pre-trained classifier
    with open('classifiers/models/log_regression_classifier.pkl', 'rb') as f:
        loaded_clf = pickle.load(f)
    print("\nLogistic Regression\nTest Sentences: ")
    for i in range(len(test_x)):
        print("[" , i, "]", "pred:", loaded_clf.predict(vect_test_x[i]), "  ", test_x[i])
    def test_score():
        print("\nmean accuracy:      ", loaded_clf.score(vect_test_x, test_y))
    def f1():
        pred_y_log = loaded_clf.predict(vect_test_x)
        f1 = f1_score(test_y, pred_y_log,  average='macro', labels=['slang'])
        print("F1 score for slang: ", f1, "\n")
    test_score()
    f1()
