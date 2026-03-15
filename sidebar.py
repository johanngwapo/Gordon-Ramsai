import streamlit as st

def sidebar():

    st.sidebar.title("🥗 Gordon RamsAi")

    st.sidebar.subheader("User Profile")

    goal = st.sidebar.selectbox(
        "Fitness Goal",
        ["Muscle Gain", "Fat Loss", "Maintenance"]
    )

    weight = st.sidebar.number_input("Weight (kg)", 40, 200)

    height = st.sidebar.number_input("Height (cm)", 140, 220)

    workout_days = st.sidebar.slider("Workout Days per Week", 1, 7)

    diet = st.sidebar.selectbox(
        "Diet Preference",
        ["High Protein", "Low Carb", "Vegetarian", "Balanced"]
    )

    st.sidebar.divider()

    st.sidebar.subheader("Chats")

    if st.sidebar.button("➕ New Chat"):
        st.session_state.messages = [
            {
                "role": "assistant",
                "content": (
                    "Hi there! I'm Gordon RamsAi — your fitness & nutrition assistant. "
                    "What can I help you with today? Feel free to ask about exercise plans or meal plans!"
                ),
            }
        ]

    return {
        "goal": goal,
        "weight": weight,
        "height": height,
        "workout_days": workout_days,
        "diet": diet
    }