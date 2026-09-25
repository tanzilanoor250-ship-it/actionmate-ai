import streamlit as st
import requests

st.set_page_config(
    page_title="ActionMate AI",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 ActionMate AI")
st.subheader("Personal Goal & Action Planning Agent")

st.write(
    "Turn your goal or problem into a clear, practical action plan."
)

st.divider()

goal = st.text_area(
    "What do you need help planning?",
    placeholder="Example: I have a presentation on Friday and I haven't started yet.",
    height=150
)

details = st.text_area(
    "Additional details (optional)",
    placeholder="Add any useful details, such as tasks, chapters, or deadlines.",
    height=100
)

if st.button("✨ Generate My Action Plan", use_container_width=True):

    if not goal.strip():
        st.warning("Please enter a goal or problem first.")

    else:
        user_input = goal

        if details.strip():
            user_input += "\n\nAdditional details:\n" + details

        st.info("ActionMate AI is creating your plan...")

        # Your Make Webhook URL will be added here later
