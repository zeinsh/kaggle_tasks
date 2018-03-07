(Toxic Comment Classification Challenge)[https://www.kaggle.com/c/jigsaw-toxic-comment-classification-challenge/leaderboard]


# Model 1

Processed data 1

- Tokenization (TreeBankWordTockenizer)
- Stemmer for English Language (snowball)

Features (bag of words)

- TfidfVectorizer 
- unigram and bigram
- min df = 5
- max df = 0.5


Learning model 1.1 (score : 0.9746)

- Logistic regression


Learning model 1.2 

- LinearSVC (score : 0.9715)
 
--------------------------------------------

# Model 2  

(Use lemmatizer instead of stemmer - resulted in no significant difference)

Processed data 2

- Tokenization (TreeBankWordTockenizer)
- Lemmatization (WordNet)


Features (bag of words)

- TfidfVectorizer 
- unigram and bigram
- min df = 5
- max df = 0.5


Learning model 2.1 

- Logistic regression (score : 0.9744)


Learning model 2.2 

- LinearSVC (score :  0.9727)
 
--------------------------------------------