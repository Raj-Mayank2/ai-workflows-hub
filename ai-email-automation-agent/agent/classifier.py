from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from agent.utils import clean_text

# Load model once
model = SentenceTransformer("all-MiniLM-L6-v2")

CATEGORIES = {
    "Support": ["issue", "problem", "not working", "error", "bug", "help"],
    "Sales": ["pricing", "demo", "buy", "purchase", "quote", "subscription"],
    "HR": ["resume", "job", "interview", "career", "hiring"],
    "Spam": ["winner", "free money", "lottery", "click here"]
}

CATEGORY_DESCRIPTIONS = {
    "Support": "Customer facing a technical issue",
    "Sales": "Customer interested in buying or pricing",
    "HR": "Job application or hiring related email",
    "Spam": "Promotional or malicious email",
    "General": "General inquiry"
}


def rule_based_classification(text: str):
    for category, keywords in CATEGORIES.items():
        for kw in keywords:
            if kw in text:
                return category
    return None


def ai_based_classification(text: str):
    email_embedding = model.encode([text])
    labels = list(CATEGORY_DESCRIPTIONS.keys())
    label_embeddings = model.encode(list(CATEGORY_DESCRIPTIONS.values()))

    scores = cosine_similarity(email_embedding, label_embeddings)[0]
    return labels[scores.argmax()]


def classify_email(text: str):
    cleaned = clean_text(text)

    rule_result = rule_based_classification(cleaned)
    if rule_result:
        return rule_result, "Rule-based"

    return ai_based_classification(cleaned), "AI-based"
