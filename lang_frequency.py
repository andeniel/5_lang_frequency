import argparse
import io
import re
from collections import Counter

LIMIT_WORDS = 10


def load_data(file_path):
    with io.open(file_path, "r", encoding="utf8") as data_file:
        return data_file.read()


def get_most_frequent_words(data_text):
    words = re.findall(r'\w+', data_text.lower())
    return Counter(words).most_common(LIMIT_WORDS)


if __name__ == '__main__':
    aparser = argparse.ArgumentParser()
    aparser.add_argument("-f", "--file", required=True, help="Filepath")
    args = aparser.parse_args()
    data_text = load_data(args.file)
    frequent_words = get_most_frequent_words(data_text)
    for word in frequent_words:
        print("{}\t{}".format(*word))
