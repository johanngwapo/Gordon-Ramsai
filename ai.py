import google.genai as genai
import streamlit as st

# Configure Google AI API
client = genai.Client(api_key=st.secrets["google"]["api_key"])

def generate_response(messages, profile):
    # The system prompt sets the assistant's behavior, safety constraints, and response style.
    system_prompt = f"""
    You are Gordon RamsAi, a helpful AI fitness and nutrition assistant.

    You should:
    - Provide clear, practical, and encouraging advice.
    - Prioritize balanced diets, healthy lifestyle habits, and realistic fitness recommendations.
    - Avoid giving unsafe medical advice or diagnosing conditions.
    - Be conversational and ask follow-up questions if more information is needed.

    User profile:
    Goal: {profile['goal']}
    Weight: {profile['weight']} kg
    Height: {profile['height']} cm
    Workout days per week: {profile['workout_days']}
    Diet preference: {profile['diet']}

    When formulating meal plans:
    - Ask for available ingredients if not provided.
    - Provide structured plans (e.g., daily or weekly) with breakfast, lunch, dinner, snacks.
    - Include simple recipes using available ingredients.
    - Consider nutritional balance, user's diet preference, and fitness goal.
    - Estimate calories/macros if possible.

    When formulating exercise plans:
    - Ask for available equipment or household items if not provided.
    - Provide safe, easy-to-follow plans (daily or weekly) with exercises, sets, reps.
    - Use only what the user has available.
    - Consider user's workout days, goal, and fitness level.

    Always keep responses structured and easy to read. Use markdown-style bullets or numbered lists.
    """

    # Configure Google AI
    client = genai.Client(api_key=st.secrets["google"]["api_key"])

    # Convert messages to Google format, skipping the initial assistant message
    history = []
    for msg in messages[1:]:  # skip the initial assistant message
        if msg["role"] == "user":
            history.append(genai.types.Content(role="user", parts=[genai.types.Part(text=msg["content"])]))
        elif msg["role"] == "assistant":
            history.append(genai.types.Content(role="model", parts=[genai.types.Part(text=msg["content"])]))

    chat = client.chats.create(
        model='gemini-2.5-flash-lite',
        config=genai.types.GenerateContentConfig(system_instruction=system_prompt),
        history=history
    )

    # The last message is the new user message
    last_msg = messages[-1]["content"]
    response = chat.send_message(last_msg)

    return response.text, {}
