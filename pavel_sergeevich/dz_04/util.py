import os
import re

import spacy
from spacy.lang.ru import stop_words as stop_words


def sentence_tokenizer(txt: str) -> list:
    assert txt != "", "Input text is empty"

    txt = re.sub(r'[^а-яё.!?]', " ", txt.lower())
    txt = re.sub(r'\s+', " ", txt)
    txt = re.sub(r'\.\.\.', ".", txt)

    # split sentence
    sentence_list = re.split(r'[.!?]', txt)

    return sentence_list


def tokenizer(txt: str) -> tuple[str, list]:
    """
    Наивный токенизатор русскоязычного текста. Функция убирает из текста все небуквенные символы,
    меняет регистр на нижний, разделяет на слова
    :param txt: сырой русский текст
    :return: список токенов
    """
    assert txt != "", "Input text is empty"

    txt = re.sub(r'[^а-яё]', " ", txt.lower())
    txt = re.sub(r'\s+', " ", txt)

    # split words
    words_list = re.split(" ", txt)

    return txt, words_list


def load_fl(path: str) -> str:
    """
    Функция загрузки текста из файла. Файл должен быть в UTF-8 кодировке
    :param path: путь к файлу
    :return: текст
    """
    assert os.path.isfile(path), "File don't exist. Please, check path to file."

    with open(path, encoding="utf-8") as fl:
        txt = fl.read()

    return txt


def get_type_of_letter(txt: str) -> tuple[int, int]:
    """
    Функция подсчитывает количество гласных и согласных букв, использую встроенную функцию isalpha
    :param txt: текст
    :return: количество гласных и согласных букв
    """
    vowels = set("аеёиоуыэюя")
    # consonant = set("бвгджзйклмнпрстфхцчшщ")

    vowels_cnt = 0
    consonant_cnt = 0

    for lt in txt:
        if lt in vowels:
            vowels_cnt += 1
        elif lt.isalpha():
            consonant_cnt += 1

    return vowels_cnt, consonant_cnt


def spacy_processing(txt):
    nlp = spacy.load("ru_core_news_sm")

    # обрабатываем уже почищенный текст от знаков препинания и множественных пробелов, текст в нижнем регистре
    doc = nlp(txt)

    lemma_uniq = []
    lemma_uniq_without_sw = []
    for word in doc:
        if word.lemma_ not in stop_words.STOP_WORDS:
            lemma_uniq_without_sw.append(word.lemma_)
        lemma_uniq.append(word.lemma_)

    return lemma_uniq, lemma_uniq_without_sw


if __name__ == "__main__":
    txt_raw = load_fl("book.txt")
    print("Загрузка книги. Количество символов: " + str(len(txt_raw)))

    txt_clean, txt_tk = tokenizer(txt_raw)
    print("Количество токенов: " + str(len(txt_tk)))
    # print(txt_tk)

    txt_tk_set = set(txt_tk)
    print("Количество уникальных токенов (слов): " + str(len(txt_tk_set)))

    word = txt_tk[20]
    v_cnt, c_cnt = get_type_of_letter(word)
    print("Количество гластных букв в слове \"" + word + "\" " + str(v_cnt) + ", а согласных - " + str(c_cnt))

    general_v_cnt = 0
    general_c_cnt = 0
    for w in txt_tk:
        v_cnt, c_cnt = get_type_of_letter(w)
        general_v_cnt += v_cnt
        general_c_cnt += c_cnt
    print("Количество гластных букв всех токенов " + str(general_v_cnt) + ", а согласных - " + str(general_c_cnt))

    sentence = sentence_tokenizer(txt_raw)
    print("Количество предложений в тексте " + str(len(sentence)))

    print(spacy_processing(txt_clean))


