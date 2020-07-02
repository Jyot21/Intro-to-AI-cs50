import nltk
import sys
import os
import string
import math

FILE_MATCHES = 1
SENTENCE_MATCHES = 1

#nltk.download('stopwords')
def main():

    # Check command-line arguments
    if len(sys.argv) != 2:
        sys.exit("Usage: python questions.py corpus")

    # Calculate IDF values across files
    files = load_files(sys.argv[1])
    file_words = {
        filename: tokenize(files[filename])
        for filename in files
    }
    file_idfs = compute_idfs(file_words)

    # Prompt user for query
    query = set(tokenize(input("Query: ")))

    # Determine top file matches according to TF-IDF
    filenames = top_files(query, file_words, file_idfs, n=FILE_MATCHES)

    # Extract sentences from top files
    sentences = dict()
    for filename in filenames:
        for passage in files[filename].split("\n"):
            for sentence in nltk.sent_tokenize(passage):
                tokens = tokenize(sentence)
                if tokens:
                    sentences[sentence] = tokens

    # Compute IDF values across sentences
    idfs = compute_idfs(sentences)

    # Determine top sentence matches
    matches = top_sentences(query, sentences, idfs, n=SENTENCE_MATCHES)
    for match in matches:
        print(match)


def load_files(directory):
    """
    Given a directory name, return a dictionary mapping the filename of each
    `.txt` file inside that directory to the file's contents as a string.
    """
    files = dict()
    for filename in os.listdir(directory):
        with open(os.path.join(directory, filename),encoding="utf8") as f:
            files[filename] = f.read()
            
    #print(files.keys())
    return files
    #raise NotImplementedError


def tokenize(document):
    """
    Given a document (represented as a string), return a list of all of the
    words in that document, in order.

    Process document by coverting all words to lowercase, and removing any
    punctuation or English stopwords.
    """
    contents = [
                word.lower() for word in
                nltk.word_tokenize(document)
                if word not in string.punctuation and word not in nltk.corpus.stopwords.words("english")
               ]
    return contents

    #raise NotImplementedError


def compute_idfs(documents):
    """
    Given a dictionary of `documents` that maps names of documents to a list
    of words, return a dictionary that maps words to their IDF values.

    Any word that appears in at least one of the documents should be in the
    resulting dictionary.
    """
    words = set()
    for filename in set(documents):
        words.update(documents[filename])
    
    #print("Calculating inverse document frequencies...")
    idfs = dict()
    for word in words:
        f = sum(word in documents[filename] for filename in documents)
        idf = math.log(len(documents) / f)
        idfs[word] = idf
    return idfs
    #raise NotImplementedError


def top_files(query, files, idfs, n):
    """
    Given a `query` (a set of words), `files` (a dictionary mapping names of
    files to a list of their words), and `idfs` (a dictionary mapping words
    to their IDF values), return a list of the filenames of the the `n` top
    files that match the query, ranked according to tf-idf.
    """
    
    
    tfidfs = dict()
    for filename in set(files):
        # Count frequencies
        frequencies = dict()
        for word in files[filename]:
            if word not in frequencies:
                frequencies[word] = 1
            else:
                frequencies[word] += 1
        #filesfreq[filename] = frequencies
        
        
        tfidfs[filename] = 0
        for word in query:
            if word in files[filename]:
                tf = frequencies[word]
                tfidfs[filename] +=  tf * idfs[word]
    #print(tfidfs)
            
    a = sorted(tfidfs, key=tfidfs.get,reverse = True)
    return a[:n]
    
    #raise NotImplementedError


def top_sentences(query, sentences, idfs, n):
    """
    Given a `query` (a set of words), `sentences` (a dictionary mapping
    sentences to a list of their words), and `idfs` (a dictionary mapping words
    to their IDF values), return a list of the `n` top sentences that match
    the query, ranked according to idf. If there are ties, preference should
    be given to sentences that have a higher query term density.
    """
    tfidfs = dict()
    for sentence in set(sentences):
        
        
        tfidfs[sentence] = 0
        for word in query:
            if word in sentences[sentence]:
                tfidfs[sentence] +=  idfs[word]
    #print(tfidfs)
    a = sorted(tfidfs, key=tfidfs.get,reverse = True)
    
    #check if two sentence have same tfidfs then we can print the sentence also 
    # code seems to be broken as the queries :
        #How do neurons connect in a neural network?
        #and how do neurons connect in a neural network?
        #both gives different ans. i don't know why ?
    #print(a[:10])
    for key in a[:n*5]:
        keys = set(tfidfs)
        keys.remove(key)
        for key2 in keys:
            if key != key2 and tfidfs[key] == tfidfs[key2] and tfidfs[key] != 0:
                #print(tfidfs[key],key)
                break
    
    
    return a[:n]
    
    
    
    #raise NotImplementedError


if __name__ == "__main__":
    main()
