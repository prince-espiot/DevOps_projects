# pip install spacy
# python -m spacy download en_core_web_sm

import spacy
from spacy import displacy
# Load English tokenizer, tagger, parser, NER and word vectors
nlp = spacy.load("en_core_web_sm")

# Process whole documents
text = ("Hello Antti, "
        "I had the pleasure of meeting you earlier this year at the job workshop and I was impressed with your "
        "company's "
        "profile and was sold on the idea of joining you once I am done with my studies. "
        "It's at this point that my interest in joining Trombia Technologies comes into play. With my educational "
        "background "
        "and experience, I believe I could contribute effectively to the growth and success of the company. "
        "I would greatly appreciate the opportunity to discuss potential job opportunities at Trombia Technologies. "
        "I am eager to contribute my knowledge and contribute to the development of cutting-edge technologies in the "
        "field. "
        "I look forward to the possibility of exploring how my qualifications and experience could benefit Trombia "
        "Technologies. best regards")
doc = nlp(text)

# Tokenization
tokens = [token.text for token in doc]
print("Tokens:", tokens)

# POS tagging
pos_tags = [(token.text, token.pos_) for token in doc]
print("POS tags:", pos_tags)

# Analyze syntax
print("Noun phrases:", [chunk.text for chunk in doc.noun_chunks])
print("Verbs:", [token.lemma_ for token in doc if token.pos_ == "VERB"])

# Find named entities, phrases and concepts
for entity in doc.ents:
    print(entity.text, entity.label_)

displacy.serve(doc, style="dep")