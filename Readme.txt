This readme describes the working of Task1.py

Dependencies : nltk, itertools, dataset files like symptoms, Amount, Frequency,etc from the drive

1. Parse the symptoms, amount, frequency files and stores them into list variables
    1.1 For amount files, store both short forms and full forms
    1.2 Stem/Lemmatize each word in those files

2. Parse the prescription
    2.1 Tokenize the prescription strings
    2.2 Use lemmatization to retain the core word e.g from sleeping to sleep
    2.3 Store the tokens in list

3. Check the intersection between Prescription token with Symptoms, amount, frequency tokens
    3.1 For amount of tablet and units get the words before amount quantity and unit itself . For 20 mg - extract position of mg
    and previous token 20 to get the extract amount
    3.2 For frequency and symptoms create just use the key word from intersection of frequency tokens and prescription
    3.3 Create separate case for keywords like every and each and detect their occurrence before intersection of frequency to
    avoid missing out on crucial cases like "every monday" and elongating the frequency file with redundant words  like "each monday"
    "each Tuesday", etc.