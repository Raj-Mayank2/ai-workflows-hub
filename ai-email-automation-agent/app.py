import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"  # hide TF warnings

import streamlit as st
from agent.classifier import classify_email
from agent.priority import detect_priority
from agent.gemini_reply import generate_ai_reply

st.set_page_config(
    page_title="AI Email Automation Agent",
    layout="centered"
)

st.title("📧 AI Email Automation Agent")
st.subheader("Turn emails into actions, automatically.")

st.divider()

email_text = st.text_area(
    "Paste Email Content",
    height=220,
    placeholder="Paste the email you want the AI to analyze..."
)

analyze = st.button("Analyze Email")

if analyze:
    if not email_text.strip():
        st.warning("Please paste an email to analyze.")
    else:
        with st.spinner("Analyzing email and generating reply..."):
            category, method = classify_email(email_text)
            priority = detect_priority(email_text)

            try:
                reply = generate_ai_reply(email_text, category, priority)
            except Exception as e:
                st.error("Gemini failed to generate reply.")
                st.stop()

        st.success(f"Email analyzed using {method} logic")

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("### 📂 Category")
            st.info(category)

        with col2:
            st.markdown("### ⏱ Priority")
            if priority == "High":
                st.error("High")
            elif priority == "Medium":
                st.warning("Medium")
            else:
                st.success("Low")

        st.markdown("### ✉️ Drafted Reply (Editable)")
        st.text_area("", value=reply, height=170)
