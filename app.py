import streamlit as st
from src.helper import get_pdf_text, get_text_chunks, get_vector_store, get_conversational_chain

# Set Page Configuration with a Dark Aesthetic Theme
st.set_page_config(page_title="QueryMind", layout="wide")

# Custom CSS for Better Readability and Visibility
st.markdown(
    """
    <style>
        /* Background & Text Colors */
        body {
            background-color: #222831;
            color: #EEEEEE;
        }
        .stApp {
            background-color: #222831;
        }
        
        /* Input Box Styling */
        .stTextInput>div>div>input {
            background-color: #4E4E50;
            color: #EEEEEE;
            font-size: 18px;
            font-weight: bold;
            border-radius: 10px;
            padding: 12px;
            border: 2px solid #4ECCA3;
            transition: 0.3s;
        }
        .stTextInput>div>div>input:focus {
            box-shadow: 0px 0px 12px rgba(78, 204, 163, 0.8);
            border: 2px solid #59DCA6;
        }

        /* Button Styling */
        .stButton>button {
            background-color: #4ECCA3;
            color: #222831;
            font-weight: bold;
            border-radius: 8px;
            padding: 12px 20px;
            border: none;
            transition: 0.3s ease-in-out;
        }
        .stButton>button:hover {
            background-color: #59DCA6;
        }

        /* Sidebar Styling */
        .stSidebar {
            background-color: #31363F;
            color: #EEEEEE;
        }

        /* Header */
        .stHeader {
            font-size: 32px;
            font-weight: bold;
            color: #4ECCA3;
            text-align: center;
        }

        /* Chat Bubble Styling */
        .chat-container {
            margin-top: 20px;
        }
        .chat-bubble {
            background-color: #393E46;
            color: #EEEEEE;
            padding: 12px 18px;
            border-radius: 10px;
            margin-bottom: 10px;
            font-size: 16px;
        }
        .user-message {
            border-left: 5px solid #4ECCA3;
        }
        .reply-message {
            border-left: 5px solid #FFA500;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Page Header
st.markdown("<h1 class='stHeader'>QueryMind</h1>", unsafe_allow_html=True)

# Function to Handle User Input
def user_input(user_question):
    response = st.session_state.conversation({'question': user_question})
    st.session_state.chatHistory = response['chat_history']
    
    st.markdown("<div class='chat-container'>", unsafe_allow_html=True)
    
    for i, message in enumerate(st.session_state.chatHistory):
        if i % 2 == 0:
            st.markdown(f"<div class='chat-bubble user-message'><strong>User:</strong> {message.content}</div>", unsafe_allow_html=True)
        else:
            st.markdown(f"<div class='chat-bubble reply-message'><strong>Reply:</strong> {message.content}</div>", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

# Sidebar for PDF Upload
with st.sidebar:
    st.subheader("Upload Your PDF")
    pdf_docs = st.file_uploader("Upload PDF Files", accept_multiple_files=True)
    if st.button("Process PDFs"):
        with st.spinner("Processing..."):
            raw_text = get_pdf_text(pdf_docs)
            text_chunks = get_text_chunks(raw_text)
            vector_store = get_vector_store(text_chunks)
            st.session_state.conversation = get_conversational_chain(vector_store)
            st.success("Done!")

# Initialize Chat Session
if "conversation" not in st.session_state:
    st.session_state.conversation = None
if "chatHistory" not in st.session_state:
    st.session_state.chatHistory = None

# User Query Input
user_question = st.text_input("Enter Your Question:")
if user_question:
    user_input(user_question)
