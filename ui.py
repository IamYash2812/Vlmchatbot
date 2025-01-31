import streamlit as st

from text_QndA import ask_question

def main():
    st.set_page_config(page_title="VLM Chat Bot", layout="wide")
    
    # Sidebar
    st.sidebar.title("VLM Chat Bot")
    option = st.sidebar.selectbox("Choose an option:", [
        "Chat with PDF",
        "Text Question Answer",
        "Image Question"
    ])
    
    st.title("Welcome to VLM Chat Bot")
    
    if option == "Chat with PDF":
        
        pass
        
    elif option == "Text Question Answer":
        st.subheader("Ask a text-based question")
        question = st.text_input("Enter your question:")
        if st.button("Ask") and question:
            response = ask_question(question)
            st.session_state['chat_history'] = [{"question": question, "response": response}] + st.session_state.get('chat_history', [])
        
        if "chat_history" not in st.session_state:
            st.session_state["chat_history"] = []
        
        

        # Display chat history
        for entry in st.session_state.get('chat_history', []):
            st.write(f"**You:** {entry['question']}")
            st.write(f"**VLMBOT:** {entry['response']}")
 
    
    
    elif option == "Image Question":
        st.subheader("Upload an image to ask a question about it")
        image_file = st.file_uploader("Upload an Image", type=["png", "jpg", "jpeg"])
        if image_file is not None:
            st.image(image_file, caption="Uploaded Image", use_column_width=True)
            question = st.text_input("Ask a question about this image:")
            if st.button("Ask"):
                st.write("Processing your image question...")
                # Implement image-based Q&A functionality here

if __name__ == "__main__":
    main()
