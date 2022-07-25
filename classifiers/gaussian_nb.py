from sklearn.naive_bayes import GaussianNB
from .modifiers.splitting import train_y, test_x, test_y, vect_train_x, vect_test_x
from sklearn.metrics import f1_score
import pickle

# function to train the classifier
def train_nbg():
    clf_nbg = GaussianNB()
    clf_nbg.fit(vect_train_x.toarray(), train_y)
    # saving trained classifier
    with open('classifiers/models/gaussian_nb_classifier.pkl', 'wb') as f:
        pickle.dump(clf_nbg,f)
    print('Naive Bayes (Gaussian) trained...')

# function to predict the test set and list the sentences
def naive_g():
    # loading pre-trained classifier
    with open('classifiers/models/gaussian_nb_classifier.pkl', 'rb') as f:
        loaded_clf = pickle.load(f)
    print("\nNaive Bayes (Gaussian)\nTest Sentences: ")
    for i in range(len(test_x)):
        print("[" , i, "]", "pred:", loaded_clf.predict(vect_test_x[i].toarray()), "  ", test_x[i])
    def test_score():
        print("\nmean accuracy:      ", loaded_clf.score(vect_test_x.toarray(), test_y))
    def f1():
        pred_y_nbg = loaded_clf.predict(vect_test_x.toarray())
        f1 = f1_score(test_y, pred_y_nbg,  average='macro', labels=['slang'])
        print("F1 score for slang: ", f1, "\n")
    test_score()
    f1()
