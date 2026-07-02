from collections import Counter
from pprint import pprint as pp


def word_counter(filename, stopwords="wordlist.txt"):
    stopwords_list = []

    with open(stopwords) as w:
        for line in w:
            stopwords_list.append(line.strip("\n"))

    with open(filename) as f:
        word_counts = Counter()
        for line in f.readlines():
            word_counts.update(
                word.strip(".,()")
                for word in line.lower().split()
                if word.strip("().,") not in stopwords_list
            )

    print(f"The most common words found in {filename} are:")
    pp(word_counts.most_common(30))


if __name__ == "__main__":
    word_counter()
