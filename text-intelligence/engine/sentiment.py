NEGATIVE_WORDS = ["bad", "worst", "issue", "problem", "hate", "angry"]
POSITIVE_WORDS = ["good", "great", "love", "excellent", "happy"]

def detect_sentiment(text:str):
    text=text.lower()

    pos=sum(word in text for word in POSITIVE_WORDS)
    neg=sum(word in text for word in NEGATIVE_WORDS)

    if pos>neg:
        return "Positive"
    elif neg>pos:
        return "Negative"
    return "Neutral"