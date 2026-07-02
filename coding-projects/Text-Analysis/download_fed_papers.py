import requests
from bs4 import BeautifulSoup

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

    with open("federalist_papers_test.txt", "a") as f:
        for paper in soup.find_all("div", class_="s-lib-box s-lib-box-std"):
            title = paper.h2.text
            if title != "Table of Contents ":
                f.write(title)
                for para in paper.find_all("p"):
                    f.write(para.text + "\n\n")
                f.write("-" * len(title) + "\n\n")
