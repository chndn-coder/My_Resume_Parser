import os
from dotenv import load_dotenv
import google.generativeai as genai

# Loading API key from .env
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("❌ GEMINI_API_KEY not found! Please check .env file.")
else:
    print("✅ GEMINI_API_KEY loaded successfully!")

# Configure Gemini
genai.configure(api_key=api_key)
model = genai.GenerativeModel("models/gemini-2.5-pro")

def analyze_resume_with_ai(resume_text: str) -> dict:
    """Analyze resume and return rating + suggestions"""
    prompt = f"""
You are a professional HR resume evaluator.
Analyze this resume and return results in **strict JSON** format:

{{
  "resume_rating": "<rating out of 10>",
  "improvement_areas": "<short summary, 3-4 lines>",
  "upskill_suggestions": "<short list of 3-5 skills to learn next>"
}}

Resume Text:
{resume_text}
"""


    try:
        response = model.generate_content(prompt)
        reply = response.text.strip() if hasattr(response, "text") else str(response)

        print("🔹 Gemini Response:", reply)

        
        rating = "N/A"
        if "Rating:" in reply:
            rating = reply.split("Rating:")[1].split("\n")[0].strip()

        return {
            "resume_rating": rating,
            "improvement_areas": reply,
            "upskill_suggestions": "See recommendations above."
        }

    except Exception as e:
        print("❌ AI Analysis Error:", e)
        return {
            "resume_rating": "N/A",
            "improvement_areas": "Could not analyze due to API error.",
            "upskill_suggestions": "N/A"
        }
