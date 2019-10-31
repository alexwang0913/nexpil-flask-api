from nltk.corpus import webtext
from nltk.collocations import BigramCollocationFinder
from nltk.metrics import BigramAssocMeasures
from nltk.stem import PorterStemmer
from nltk.corpus import wordnet
import itertools


pstem = PorterStemmer()
with open("dataset2.txt") as f:
    dataset = f.readlines()
with open("symptoms.txt") as f:
    symptoms = f.readlines()
# print(symptoms)
finalsyns=[]
for word in symptoms:
    syns = wordnet.synsets(word.strip())
    # print(syns)
    syns = [s.lemma_names() for s in syns ]
    merged = list(itertools.chain(*syns))
    if len(merged) == 0:
        finalsyns = finalsyns+[pstem.stem(word.strip())]
        print(finalsyns)
    else :
        finalsyns = finalsyns+merged


finalsyns = list(dict.fromkeys(finalsyns))
print(finalsyns)