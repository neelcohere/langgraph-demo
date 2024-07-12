# ../langgraph_demo/constants.py

import os

from dotenv import load_dotenv
load_dotenv()


class Constants:
    # API keys
    COHERE_API_KEY = os.getenv('COHERE_API_KEY')
    LANGCHAIN_API_KEY = os.getenv('LANGCHAIN_API_KEY')
    
    # langsmith
    LANGCHAIN_PROJECT = os.getenv('LANGCHAIN_PROJECT')

    # models
    CHAT_MODEL = "command-r-plus"
