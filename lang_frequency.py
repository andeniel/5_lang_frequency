import argparse
import io
import re
from collections import Counter

def load_data(file_path):    
    with io.open(file_path, "r", encoding="utf8") as data_file:
        return data_file.read()


def get_most_frequent_words(data_text):
    reg = re.compile(r'\W')
    words = list(map(lambda word: reg.sub('', word), data_text.split()))    
    clear_words = list(filter(lambda word: len(word) > 2, words))    
    count_words = Counter(clear_words)
    sorted_words = sorted(count_words.items(), key=lambda item:item[1], reverse=True)
    return sorted_words[:10]    


if __name__ == '__main__':
    aparser = argparse.ArgumentParser()
    aparser.add_argument("-f", "--file", required=True, help="Filepath")
    args = vars(aparser.parse_args())
    data_text = load_data(args['file'])    
    frequent_words = get_most_frequent_words(data_text)
    print("Часто используемые слова в тексте:")
    for item in frequent_words:
        print("{}\t{}".format(*item))        
