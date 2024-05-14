from bs4 import BeautifulSoup
from tqdm import tqdm

for i in tqdm(range(1, 261)):
    file = f"Task 2\sources\{i}.html"
    with open(file, "r", encoding="utf-8") as f:
        content = f.readlines()

    content = "".join(content)
    soup = BeautifulSoup(content, "html5lib")
    chapter = soup.find("div", attrs={"class": "chapter"})
    chapter_text = ''
    for verse in chapter.findAll(
        "span",
        attrs={
            "class": "align-left",
        },
    ):
        chapter_text += verse.text
    
    with open(f"Task 2/transcripts/{i}.txt", 'w', encoding="utf-8") as f:
        f.write(" ".join(chapter_text.split()))
