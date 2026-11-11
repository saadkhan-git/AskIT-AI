import streamlit as st
import ollama

st.set_page_config(
    page_title="AskIT AI",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 AskIT AI")
st.caption("Your Personal AI Assistant | Powered by Llama 3.2")

if "messages" not in st.session_state:
    st.session_state.messages = []

st.sidebar.title("⚙️ Settings")

model = st.sidebar.selectbox(
    "Choose AI Model",
    ["llama3.2:3b"]
)

st.sidebar.divider()

st.sidebar.write("*About Askit AI*")
st.sidebar.caption(
    "A personal AI assistant built using Python, Streamlit and Ollama."
)

if st.sidebar.button("🗑️ Clear Chat", use_container_width=True):
    st.session_state.messages = []
    st.rerun()


def generate_response(messages, model):

    stream = ollama.chat(
        model=model,
        messages=messages,
        stream=True
    )

    for chunk in stream:
        content = chunk["message"]["content"]

        if content:
            yield content


for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])


prompt = st.chat_input("Ask Unnamed anything...")

if prompt:

    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):

        try:

            with st.spinner("Unnamed is thinking..."):

                answer = st.write_stream(
                    generate_response(
                        st.session_state.messages,
                        model
                    )
                )

            st.session_state.messages.append({
                "role": "assistant",
                "content": answer
            })

        except Exception as e:

            st.error(f"Something went wrong: {e}")


st.divider()

st.caption("Askit AI © 2026 | Built with Saad Khan")