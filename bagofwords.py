import re 
from sklearn.feature_extraction.text import CountVectorizer 

#Removes all punctuation from text
def letters(text):
    return re.sub("[^a-zA-Z]", " ", text.get_text() ) 

#turns all text to lowercase and splits words into list 
def words(text): 
    return letters.lower().split()

vectorizer = CountVectorizer(analyzer = "word",   \
                           tokenizer = None,    \
                           preprocessor = None, \
                           stop_words = None,   \
                           max_features = 10000) 

#feature extraction + convert to array
def train_data_features(text): 
    return vectorizer.fit_transform(text).toarray()
  

