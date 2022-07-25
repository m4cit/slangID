# Introducing slangID

In a nutshell: The slangID project tries to detect slang phrases / sentences.

 slangID consists of two programs:
  1. slangID_demo lets you train Machine Learning Models with a selection of classifiers, and prints out a test set of sentences with their predicted types (slang or normal).
  2. slangID_predict lets you train Machine Learning Models and lets you predict the type of your input sentence, with a selection of classifiers.

# Challenges

Due to a lack of data, the results, regardless of the classifier used, are not good enough.
 Certain bigram slang words like "(a) real one" are more difficult to resolve since the provided models do not take n-grams into consideration.
 
# How to Run slangID_demo and _predict

1. Install Python 3.9 or later (3.8 and 3.10 is probably fine too, I used 3.9.12)
2. Install the required packages by running _pip install -r requirements.txt_ in your preferred shell. Make sure you are in the directory where the .txt file is located.

pip install pickle-mixin

pip install sklearn

pip install pandas

Python 3.9.12
