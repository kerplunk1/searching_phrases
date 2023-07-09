from spacy.strings import StringStore

def get_hash(list_of_words):
    stringstore = StringStore(list_of_words)
    for word in list_of_words:
        print(f"{word} - {stringstore[word]}")

