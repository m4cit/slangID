import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import MultinomialNB   
import pickle

################ splitting the data #########################################################
data = pd.read_csv (r'modifiers/data/handpicked_data.csv')
train, test = train_test_split(data, test_size=.11, random_state=42, stratify=data['type'])
train_x = [x for x in train['sentence']]
train_y = [x for x in train['type']]
test_x = [x for x in test['sentence']]
test_y = [x for x in test['type']]

vectorizer = TfidfVectorizer()
vect_train_x = vectorizer.fit_transform(train_x)
vect_test_x = vectorizer.transform(test_x)

############## functions to train classifiers ################
def train_svm():
    clf_svm = svm.SVC(kernel='linear', C=16)
    clf_svm.fit(vect_train_x, train_y)
    # saving trained models
    with open('./models/linear_svm_classifier.pkl', 'wb') as f:
        pickle.dump(clf_svm,f)
    print('\nLinear SVM trained...')

def train_log():
    clf_log = LogisticRegression(C=32, fit_intercept=False, solver='newton-cg')
    clf_log.fit(vect_train_x, train_y)
    # saving trained models
    with open('./models/log_regression_classifier.pkl', 'wb') as f:
        pickle.dump(clf_log,f)
    print('Logistic Regression trained...\n')

def train_dt():
    clf_dt = DecisionTreeClassifier(criterion='log_loss', min_samples_split=10)
    clf_dt.fit(vect_train_x, train_y)
    # saving trained models
    with open('./models/decision_tree_classifier.pkl', 'wb') as f:
        pickle.dump(clf_dt,f)
    print('Decision Tree trained...')

def train_nbg():
    clf_nbg = GaussianNB()
    clf_nbg.fit(vect_train_x.toarray(), train_y)
    # saving trained models
    with open('./models/gaussian_nb_classifier.pkl', 'wb') as f:
        pickle.dump(clf_nbg,f)
    print('Naive Bayes (Gaussian) trained...')

def train_nbm():
    clf_nbm = MultinomialNB(alpha=2.0, fit_prior=False)
    clf_nbm.fit(vect_train_x, train_y)
    # saving trained models
    with open('./models/multinomial_nb_classifier.pkl', 'wb') as f:
        pickle.dump(clf_nbm,f)
    print('Naive Bayes (Multinomial) trained...')

####################################################################################

############# following functions to predict the input sentence, as well as print the mean accuracy of the classifier##############

def predictor_svm(input):
    # loading pre-trained classifier
    with open('./models/linear_svm_classifier.pkl','rb') as f:
        loaded_clf = pickle.load(f)
    print("\nLinear SVM:\nSentence: ",'[', input[0],']', " Prediction: ", loaded_clf.predict(vectorizer.transform(input))[0])
    def test_score():
        print("mean accuracy: ", loaded_clf.score(vect_test_x, test_y))
    test_score()


def predictor_log(input):
    # loading pre-trained classifier
    with open('./models/log_regression_classifier.pkl','rb') as f:
        loaded_clf = pickle.load(f)
    print("\nLogistic Regression:\nSentence: ",'[', input[0],']', " Prediction: ", loaded_clf.predict(vectorizer.transform(input))[0])
    def test_score():
        print("mean accuracy: ", loaded_clf.score(vect_test_x, test_y))
    test_score()


def predictor_dec(input):
    # loading pre-trained classifier
    with open('./models/decision_tree_classifier.pkl','rb') as f:
        loaded_clf = pickle.load(f)
    print("\nDecision Tree:\nSentence: ",'[', input[0],']', " Prediction: ", loaded_clf.predict(vectorizer.transform(input))[0])
    def test_score():
        print("mean accuracy: ", loaded_clf.score(vect_test_x, test_y))
    test_score()


def predictor_naive_g(input):
    # loading pre-trained classifier
    with open('./models/gaussian_nb_classifier.pkl','rb') as f:
        loaded_clf = pickle.load(f)
    print("\nNaive Bayes (Gaussian):\nSentence: ",'[', input[0],']', " Prediction: ", loaded_clf.predict(vectorizer.transform(input).toarray())[0])
    def test_score():
        print("mean accuracy: ", loaded_clf.score(vect_test_x.toarray(), test_y))
    test_score()


def predictor_naive_m(input):
    # loading pre-trained classifier
    with open('./models/multinomial_nb_classifier.pkl','rb') as f:
        loaded_clf = pickle.load(f)
    print("\nNaive Bayes (Multinomial):\nSentence: ",'[', input[0],']', " Prediction: ", loaded_clf.predict(vectorizer.transform(input))[0])
    def test_score():
        print("mean accuracy: ", loaded_clf.score(vect_test_x, test_y))
    test_score()
