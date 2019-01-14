#First foray into NLP via https://towardsdatascience.com/sentiment-analysis-with-python-part-1-5ce197074184
#Ari Klau - 1/13/19
import re

reviews_train = []

for line in open('/Users/Ari/Desktop/NLP/aclImdb/movie_data/full_train.txt', 'r'):
    reviews_train.append(line.strip())

reviews_test = []

for line in open('/Users/Ari/Desktop/NLP/aclImdb/movie_data/full_test.txt', 'r'):
    reviews_test.append(line.strip())

#Want text with no punctuation or html markups
#strip using these regexes
REPLACE_NO_SPACE = re.compile("(\.)|(\;)|(\:)|(\!)|(\')|(\?)|(\,)|(\")|(\()|(\))|(\[)|(\])")
REPLACE_WITH_SPACE = re.compile("(<br\s*/><br\s*/>)|(\-)|(\/)")

def preprocess_reviews(reviews):
    reviews = [REPLACE_NO_SPACE.sub("", line.lower()) for line in reviews]
    reviews = [REPLACE_WITH_SPACE.sub(" ", line) for line in reviews]

    return reviews

reviews_train_clean = preprocess_reviews(reviews_train)
reviews_test_clean = preprocess_reviews(reviews_test)