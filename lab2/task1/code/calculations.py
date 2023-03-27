from collections import Counter
from constants import SPLIT_INTO_SENTENCES_PATTERN, FIND_ALL_WORDS_PATTERN, NON_DECLARATIVE_SENTENCE_ENDINGS


def get_sentences(text):
    return list(filter(lambda sent: sent != '', SPLIT_INTO_SENTENCES_PATTERN.split(text)))


def get_amount_of_sentences(text):
    return len(get_sentences(text))


def get_amount_of_non_declarative_sentences(text):
    sentences = get_sentences(text)
    count = 0
    for s in sentences:
        if (s.endswith(NON_DECLARATIVE_SENTENCE_ENDINGS)):
            count += 1

    return count


def get_words(text):
    sentences = get_sentences(text)
    words = []
    for sent in sentences:
        words.extend(FIND_ALL_WORDS_PATTERN.findall(sent))

    return words


def get_average_length_of_sentence(text):
    num_of_sentences = len(get_sentences(text))
    if (num_of_sentences == 0):
        return 0
    words = get_words(text)
    total_length = 0
    for word in words:
        total_length += len(word)

    return round(total_length / num_of_sentences, 2)


def get_average_length_of_word(text):
    words = get_words(text)
    num_of_words = len(words)
    if (num_of_words == 0):
        return 0
    total_length = 0
    for word in words:
        total_length += len(word)

    return round(total_length / num_of_words, 2)


def get_top_K_repeated_N_grams(text, k=10, n=4):
    sentences = get_sentences(text)
    words_by_sentence = [FIND_ALL_WORDS_PATTERN.findall(
        sent) for sent in sentences]

    n_grams = []
    for words in words_by_sentence:
        n_grams.extend(list(zip(*[words[i:] for i in range(n)])))

    counter = Counter()

    for n_gram in n_grams:
        counter[' '.join(n_gram)] += 1

    return dict(counter.most_common(k))
