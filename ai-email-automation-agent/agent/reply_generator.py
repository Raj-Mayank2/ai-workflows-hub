def generate_reply(email_text: str, category: str, priority: str) -> str:
    email_preview = email_text.strip().split("\n")[0][:200]

    if category == "Support":
        if priority == "High":
            return (
                f"Thanks for reaching out regarding the issue you mentioned: "
                f"\"{email_preview}\".\n\n"
                "We understand the urgency and our team is actively looking into this. "
                "We’ll keep you updated as soon as we have progress."
            )
        else:
            return (
                f"Thanks for contacting support about: \"{email_preview}\".\n\n"
                "Our team has received your request and will assist you shortly."
            )

    if category == "Sales":
        return (
            f"Thanks for your interest.\n\n"
            f"We noted your query regarding: \"{email_preview}\".\n"
            "Our sales team will get back to you soon with the relevant details."
        )

    if category == "HR":
        return (
            f"Thank you for your email.\n\n"
            f"We have received your message regarding: \"{email_preview}\".\n"
            "Our hiring team will review it and reach out if there’s a match."
        )

    if category == "Spam":
        return (
            "Thank you for your message. This inbox is monitored for relevant inquiries only."
        )

    # General fallback
    return (
        f"Thank you for your email.\n\n"
        f"We have received your message regarding: \"{email_preview}\".\n"
        "We’ll respond with more details soon."
    )
