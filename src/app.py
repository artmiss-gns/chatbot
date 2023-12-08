import streamlit as st
from src.model_interaction import call_model



col1, col2, col3 = st.columns(3)
col2.title("🤖 Chat Bot")

# initialize messages in session_state
if "messages" not in st.session_state :
    st.session_state["messages"] = [
        {
            "role": "ai",
            "content": "Hello there. How can i help you"
        }
    ]

for msg in st.session_state["messages"] :
    with st.chat_message(msg["role"]) and st.spinner("loading..."):
        st.write(msg["content"])

if(prompt:= st.chat_input("...")) :
    with st.chat_message("human") :
        st.session_state["messages"].append({"role": "human", "content": prompt})
        st.write(prompt)

    with st.chat_message("ai") and st.spinner("loading..."):
        response = call_model(prompt)
        st.session_state["messages"].append({"role": "ai", "content": response["response"]})
        st.write(response["response"])