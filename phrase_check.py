import spacy

nlp = spacy.load("ru_core_news_sm")

text = """Капитальный ремонт автомобильной дороги Р-215 Астрахань - Кочубей - Кизляр - Махачкала, подъезд к г. Грозный на участке км 70+127 – км 85+267, Чеченская Республика"""

def check_phrase(phrase):
    doc = nlp(phrase)
    for token in doc:
        print(token.text, token.lemma_, token.pos_, token.dep_)

if __name__ == '__main__':
    check_phrase(text)