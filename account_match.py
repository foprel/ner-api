import csv
from fuzzywuzzy import fuzz
from nltk.tokenize import word_tokenize
import re
import nltk
nltk.download('punkt')


def get_accounts(filename):
    with open(filename, 'r', newline="", encoding="utf-8") as f:
        f_reader = csv.reader(f, delimiter=',', quotechar="\"")
        accounts = []
        for row in f_reader:
            # preprocess accounts here
            account_name = row[0]
            accounts.append([account_name])
    return accounts


def get_stopwords(filename, n=20):
    with open(filename, 'r', newline="", encoding="utf-8") as f:
        f_reader = csv.reader(f, delimiter=",", quotechar="\"")
        word_count = {}
        for row in f_reader:
            account_name = clean(row[0])
            tokens = word_tokenize(account_name)
            for token in tokens:
                if token not in word_count:
                    word_count[token] = 1
                elif token in word_count:
                    word_count[token] += 1
        stopwords_dict = {k: v for k, v in sorted(word_count.items(), key=lambda item: item[1], reverse=True)}
        stopwords = [keys for keys, _ in stopwords_dict.items()][:n]
    return stopwords


def clean(input_str):
    input_str = input_str.lower()
    output_str = re.sub(r"[^A-Za-z0-9\s]+", "", input_str)
    return output_str


def match(str2match, accounts, stopwords, u=95, keep_old_value=True):
    rank_list = []

    tokens = word_tokenize(clean(str2match))
    for idx1, token in enumerate(tokens):
        if token in stopwords:
            tokens[idx1] = ""
    tokens = [x for x in tokens if x]
    str2match_cleaned = " ".join(tokens)

    for account in accounts:
        account_name = word_tokenize(clean(account[0]))
        for idx2, token in enumerate(account_name):
            if token in stopwords:
                account_name[idx2] = ""
        account_name = [x for x in account_name if x]
        account_name = " ".join(account_name)

        token_sort_ratio = fuzz.token_sort_ratio(str2match_cleaned, account_name)
        rank_list.append([token_sort_ratio])

    score = max(rank_list)[0]

    if score >= u:
        best_match_index = rank_list.index(max(rank_list))
        best_match = accounts[best_match_index][0]
    else:
        if keep_old_value:
            best_match = str2match
        else:
            best_match = ""

    return best_match
