from calculations import get_amount_of_sentences, get_top_K_repeated_N_grams, get_average_length_of_sentence, get_average_length_of_word, get_amount_of_non_declarative_sentences
from helper_functions import is_input_valid


def test_get_amount_of_sentences0():
    text = ''
    assert get_amount_of_sentences(text) == 0


def test_get_amount_of_sentences1():
    text = 'Hi, Mr.Name.'
    assert get_amount_of_sentences(text) == 1


def test_get_amount_of_sentences2():
    text = 'Hi, Mr. !?'
    assert get_amount_of_sentences(text) == 1


def test_get_amount_of_sentences3():
    text = 'Hi, Mr. Name! Assa; Mrs. Name.'
    assert get_amount_of_sentences(text) == 2


def test_get_amount_of_sentences4():
    text = 'Hi, Mr. Name! Daassd, Mrs. Name?!'
    assert get_amount_of_sentences(text) == 2


def test_get_amount_of_sentences5():
    text = 'Hi, Mr. Name! Lklkaad, Jan.'
    assert get_amount_of_sentences(text) == 2


def test_get_amount_of_sentences6():
    text = 'Hi, Mr. Name. See Jan. qwert.'
    assert get_amount_of_sentences(text) == 2


def test_get_amount_of_sentences7():
    text = 'Hi, J. R. R. Tolkien!'
    assert get_amount_of_sentences(text) == 1


def test_get_amount_of_sentences8():
    text = 'Hi, Tolkien J. R.!'
    assert get_amount_of_sentences(text) == 1


def test_get_amount_of_sentences9():
    text = 'Hello... Lololo!!'
    assert get_amount_of_sentences(text) == 2


def test_get_amount_of_sentences10():
    text = 'Hello Mr. Cos. Goodbuy!'
    assert get_amount_of_sentences(text) == 2


def test_get_amount_of_sentences11():
    text = 'Hi, Mr.Name.'
    assert get_amount_of_sentences(text) == 1


def test_get_amount_of_sentences12():
    text = 'Hello... lololo!!'
    assert get_amount_of_sentences(text) == 1


def test_get_amount_of_sentences13():
    text = 'At the monday he said, "...Qwe qwe qwe?! Hello, Mr. David!", qweq qwe qwe'
    assert get_amount_of_sentences(text) == 1


def test_get_amount_of_sentences14():
    text = 'Ph.D. john B.Sci.arg!'
    assert get_amount_of_sentences(text) == 1

# ————————————————————————————————————————————————————————————
# ————————————————————————————————————————————————————————————
# ————————————————————————————————————————————————————————————


def test_get_amount_of_non_declarative_sentences_0():
    text = ''
    assert get_amount_of_non_declarative_sentences(text) == 0


def test_get_amount_of_non_declarative_sentences_1():
    text = 'Hi, Mr. Tom. Goodbye, Mrs. Smith?!'
    assert get_amount_of_non_declarative_sentences(text) == 1


def test_get_amount_of_non_declarative_sentences_2():
    text = 'Hi, Mr. Tom. Goodbye, Mrs. Smith?! Blabla, "Qwe!"'
    assert get_amount_of_non_declarative_sentences(text) == 1


def test_get_amount_of_non_declarative_sentences_3():
    text = 'Hi, Mr. Tom. Goodbye, Mrs. Smith?!'
    assert get_amount_of_non_declarative_sentences(text) == 1


def test_get_amount_of_non_declarative_sentences_3():
    text = 'Hi, Mr. Tom. Goodbye, Mrs. Smith?! Some text... Some text!'
    assert get_amount_of_non_declarative_sentences(text) == 2


def test_get_amount_of_non_declarative_sentences_4():
    text = 'Some text; some text...'
    assert get_amount_of_non_declarative_sentences(text) == 0


def test_get_amount_of_non_declarative_sentences_5():
    text = 'Some text; some text... Some text!!!'
    assert get_amount_of_non_declarative_sentences(text) == 1

# ————————————————————————————————————————————————————————————
# ————————————————————————————————————————————————————————————
# ————————————————————————————————————————————————————————————


def test_get_average_length_of_sentence_1():
    text = ''
    assert get_average_length_of_sentence(text) == 0


def test_get_average_length_of_sentence_2():
    text = 'Hi, Mr. Tom. Goodbye, Mrs. Smith! How r u, J. R. R. Tolkien?!'
    chars = [2, 2, 3, 7, 3, 5, 3, 1, 1, 1, 1, 1, 7]
    expected = round(sum(chars)/3, 2)
    assert get_average_length_of_sentence(text) == expected


def test_get_average_length_of_sentence_3():
    text = 'Hi, Mr. Tom. Goodbye, Mrs. Smith! How r u, J. R. R. Tolkien?! Some text, "...Some text?!"'
    chars = [2, 2, 3, 7, 3, 5, 3, 1, 1, 1, 1, 1, 7, 4, 4, 4, 4]
    expected = round(sum(chars)/4, 2)
    assert get_average_length_of_sentence(text) == expected


def test_get_average_length_of_sentence_4():
    text = 'Hi, Mr. Tom. Goodbye, Mrs. Smith! How r u, J. R. R. Tolkien 123?!'
    chars = [2, 2, 3, 7, 3, 5, 3, 1, 1, 1, 1, 1, 7]
    expected = round(sum(chars)/3, 2)
    assert get_average_length_of_sentence(text) == expected


def test_get_average_length_of_sentence_5():
    text = '123 123 kolkol.'
    chars = [6]
    expected = round(sum(chars)/1, 2)
    assert get_average_length_of_sentence(text) == expected


# ————————————————————————————————————————————————————————————
# ————————————————————————————————————————————————————————————
# ————————————————————————————————————————————————————————————

def test_get_average_length_of_word_1():
    text = ''
    assert get_average_length_of_word(text) == 0


def test_get_average_length_of_word_2():
    text = 'Hi, Mr. Tom.'
    chars = [2, 2, 3]
    expected = round(sum(chars)/len(chars), 2)
    assert get_average_length_of_word(text) == expected


def test_get_average_length_of_word_3():
    text = 'Hi, Mr. Tom. Hi; Goodbye.'
    chars = [2, 2, 3, 2, 7]
    expected = round(sum(chars)/len(chars), 2)
    assert get_average_length_of_word(text) == expected


def test_get_average_length_of_word_4():
    text = 'Hi, Mr. Tom 123 A1.'
    chars = [2, 2, 3, 2]
    expected = round(sum(chars)/len(chars), 2)
    assert get_average_length_of_word(text) == expected


def test_get_average_length_of_word_5():
    text = "Hi, Mr. Tom. What u'll do?"
    chars = [2, 2, 3, 4, 1, 2, 2]
    expected = round(sum(chars)/len(chars), 2)
    assert get_average_length_of_word(text) == expected


def test_get_average_length_of_word_6():
    text = "Hi, Mr. Tom. What u'll do? I'm Ph.d! Some text e.g."
    chars = [2, 2, 3, 4, 1, 2, 2, 1, 1, 2, 1, 4, 4, 1, 1]
    expected = round(sum(chars)/len(chars), 2)
    assert get_average_length_of_word(text) == expected


def test_get_average_length_of_word_7():
    text = "Hi Mr.Name!"
    chars = [2, 2, 4]
    expected = round(sum(chars)/len(chars), 2)
    assert get_average_length_of_word(text) == expected


# ————————————————————————————————————————————————————————————
# ————————————————————————————————————————————————————————————
# ————————————————————————————————————————————————————————————


def test_get_top_K_repeated_N_grams_1():
    text = ''
    assert get_top_K_repeated_N_grams(text, 10, 2) == {}


def test_get_top_K_repeated_N_grams_2():
    text = 'Hi, Mr. Tom. Hi, Mr. 123 Tom.'
    expected = {'Hi Mr': 2, 'Mr Tom': 2}
    assert get_top_K_repeated_N_grams(text, 10, 2) == expected


def test_get_top_K_repeated_N_grams_3():
    text = 'Hi, Mr. Tom. Hi, Mr. Tom 123 123 123 123 123 123.'
    expected = {'Hi Mr': 2, 'Mr Tom': 2}
    assert get_top_K_repeated_N_grams(text, 10, 2) == expected


def test_get_top_K_repeated_N_grams_4():
    text = 'A1, A2, A3, A4, A5, A6, A7, A8, A9, A10, A11, A12'
    expected = {'A1 A2': 1, 'A2 A3': 1, 'A3 A4': 1, 'A4 A5': 1, 'A5 A6': 1,
                'A6 A7': 1, 'A7 A8': 1, 'A8 A9': 1, 'A9 A10': 1, 'A10 A11': 1}
    assert get_top_K_repeated_N_grams(text, 10, 2) == expected


def test_get_top_K_repeated_N_grams_5():
    text = 'Hi, Mr. Tom. Hi, Mr. Tom 123 123 123 123 123 123.'
    expected = {'Hi Mr Tom': 2}
    assert get_top_K_repeated_N_grams(text, 2, 3) == expected


# ————————————————————————————————————————————————————————————
# ————————————————————————————————————————————————————————————
# ————————————————————————————————————————————————————————————

def test_is_input_valid_0():
    text = "la la!!? isn't true good bla bla"
    expected = True
    assert is_input_valid(text) == expected


def test_is_input_valid_1():
    text = "la la!!? isn't привет good bla bla"
    expected = False
    assert is_input_valid(text) == expected


def test_is_input_valid_2():
    text = "привет"
    expected = False
    assert is_input_valid(text) == expected


def test_is_input_valid_3():
    text = ""
    expected = True
    assert is_input_valid(text) == expected


def test_is_input_valid_4():
    text = "аассс"
    expected = False
    assert is_input_valid(text) == expected
