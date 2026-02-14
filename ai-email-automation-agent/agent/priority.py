HIGH_PRIORITY_KEYWORDS = [
    "urgent", "asap", "immediately", "right away",
    "not working", "down", "failed", "issue",
    "complaint", "deadline"
]

LOW_PRIORITY_KEYWORDS = [
    "newsletter", "update", "no rush", "whenever"
]


def detect_priority(text: str) -> str:
    text = text.lower()

    for word in HIGH_PRIORITY_KEYWORDS:
        if word in text:
            return "High"

    for word in LOW_PRIORITY_KEYWORDS:
        if word in text:
            return "Low"

    return "Medium"
