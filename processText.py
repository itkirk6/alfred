from settings import number_words
import re

def processText(text):
    words = text.split()
    result_words = []
    for word in words:
        clean_word = re.sub(r'[^\w\s]', '', word).lower()
        if clean_word in number_words:
            result_words.append(str(number_words[clean_word]))
        else:
            result_words.append(word)
    return ' '.join(result_words)


