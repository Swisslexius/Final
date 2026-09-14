import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

# Store important variable in a session_state
if "name" not in st.session_state:
    st.session_state.name = ""

if "button_value" not in st.session_state:
    st.session_state.button_value = False

#Ask the user to enter their name.
st.session_state.name = st.text_input("What's your name?") 
st.session_state.button_value = st.button("Click Me")

if st.session_state.name != "" and st.session_state.button_value == True:
    st.write(f"Hello {st.session_state.name}")

    st.header("Part 4")
    client = OpenAI()
    response = client.responses.create(
        model="gpt-4o",
        input=f"Greet {st.session_state.name} and make them welcome.",
    )
    st.write(response.output_text)

if st.session_state.name != "" and st.session_state.button_value == True:
    st.write(f"Hello {st.session_state.name}")

    st.header("Part 4")
    client = OpenAI()
    response = client.responses.create(
        model="gpt-4o",
        input=f"Greet {st.session_state.name} and make them welcome.",
    )
    st.write(response.output_text)
    awjerqwekjhf