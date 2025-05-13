Dock Ai

Dock Ai is a simple and effective web application that summarizes patient health records from PDF documents using Google's Gemini 2.0 Flash LLM.

🚀 Features :

📤 Upload patient records in PDF format

🔐 Secure Gemini API key entry

🤖 Auto-generates summaries (within ~1000 words)

🌐 Built with Streamlit for quick and interactive use

🛠️ Tech Stack

Python

Streamlit

Google Generative AI (via LangChain)

PyPDF2

python-dotenv

📦 Installation

Clone the Repository

      git clone https://github.com/your-username/dock-ai.git
      cd dock-ai

Install Dependencies

        pip install -r requirements.txt



Set Up Environment Variables

Create a .env file:

      GEMINI_API_KEY=your_google_gemini_api_key

  
🔑 Note: You’ll also enter the API key in the Streamlit sidebar when running the app.

🚀 Run the App

            streamlit run rag.py

Open your browser and navigate to http://localhost:8501/.

📋 How to Use

Enter your Gemini Pro API Key in the sidebar.

Upload a PDF patient health document.

Click Submit.

View the AI-generated summary of the document.

🔐 Security

Your API key is used only during the session.


It is not stored or logged anywhere.
