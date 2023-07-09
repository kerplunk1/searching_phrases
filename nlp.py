import spacy
from spacy.matcher import Matcher
from spacy import displacy
from spacy.tokens import Span

nlp = spacy.load("ru_core_news_sm")

def get_pattern_list(phrase):
    doc = nlp(phrase)
    pattern_list = []
    
    for index, token in enumerate(doc):
        pattern_list.append({"LOWER": {"FUZZY": token.text}})
    
    return pattern_list


def searching_phrase(phrase, text):
    matcher = Matcher(nlp.vocab)
    pattern = get_pattern_list(phrase)
    
    matcher.add("MATCH", [pattern])
    
    doc = nlp(text)
    matches = matcher(doc)
    
    return matches, doc 


def vizualize(phrase, text):
    matches, doc = searching_phrase(phrase, text)
    options = {"colors": {"full_match": "green", "non_identical_match": "red"}}
    start_end_list = []
    
    for match_id, start, end in matches:
        if doc[start: end].text == phrase:
            start_end_list.append(Span(doc, start, end, "full_match"))
        else:
            start_end_list.append(Span(doc, start, end, "non_identical_match"))
    
    doc.spans["sc"] = start_end_list
    
    html = displacy.render(doc, style="span", options=options)
    return html

