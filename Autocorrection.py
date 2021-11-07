import nltk

#nltk.download()
import pandas as pd
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

data = pd.read_csv('news_quiz_qa-dev.csv')
questions = data['question']
answers = data['answer']
#answers_arr = answers.to_numpy()
#ex_sentence = answers[0]
stop_words = set(stopwords.words("English"))

for i in range(len(answers)):
    sentence = word_tokenize(answers[i])
    filtered_sentence =[]
    for word in sentence:
        if word not in stop_words:
            filtered_sentence.append(word)
    print(filtered_sentence)