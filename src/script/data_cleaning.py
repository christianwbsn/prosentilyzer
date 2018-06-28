import pandas as pd
import re

def remove_non_letter(review):
    return re.sub("[^a-zA-Z]"," ", review)

def transform_to_word_list(review):
    return remove_non_letter(review).lower().split()

def remove_stop_words(word_list):
    return [word for word in word_list if word not in stop_words]

if __name__ == "__main__":
    raw = pd.read_csv( "../../input/raw/lazada_review.csv", 
                        header=None, names = ['rating', 'review'])
    stop_words = pd.read_csv("../../input/raw/stopwords_ID.txt",
                        sep="\n", header=None).values.tolist()
    raw = raw.dropna(subset=['review'],how='all')
    raw = raw.drop_duplicates(subset=['review'])
    raw['review'] = raw['review'].apply(transform_to_word_list)
    raw['review'] = raw['review'].apply(remove_stop_words)
    raw = raw[raw['review'].map(len) > 0]
    raw['word_count'] = raw['review'].map(len)
    raw.to_csv("../../input/preprocessed/lazada_review_clean.csv", index=False)