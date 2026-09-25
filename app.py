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
