import re
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import nltk

nltk.download("stopwords")
stop_words = set(map(lambda x: x.lower(), stopwords.words("english")))

nltk.download("wordnet")
lemmatizer = WordNetLemmatizer()


def cleanup(word_list):
    word_list = list(map(lambda w: w.lower(), word_list))

    word_list = list(filter(lambda w: w not in stop_words, word_list))
    word_list = list(filter(lambda w: len(w) > 2, word_list))

    before = word_list.copy()
    word_list = list(map(remove_tags, word_list))

    word_list = list(
        map(lambda w: re.sub("^[^a-zA-z]*|[^a-zA-Z]*$", "", w), word_list)
    )  # remove non letters from beginning and end

    word_list = list(map(remove_punctuation, word_list))
    word_list = list(map(lambda w: lemmatizer.lemmatize(w), word_list))

    for i in range(len(before)):
        print(before[i], " --> ", word_list[i])

    word_list = list(filter(lambda w: w not in stop_words, word_list))
    word_list = list(filter(lambda w: len(w) > 2, word_list))

    return word_list


chars_to_remove = ["?", ".", "!", ",", '"']


def remove_tags(w):
    return w.replace("<i>", "").replace("</i>", "")


def remove_punctuation(w):
    for char in chars_to_remove:
        w = w.replace(char, "")
    return w
