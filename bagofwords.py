import re 
from sklearn.feature_extraction.text import CountVectorizer 

def letters(text):
    return re.sub("[^a-zA-Z]", " ", text.get_text() ) 

def words(text): 
    return letters.lower().split()

vectorizer = CountVectorizer(analyzer = "word",   \
                           tokenizer = None,    \
                           preprocessor = None, \
                           stop_words = None,   \
                           max_features = 10000) 


def train_data_features(text): 
    return vectorizer.fit_transform(text).toarray()
  

