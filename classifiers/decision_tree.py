from sklearn.tree import DecisionTreeClassifier
from .modifiers.splitting import train_y, test_x, test_y, vect_train_x, vect_test_x
from sklearn.metrics import f1_score
import pickle

# function to train the classifier
def train_dt():
    clf_dt = DecisionTreeClassifier(criterion='log_loss', min_samples_split=10)
    clf_dt.fit(vect_train_x, train_y)
    # saving trained classifier
    with open('classifiers/models/decision_tree_classifier.pkl', 'wb') as f:
        pickle.dump(clf_dt,f)
    print('\nDecision Tree trained...\n')

# function to predict the test set and list the sentences
def dec_tree():
    # loading pre-trained classifier
    with open('classifiers/models/decision_tree_classifier.pkl', 'rb') as f:
        loaded_clf = pickle.load(f)
    print("\nDecision Tree\nTest Sentences: ")
    for i in range(len(test_x)):
        print("[" , i, "]", "pred:", loaded_clf.predict(vect_test_x[i]), "  ", test_x[i])
    def test_score():
        print("\nmean accuracy:      ", loaded_clf.score(vect_test_x, test_y))
    def f1():
        pred_y_dt = loaded_clf.predict(vect_test_x)
        f1 = f1_score(test_y, pred_y_dt,  average='macro', labels=['slang'])
        print("F1 score for slang: ", f1, "\n")
    test_score()
    f1()
