import os
import json
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("❌ GEMINI_API_KEY not found! Please check your .env file.")
else:
    print("✅ GEMINI_API_KEY loaded successfully!")

# Configure Gemini API
genai.configure(api_key=api_key)
model = genai.GenerativeModel("models/gemini-2.5-pro")

def analyze_resume_with_ai(resume_text: str) -> dict:
    """
    Analyze resume text using Gemini AI and return a structured JSON result.
    Returns:
        dict: {
            "resume_rating": str,
            "improvement_areas": str,
            "upskill_suggestions": list
        }
    """
    prompt = f"""
You are a professional HR resume evaluator.
Analyze this resume and respond ONLY in strict JSON format, without extra text.

Example format:
{{
  "resume_rating": "8.5 / 10",
  "improvement_areas": "Add project links, fix date inconsistencies, and improve bullet structure.",
  "upskill_suggestions": ["React", "Docker", "PostgreSQL", "PyTorch", "MLOps"]
}}

Now analyze the following resume text:
\"\"\"{resume_text}\"\"\"
"""

    try:
        response = model.generate_content(prompt)
        reply = response.text.strip() if hasattr(response, "text") else str(response)

        print("🔹 Gemini JSON Response:", reply)

        # Try parsing Gemini's JSON output
        try:
            parsed = json.loads(reply)
        except json.JSONDecodeError:
            print("⚠️ Gemini returned non-JSON text. Using fallback parsing.")
            parsed = {
                "resume_rating": "N/A",
                "improvement_areas": reply[:800],  # fallback to text
                "upskill_suggestions": ["See text above for suggestions."]
            }

        # Final structured response
        return {
            "resume_rating": parsed.get("resume_rating", "N/A"),
            "improvement_areas": parsed.get("improvement_areas", "No insights available."),
            "upskill_suggestions": parsed.get("upskill_suggestions", ["No suggestions available."])
        }

    except Exception as e:
        print("❌ AI Analysis Error:", e)
        return {
            "resume_rating": "N/A",
            "improvement_areas": "Could not analyze due to API error.",
            "upskill_suggestions": ["N/A"]
        }
