from collections import Counter
from pprint import pprint as pp


def get_stopwords(stopwords="wordlist.txt"):
    with open(stopwords) as f:
        return [word.strip() for word in f.readlines()]


def word_counter(filename):
    stopwords = get_stopwords()

    with open(filename) as f:
        word_counts = Counter()
        for line in f.readlines():
            word_counts.update(
                word.strip(".,()")
                for word in line.lower().split()
                if word.strip("().,") not in stopwords
            )

    print(f"The most common words found in {filename} are:")
    pp(word_counts.most_common(30))


if __name__ == "__main__":
    word_counter()
