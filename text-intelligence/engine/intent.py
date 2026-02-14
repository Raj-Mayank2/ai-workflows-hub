from engine.similarity import similarity

INTENTS = {
    "Support": "User is facing a problem or issue",
    "Sales": "User wants pricing or product information",
    "Feedback": "User is giving feedback or opinion",
    "General": "General conversation or inquiry"
}


def detect_intent(text:str):
    scores={}

    for intent, desc in INTENTS.items():
        scores[intent]=similarity(text,desc)
    
    best_intent=max(scores, key=scores.get)
    return best_intent, round(scores[best_intent],3)