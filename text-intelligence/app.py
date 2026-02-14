import streamlit as st
from engine.intent import detect_intent
from engine.sentiment import detect_sentiment
from engine.similarity import similarity

st.set_page_config(page_title="LLM Text Intelligence Toolkit")

st.title("🧠 LLM Text Intelligence Toolkit")
st.subheader("Understand text meaning using embeddings")

st.divider()

text = st.text_area("Enter text", height=150)

compare_text = st.text_area(
    "Compare with another text (optional)",
    height=100
)

if st.button("Analyze"):
    if not text.strip():
        st.warning("Enter some text")
    else:
        intent, score = detect_intent(text)
        sentiment = detect_sentiment(text)

        st.markdown("### 🔍 Results")
        st.info(f"**Intent:** {intent} (confidence: {score})")
        st.info(f"**Sentiment:** {sentiment}")

        if compare_text.strip():
            sim = similarity(text, compare_text)
            st.markdown("### 🔗 Similarity")
            st.success(f"Similarity score: {round(sim, 3)}")
