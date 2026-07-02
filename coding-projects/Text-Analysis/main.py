from collections import Counter
from pprint import pprint as pp
from matplotlib import pyplot as plt
from wordcloud import STOPWORDS, WordCloud

import requests
from bs4 import BeautifulSoup

FED_PAPERS = "federalist_papers_test.txt"


def download_fed_papers():
    sources = [
        "https://guides.loc.gov/federalist-papers/text-1-10",
        "https://guides.loc.gov/federalist-papers/text-11-20",
        "https://guides.loc.gov/federalist-papers/text-21-30",
        "https://guides.loc.gov/federalist-papers/text-31-40",
        "https://guides.loc.gov/federalist-papers/text-41-50",
        "https://guides.loc.gov/federalist-papers/text-51-60",
        "https://guides.loc.gov/federalist-papers/text-61-70",
        "https://guides.loc.gov/federalist-papers/text-71-80",
        "https://guides.loc.gov/federalist-papers/text-81-85",
    ]

    for s in sources:
        source = requests.get(s).text

        soup = BeautifulSoup(source, "lxml")

        with open(FED_PAPERS, "a") as f:
            for paper in soup.find_all("div", class_="s-lib-box s-lib-box-std"):
                title = paper.h2.text
                if title != "Table of Contents ":
                    f.write(title)
                    for para in paper.find_all("p"):
                        f.write(para.text + "\n\n")
                    f.write("-" * len(title) + "\n\n")


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


def word_cloud_generator(filename):
    with open(filename, "r") as text:
        text_string = " ".join(line for line in text)

    wordcloud = WordCloud(width=1200, height=800, stopwords=STOPWORDS).generate(
        text_string
    )

    plt.imshow(wordcloud)
    plt.axis("off")
    plt.savefig(f"{filename[:-4]}_word_cloud.png", format="png")


if __name__ == "__main__":
    if not FED_PAPERS:
        download_fed_papers()
    word_counter("federalist_papers.txt")
    word_cloud_generator("federalist_papers.txt")
