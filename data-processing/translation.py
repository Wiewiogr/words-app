from PyDictionary import PyDictionary

dictionary = PyDictionary()


class Word:
    def __init__(self, content, meaning):
        self.content = content
        self.meaning = meaning


def get_meaning(word):
    result = dictionary.meaning(word)
    if result == None:
        return None

    if "Noun" in result.keys() and len(result["Noun"]) > 0:
        return result["Noun"][0]

    if "Verb" in result.keys() and len(result["Verb"]) > 0:
        return result["Verb"][0]

    if "Adjective" in result.keys() and len(result["Adjective"]) > 0:
        return result["Adjective"][0]

    if "Adverb" in result.keys() and len(result["Adverb"]) > 0:
        return result["Adverb"][0]

    return result


def to_word_with_meaning(word):
    meaning = get_meaning(word)
    return Word(word, meaning)
