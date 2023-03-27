import re

NON_DECLARATIVE_SENTENCE_ENDINGS = ('!', '?')

SPLIT_INTO_SENTENCES_PATTERN = re.compile(
    r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<![A-Z]rs\.)(?<=\.|\?|!)(?<![A-Z]\.)\s(?![a-z])')

FIND_ALL_WORDS_PATTERN = re.compile(
    r'(?:\d*[@_a-zA-Z]+[_\d@a-zA-Z-]*\d*)+')

INVALID_INPUT_PATTERN = re.compile(r'[^A-Za-z\d_;:—\.,!\?\'\-\"\s@]')
