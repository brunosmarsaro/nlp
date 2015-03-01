import nltk
from nltk.stem.lancaster import LancasterStemmer
import string

'''
    This module contains methods to process words/text.
    So far, it is able to remove all kind of punctuations and stem all words given a sentence


    Example:
    text = text_process("This is an example")

    contact: brunosmarsaro@gmail.com
'''

class text_process:
    # Initialise class:
    def __init__(self, text):
        # Normalisation of the text
        self.text = text.lower()

    # Remove punctuation
    def remove_punctuation(self):
        # Create a set with all the possible punctuations in English 
        exclude = set(string.punctuation)
        # All characters of the string are compared to the set above
        # Then, they are joint together to reconstruct the string
        self.text = ''.join(ch for ch in self.text if ch not in exclude)

    # Lancaster Stemmer
    def stemmer(self):
        # Initialise the object of the Stemmer, which is restrained in the NLTK library
        # For more information, read the library's documentation.
        st = LancasterStemmer()
        words_list = []        
        for word in self.text.split():
            words_list.append(st.stem(word))
        
        self.text = ' '.join(words_list)

    # Remove Stopwords
    def remove_stopwords(self):
        # The variable below receives a complete list of all stopwords in English
        stopwords = nltk.corpus.stopwords.words('english')
        # Transform the current text into a list of words
        self.text = self.text.split()
        # All the words within the list that are within stopwords are removed
        self.text = [x for x in self.text if x not in stopwords]
        # The list of words is joint together to form the text again.
        self.text = ' '.join(self.text)

