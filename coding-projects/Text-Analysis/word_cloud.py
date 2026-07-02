from matplotlib import pyplot as plt
from wordcloud import STOPWORDS, WordCloud


def word_cloud_generator(filename):
    with open(filename, "r") as text:
        text_string = " ".join(line for line in text)

    wordcloud = WordCloud(width=1200, height=800, stopwords=STOPWORDS).generate(
        text_string
    )

    plt.imshow(wordcloud)
    plt.axis("off")
    plt.savefig(f"{filename[:-4]}_word_cloud.png", format="png")
