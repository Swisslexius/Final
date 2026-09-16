1. Create READMEmd file for taking notes

## SAVING CODE
1. On LHS of screen, go to "source control"
2. cloent to add files to the commit (i.e., stage changes)
3. Enter a commit message (anything)
4. click "commit"
5. click "sync changes"

## SETTING UP ENVIRONMENT (IN TERMINAL)

1. > python -m venv .venv
2. > source .venv/bin/activate
3. to install libraries / dependencies, first create a requirements.txt file
4. add openai, streamlit, python-dotenv, chromadb, pypdf to requirements.txt file
5. install dependencies by referring to requirements.txt file
> pip install -r requirements.txt
> pip freeze > requirements.txt
6. create a  .env file for API Key
7. ensure .env file is grayed out (git ignored) - if not edit .gitignore to include .env
8. Add secrets to .env
> OPENAI_API_KEY="<insert>"
> PASSWORD = ""

## CREATE SOME CODE
1. creat a pages folder
> mkdir pages
2. create a python file (call it wathever I like)
> touch <name>.py
3. run streamlit, reffering to the python file I created
> streamlit run home.py

## CREATE CODE IN YOUR PYTHON FILE

1. import streamlit
> import streamlit as st
2. import openai
> from openai import OpenAI
3. import python-dotenv
> from dotenv import load_dotenv
4. get all of the secret valus
> load_dotenv()
