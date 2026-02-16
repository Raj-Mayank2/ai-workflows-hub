def is_low_quality(text: str) -> bool:
    if len(text) < 30:
        return True

    noise_ratio = sum(
        1 for c in text if not c.isalnum()
    ) / max(len(text), 1)

    return noise_ratio > 0.5
