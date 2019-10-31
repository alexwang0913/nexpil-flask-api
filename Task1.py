from nltk.tokenize import regexp_tokenize
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from itertools import chain
from nltk.stem import RegexpStemmer as RegexpStemmer
from nltk.stem import PorterStemmer as PorterStemmer
from nltk.corpus import wordnet
import itertools



def get_prescription(text):

    pstem = PorterStemmer()
    with open("symptoms.txt") as f:
        symptoms = f.readlines()
    finalsyns=[]
    for word in symptoms:
        syns = wordnet.synsets(word.strip())
        syns = [s.lemma_names() for s in syns ]
        merged = list(itertools.chain(*syns))
        if len(merged) == 0:
            finalsyns = finalsyns+[pstem.stem(word.strip())]
            ##print(finalsyns)
        else :
            finalsyns = finalsyns+merged
    finalsyns = [f.replace('\n','') for f in finalsyns]
    finalsyns = list(dict.fromkeys(finalsyns))
    #print(finalsyns)
    pstem = PorterStemmer()
    rstem = RegexpStemmer('\(s\)')
    def words_in_string(word_list, a_string):
        return set(word_list).intersection(a_string)


    with open("Amount.txt") as f:
        Amount = f.readlines()

    Amount = [rstem.stem(x.strip()).split(' - ') for x in Amount]
    Amount = list(chain(*Amount))
    prescription_dataset = tuple(open("dataset2.txt", 'r'))

    with open("Frequency.txt") as f:
        frequency = f.readlines()
    frequency = [rstem.stem(x.strip()).split(' - ') for x in frequency]
    frequency = list(chain(*frequency))

    schedule={}
    with open("schedule.txt") as f:
        for line in f:
             #print(line.split(':'))
             s = line.split(':')
             schedule[s[0].strip().lower()] = s[1].strip()

    data = {}
    prescription = text.lower()
    prescription_tokenized = [word.replace(".","").replace("(","").replace(")","") for word in prescription.split()]
    prescription_tokenized_final = [pstem.stem(word) for word in prescription_tokenized ]
    print(prescription)
    data.update({'prescription': prescription})
    amount=""
    for word in Amount:
        if pstem.stem(word) in prescription_tokenized_final or rstem.stem(word) in prescription_tokenized:
            index = prescription_tokenized_final.index(pstem.stem(word))
            amount = prescription_tokenized[index-1]+" "+prescription_tokenized[index]

    if amount is "":
        print("Amount not mentioned!")
    else:
        print("Amount : " + amount)
    freq= ""
    timing = ""
    if "every" in prescription or "each" in prescription:
        if "every" in prescription:
            ei = prescription_tokenized.index("every")
            re="every"
        elif "each in prescription":
            ei = prescription_tokenized.index("each")
            re="each"
        st = ["minutes","minute","hours","hour","meal","day","days","morning","evening","afternoon"]
        for i in range(0,10):
            s=st[i]
            if s in prescription_tokenized:
                ti=prescription_tokenized.index(s)
                if ti-ei==2:
                    freq=re+" "+prescription_tokenized[ei+1]+" "+s
                elif ti-ei==1 and i>=7:
                    freq= re+" "+ s
    if schedule.get(freq.strip()) is not None:
        timing = schedule.get(freq.strip())

    for word in frequency:
        if word in prescription and word.strip() is not "":
            freq=freq + " "+ word
            if schedule.get(word.strip()) is not None:
                timing = schedule.get(word.strip())
    if freq is "":
        print("No Frequency mentioned!")

    symptoms =""
    for s in finalsyns:
        if s in prescription:
            symptoms+= " "+s

    _check = ["", None]        
    if freq in _check:
        return {'error':"No prescription found!"}         
    data.update({"Amount":amount,"Symptoms" :symptoms,"Frequency":freq,"Timings":timing})

    return data