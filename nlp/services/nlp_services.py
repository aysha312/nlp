from transformers import pipeline

sentiment_model = pipeline("sentiment-analysis")
ner = pipeline("ner", aggregation_strategy="simple")
classifier_model = pipeline("zero-shot-classification")


def analyze_sentiment(text: str):
    return sentiment_model(text)[0]

ner_model = pipeline(
    "ner",
    model="dslim/bert-base-NER",
    aggregation_strategy="simple"
)

def recognize_entities(text: str):
    results = ner_model(text)

    clean = []
    for r in results:
        clean.append({
            "entity": r.get("entity_group"),
            "word": r.get("word"),
            "score": float(r.get("score")),
        })

    return clean

def classify_text(text: str, labels=None):
    if labels is None:
        labels = ["technology", "education", "business", "health", "entertainment"]
    return classifier_model(text, candidate_labels=labels)