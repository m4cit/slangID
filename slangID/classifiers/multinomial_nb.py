from sklearn.naive_bayes import MultinomialNB
from .modifiers.splitting import train_y, test_x, test_y, vect_train_x, vect_test_x
from sklearn.metrics import f1_score
import pickle

# function to train the classifier
def train_nbm():
    clf_nbm = MultinomialNB(alpha=2.0, fit_prior=False)
    clf_nbm.fit(vect_train_x, train_y)
    # saving trained classifier
    with open('classifiers/models/multinomial_nb_classifier.pkl', 'wb') as f:
        pickle.dump(clf_nbm,f)
    print('Naive Bayes (Multinomial) trained...')

# function to predict the test set and list the sentences
def naive_m():
    # loading pre-trained classifier
    with open('classifiers/models/multinomial_nb_classifier.pkl', 'rb') as f:
        loaded_clf = pickle.load(f)
    print("\nNaive Bayes (Multinomial)\nTest Sentences: ")
    for i in range(len(test_x)):
        print("[" , i, "]", "pred:", loaded_clf.predict(vect_test_x[i]), "  ", test_x[i])
    def test_score():
        print("\nmean accuracy:      ", loaded_clf.score(vect_test_x, test_y))
    def f1():
        pred_y_nbm = loaded_clf.predict(vect_test_x)
        f1 = f1_score(test_y, pred_y_nbm,  average='macro', labels=['slang'])
        print("F1 score for slang: ", f1, "\n")
    test_score()
    f1()
