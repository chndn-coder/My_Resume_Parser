# 🧠 AI Resume Parser

Welcome to your smart, AI-powered resume analyzer!  
This project uses **FastAPI**, **PostgreSQL**, and **Gemini AI** to extract key details from PDF resumes and provide actionable improvement suggestions—making your job search smarter and easier.

---

## 🚀 What Can It Do?
- 📂 **Upload PDF Resumes:** Just drag and drop your resume—no hassle!
- 🧾 **Automatic Info Extraction:** Instantly grabs your **Name**, **Email**, **Phone**, and **Skills** from your resume.
- 🤖 **AI Review & Suggestions:** Get a professional rating and personalized improvement tips powered by Gemini AI.
- 🗃 **Database Storage:** Every uploaded resume is safely stored in a PostgreSQL database.
- 🌐 **Modern Web Interface:** Clean, simple, and easy to use—built with HTML, CSS, and JavaScript.

---

## 🖼️ Screenshots

Here’s how the AI Resume Parser looks in action:

![Resume Parser Screenshot](frontend/assets/screenshot.png)
<!-- Add more screenshots below if needed -->
<!-- ![Another Screenshot](frontend/assets/another_screenshot.png) -->

---

## 🏗️ Tech Stack at a Glance
- **Backend:** FastAPI, SQLAlchemy, PostgreSQL
- **AI Model:** Gemini 2.5 Pro (or Flash, depending on your API access)
- **Frontend:** HTML, CSS, JavaScript
- **Other Tools:** LangChain, dotenv, pdfminer.six

---

## ⚙️ Getting Started

### 1️⃣ Clone This Repo
```bash
git clone https://github.com/chndn-coder/My_Resume_Parser.git
cd My_Resume_Parser
```

### 2️⃣ Set Up Your Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate   # On Windows
```

### 3️⃣ Install All Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Add Your Environment Variables
Create a `.env` file in the project root with the following:
```
DATABASE_URL=postgresql://postgres:yourpassword@localhost/resume_db
GEMINI_API_KEY=My_gemini_api_key
```

### 5️⃣ Start the FastAPI Server
```bash
uvicorn app.main:app --reload
```

### 6️⃣ Open the Frontend
Just open `frontend/index.html` in your browser, or use a live server extension in VS Code for the best experience.

---

## 🖼️ Example Output

**Uploaded Resume Info:**
- **Name:** John Doe
- **Email:** john.doe@example.com
- **Phone:** +91-9876543210
- **Skills:** Python, Machine Learning, SQL

**AI Feedback:**
- **Rating:** 8.5 / 10
- **Improvement:** Add specific project metrics and certifications.
- **Suggested Skills:** Cloud Computing, Deep Learning

---

## 📁 Project Structure

```
My_Resume_Parser/
│
├── app/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── routes/
│   │   └── resume.py
│   └── utils/
│       ├── pdf_extractor.py
│       └── ai_analyzer.py
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│   └── assets/
│       └── screenshot.png
│
├── uploads/
├── .env
├── requirements.txt
└── README.md
```

---

## 👨‍💻 Author

**Chandan Kumar**  
📧 charankr143rk@gmail.com  
🔗 [GitHub](https://github.com/chndn-coder/My_Resume_Parser)

---

> Made with ❤️ to help you land your dream job!
