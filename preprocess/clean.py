import string
import re
import nltk # type: ignore
from nltk.corpus import stopwords # type: ignore

# variables
tagRegex = '<.*?>'
urlRegex = 'https?://\S+|www\.\S+'
punctuation = string.punctuation
stopwords = stopwords.words('english')
#print(stopwords)
chat_words = {"LMAO": "laughing my ass off", "AFAIK": "as far as i know", "":""}


# data cleaning functions
def lowering(text):
    return text.lower()


def removeHTMLTags(text):
    pattern = re.compile(tagRegex)
    return pattern.sub(r'', text)


def removeURLs(text):
    pattern = re.compile(urlRegex)
    return pattern.sub(r'', text)


# slow method
def removePuncSlow(text):
    for p in punctuation:
        text = text.replace(p,"")
    return text
# fast method
def removePuncFast(text):
    return text.translate(str.maketrans('','',punctuation))


def removeStopwords(text):
    new_text = []
    
    for word in text.split(" "):
        if word in stopwords:
            new_text.append('')
        else:
            new_text.append(word)
    x = new_text[:]
    new_text.clear()
    return " ".join(x)


def removeEmojis(text):
    emoji_pattern = re.compile("["
                           u"\U0001F600-\U0001F64F"  # emoticons
                           u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                           u"\U0001F680-\U0001F6FF"  # transport & map symbols
                           u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           u"\U00002702-\U000027B0"
                           u"\U000024C2-\U0001F251"
                           "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', text)


def removeChatWords(text):
    words = []
    for word in text.split(" "):
        if word.upper() in chat_words:
            words.append(chat_words[word.upper()])
        else:
            words.append(word)
    new_text = " ".join(words)
    return new_text

