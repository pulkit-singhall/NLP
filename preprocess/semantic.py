from nltk.tokenize import word_tokenize # type: ignore
from nltk.stem.porter import PorterStemmer # type: ignore
from nltk.stem import WordNetLemmatizer # type: ignore


# pass a list of textual data 
# (text sentences in the form of list of string)
def tokenisation(reviews):
    tokens = []
    for rev in reviews:
        tokenRev = word_tokenize(rev)
        tokens.append(tokenRev)
    return tokens # 2D List


# stemming
def stemming(tokenList): # 1D List
    stemmer = PorterStemmer()
    stemTokens = []
    for tok in tokenList:
        stemmedToken = stemmer.stem(tok)
        stemTokens.append(stemmedToken)
    return stemTokens # 1D List


# Lemmatisation
def lemmatisation(tokenList): # 1D List
    lemmer = WordNetLemmatizer()
    lemmaTokens = []
    for tok in tokenList:
        lemmaToken = lemmer.lemmatize(tok,pos='v')
        lemmaTokens.append(lemmaToken)
    return lemmaTokens # 1D List

