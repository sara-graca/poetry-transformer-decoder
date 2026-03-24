with open('victorian_poetry.txt', 'r', encoding='utf-8') as f:
    corpus = f.read()

books = corpus.split("*** END OF")
books = [b.split("*** START OF")[-1] for b in books]

cleaned_books = []
for book in books:
    lines = book.split("\n")
    cleaned = []
    for line in lines:
        if "[illustration" in line.lower():
            continue
        cleaned.append(line)
    cleaned_books.append("<book>\n" + "\n".join(cleaned) + "\n</book>")

result = "\n\n".join(cleaned_books)

with open('corpus.txt', 'w', encoding='utf-8') as f:
    f.write(result)