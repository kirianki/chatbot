import nltk
#nltk.download('punkt')
import numpy as np
from nltk.stem.porter import PorterStemmer
stemmer = PorterStemmer()

def  tokenize(sentence):
    return nltk.word_tokenize(sentence)

def stem(word):
    return stemmer.stem(word.lower())

def bag_of_word(tokenized_sentence, all_words):
    tokenized_sentence = [stem(w) for w in tokenized_sentence]

    bag = np.zeros(len(all_words), dtype=np.float32)
    for index, w in  enumerate(all_words):
        if w in tokenized_sentence:
            bag[index] = 1
    
    return bag
