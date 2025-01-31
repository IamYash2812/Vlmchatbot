
import streamlit as st
from llm_config import get_llm_model
from llm_config import get_output_parser
from llm_config import get_chat_prompt

def ask_question(input_text):
    #get LLAMA2 model
    llm = get_llm_model()

    #get prompt_template
    prompt_template = get_chat_prompt()

    #get ouput parser
    output_parser = get_output_parser()

    chain = prompt_template|llm|output_parser

    if input_text:
        response = chain.invoke({"question":input_text})
        return response

   