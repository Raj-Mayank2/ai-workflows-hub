import google.generativeai as genai

# 🔴 PASTE YOUR GEMINI API KEY HERE
GEMINI_API_KEY = "AIzaSyA4Suo66Q3xSjscj8Mv_4ICmODujmwjmFw"

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("models/gemini-1.5-flash")


def generate_ai_reply(email_text: str, category: str, priority: str) -> str:
    prompt = f"""
You are a professional email assistant.

Read the email carefully and write a polite, helpful, human-like reply.

Email category: {category}
Priority: {priority}

Rules:
- Respond directly to the email content
- Do NOT mention AI or automation
- Match urgency based on priority
- Keep it concise and professional

Email:
\"\"\"
{email_text}
\"\"\"

Reply:
"""

    response = model.generate_content(prompt)
    return response.text.strip()
