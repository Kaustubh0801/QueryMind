# QueryMind

QueryMind is an interactive AI-powered chatbot designed to extract information from PDFs and respond to user queries using Google's Gemini API.

## Features

- Upload multiple PDF documents
- Extract and process text from PDFs
- Utilize vector embeddings for efficient retrieval
- Engage in contextual conversations using an AI model
- User-friendly interface built with Streamlit

---

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/Kaustubh0801/QueryMind.git
cd QueryMind
```

### 2. Create a Virtual Environment (Recommended)
```bash
python -m venv venv
# Activate the virtual environment
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate     # On Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Set Up the Gemini API Key
- Obtain an API key from [Google AI Studio](https://aistudio.google.com)
- Create a `.env` file in the root directory and add:
  ```ini
  GEMINI_API_KEY=your_api_key_here
  ```

---

## Usage

### 1. Run the Application
```bash
streamlit run app.py
```

### 2. Upload PDFs
- Use the sidebar to upload one or multiple PDF files.
- Click on the "Process PDFs" button to extract text and store vector embeddings.

### 3. Ask Questions
- Type your question in the text box.
- QueryMind will retrieve relevant information from the processed documents and provide responses.

---

## Project Structure

```
QueryMind/
│── src/
│   ├── __init__.py
│   ├── helper.py          # Helper functions for PDF processing and AI retrieval
│── app.py                 # Streamlit app interface
│── requirements.txt        # Dependencies list
│── setup.py                # Installation setup
│── .gitignore              # Ignored files for Git
│── README.md               # Project documentation
│── LICENSE                 # License information
```

---

## Dependencies

The following dependencies are required for running QueryMind:

- `streamlit` (for UI)
- `PyMuPDF` (for PDF processing)
- `sentence-transformers` (for text embeddings)
- `google-generativeai` (for Gemini API integration)
- `python-dotenv` (for environment variable management)

To install all dependencies, run:
```bash
pip install -r requirements.txt
```

---


## License

This project is licensed under the MIT License.

---


