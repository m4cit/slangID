# Introducing slangID

In a nutshell: The slangID project tries to detect slang phrases / sentences. Something literally no one asked for...

 slangID consists of two programs:
 1. **slangID_demo.py** lets you train a selection of Machine Learning Models, and prints out a test set of sentences with their predicted types (slang or normal).
 2. **slangID_predict.py** lets you train a selection of Machine Learning Models and predict the type of your input.

# Challenges

Due to a lack of data, the results, regardless of the classifier used, are not good enough right now.
 Certain bigram slang words like (_a_) _**real one**_ are more difficult to resolve since the provided models do not take n-grams into consideration.

# How to run slangID_demo and slangID_predict

1. Install Python **3.9** or later (3.8 and 3.10 is probably fine too, I used 3.9.12).
2. Install the required packages by running **_pip install -r requirements.txt_** in your shell of choice. Make sure you are in the directory where the file is located.
3. In the project directory, open your shell (or navigate there in the shell) and run **_python slangID_demo.py_** or **_slangID_predict.py_**.
4. Follow the displayed instructions.

# What you will be greeted with when you run slangID_demo

![demo](https://user-images.githubusercontent.com/92433046/180863321-b8f6d0d7-f984-4388-abb6-105628510e60.png)


# What you will be greeted with when you run slangID_predict

![predict](https://user-images.githubusercontent.com/92433046/180862844-488c89da-0d0a-431f-b21b-00f4dcbb9fd2.png)


# Source of the data

Most of the hand-picked sentences come from archive.org's [Twitter Stream of June 6th](https://archive.org/details/archiveteam-twitter-stream-2021-06).

Some of the sentences / phrases come from me personally, which you might recognize due to their sad and depressing nature.


# Recognition of Open Source use

* scikit-learn
* pandas
