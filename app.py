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

        WEBHOOK_URL = "https://hook.us2.make.com/3sxscrkuj7iqe130kua1t4fcclng6cgq"

        try:
            response = requests.post(
                WEBHOOK_URL,
                json={
                    "request": user_input,
                    "conversationID": "actionmate-user"
                },
                timeout=60
            )

            if response.status_code == 200:
                data = response.json()

                st.success("✓ Action Plan Generated")

                st.markdown("### Your Action Plan")
                st.write(data.get("response", "No response received."))

            else:
                st.error(
                    f"Make returned an error: {response.status_code}"
                )

        except Exception as e:
            st.error(f"Connection error: {e}")
