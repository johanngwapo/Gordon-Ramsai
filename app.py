import streamlit as st
from sidebar import sidebar
from ai import generate_response

st.set_page_config(page_title="Gordon RamsAi", page_icon="🥗")

st.title("🥗 Gordon RamsAi")

# Load sidebar
profile = sidebar()

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": (
                "Hi there! I'm Gordon RamsAi — your fitness & nutrition assistant. "
                "What can I help you with today? Feel free to ask about exercise plans or meal plans!"
            ),
        }
    ]

# Display chat
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
prompt = st.chat_input("Send a message...")

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate response
    with st.spinner("Thinking..."):
        try:
            response, usage = generate_response(st.session_state.messages, profile)
        except Exception as e:
            response = f"⚠️ Error generating response: {e}"
            usage = None

    st.session_state.messages.append({"role": "assistant", "content": response})

    with st.chat_message("assistant"):
        st.markdown(response)

