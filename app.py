import streamlit as st
from src.helper import get_pdf_text, get_text_chunks, get_vector_store, get_conversational_chain

# Set Page Configuration
st.set_page_config(page_title="QueryMind", layout="wide")

# Custom CSS for Improved UI & Visibility
st.markdown(
    """
    <style>
        /* Background & Text Colors */
        body {
            background-color: #2A0E4F;
            color: #FFFFFF;
        }
        .stApp {
            background-color: #2A0E4F;
        }

        /* Input Box Styling */
        .stTextInput>div>div>input {
            background-color: #4A148C;
            color: #FFFFFF;
            font-size: 18px;
            font-weight: bold;
            border-radius: 12px;
            padding: 14px;
            border: 2px solid #BA68C8;
            transition: 0.3s;
        }
        .stTextInput>div>div>input:focus {
            box-shadow: 0px 0px 15px rgba(186, 104, 200, 0.8);
            border: 2px solid #D1C4E9;
        }

        /* Button Styling */
        .stButton>button {
            background-color: #BA68C8;
            color: #2A0E4F;
            font-weight: bold;
            border-radius: 10px;
            padding: 14px 22px;
            border: none;
            transition: 0.3s ease-in-out;
        }
        .stButton>button:hover {
            background-color: #D1C4E9;
            transform: scale(1.05);
        }

        /* Sidebar Styling */
        .stSidebar {
            background-color: #4A148C;
            color: #FFFFFF;
            padding: 20px;
            border-radius: 12px;
        }

        /* Header */
        .stHeader {
            font-size: 42px;
            font-weight: bold;
            color: #E1BEE7;
            text-align: center;
            margin-bottom: 10px;
        }

        /* Chat Bubble Styling */
        .chat-container {
            margin-top: 20px;
        }
        .chat-bubble {
            background-color: #6A1B9A;
            color: #FFFFFF;
            padding: 12px 18px;
            border-radius: 10px;
            margin-bottom: 10px;
            font-size: 16px;
            width: fit-content;
            max-width: 80%;
        }
        .user-message {
            border-left: 5px solid #D1C4E9;
            margin-left: auto;
            text-align: right;
            background-color: #8E24AA;
        }
        .reply-message {
            border-left: 5px solid #FFAB91;
            background-color: #6A1B9A;
        }

        /* Scrollable Chat History */
        .chat-history {
            max-height: 500px;
            overflow-y: auto;
            padding-right: 10px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Page Header
st.markdown(
    "<h1 class='stHeader' style='color: #E1BEE7; text-align: center;'>QueryMind</h1>",
    unsafe_allow_html=True
)

# Sidebar for PDF Upload
with st.sidebar:
    st.subheader("Upload Your PDF")
    pdf_docs = st.file_uploader("Upload PDF Files", accept_multiple_files=True)
    
    if st.button("Process PDFs"):
        if pdf_docs:
            with st.spinner("Processing PDFs... Please wait..."):
                raw_text = get_pdf_text(pdf_docs)
                text_chunks = get_text_chunks(raw_text)
                vector_store = get_vector_store(text_chunks)
                st.session_state.conversation = get_conversational_chain(vector_store)
                st.success("Processing Complete!")
        else:
            st.warning("Please upload at least one PDF.")

# Initialize Chat Session
if "conversation" not in st.session_state:
    st.session_state.conversation = None
if "chatHistory" not in st.session_state:
    st.session_state.chatHistory = []

# Function to Handle User Input
def user_input(user_question):
    if st.session_state.conversation:
        response = st.session_state.conversation({'question': user_question})
        st.session_state.chatHistory = response['chat_history']
    
    # Display Chat History
    st.markdown("<div class='chat-history'>", unsafe_allow_html=True)
    
    for i, message in enumerate(st.session_state.chatHistory):
        message_class = "user-message" if i % 2 == 0 else "reply-message"
        role = "<strong>User:</strong>" if i % 2 == 0 else "<strong>Reply:</strong>"
        st.markdown(
            f"<div class='chat-bubble {message_class}'>{role} {message.content}</div>",
            unsafe_allow_html=True
        )

    st.markdown("</div>", unsafe_allow_html=True)

# User Query Input
user_question = st.text_input("Enter Your Question:")
if user_question:
    user_input(user_question)
