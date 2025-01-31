from langchain_core.output_parsers import StrOutputParser 



# Thired party integration using langchain_community 
from langchain_community.llms import Ollama

# # llm model
def get_llm_model():
    return Ollama(model="llama3.1:8b")

def get_output_parser():
    return StrOutputParser()



