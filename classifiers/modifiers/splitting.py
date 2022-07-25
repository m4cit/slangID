from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

# loading data
data = pd.read_csv (r'classifiers/modifiers/data/handpicked_data.csv')

# splitting data into test and train data
train, test = train_test_split(data, test_size=.195, random_state=42, stratify=data['type'])

# categorization to identify and test
train_x = [x for x in train['sentence']] 
train_y = [x for x in train['type']]
test_x = [x for x in test['sentence']]
test_y = [x for x in test['type']]

vectorizer = TfidfVectorizer()
# fit transforming train_x
vect_train_x = vectorizer.fit_transform(train_x)
# transforming test_x
# no fitting because it's test data
vect_test_x = vectorizer.transform(test_x)
