from wordfreq import zipf_frequency


class WordStats:
    def __init__(self, content, count, zipf_frequency):
        self.content = content
        self.count = count
        self.zipf_frequency = zipf_frequency


def count_word_counts(word_list):
    words_dict = {}
    for word in word_list:
        if word in words_dict:
            words_dict[word] += 1
        else:
            words_dict[word] = 1
    return words_dict


def add_zipf_frequency(word_count):
    words_stats = []

    for w, c in word_count.items():
        freq = zipf_frequency(w, "en")
        words_stats.append(WordStats(w, c, freq))

    return words_stats


def compute_score(word):
    return word.count / word.zipf_frequency 

def is_proper(word):

    # score = word.count / word.zipf_frequency 
    if word.zipf_frequency == 0 :
        print(word.content, "freq equals 0")
        return False
    return True
    # return word.zipf_frequency < 5.0 and word.count >= 2
