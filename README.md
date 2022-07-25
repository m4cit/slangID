# Introducing slangID

In a nutshell: The slangID project tries to detect slang phrases / sentences.

 slangID consists of two programs:
  1. slangID_demo lets you train Machine Learning Models with a selection of classifiers, and prints out a test set of sentences with their predicted types (slang or normal).
  2. slangID_predict lets you train Machine Learning Models and lets you predict the type of your input sentence, with a selection of classifiers.

# Challenges

Due to a lack of data, the results, regardless of the classifier used, are not good enough.
 Certain bigram slang words like (a) **real one** are more difficult to resolve since the provided models do not take n-grams into consideration.

# How to Run slangID_demo and _predict

1. Install Python **3.9** or later (3.8 and 3.10 is probably fine too, I used 3.9.12)
2. Install the required packages by running **_pip install -r requirements.txt_** in your shell of choice. Make sure you are in the directory where the file is located.
3. In the project directory (or navigate there in the shell), open your shell and run **_python slangID_demo.py_** or **_slangID_predict.py_**.

# Source of the Data

Most of the hand-picked sentences come from archive.org's [Twitter Stream of June 6th](https://archive.org/details/archiveteam-twitter-stream-2021-06).

Some of the sentences come from me personally, which you might recognize due to their sad and depressing nature.
