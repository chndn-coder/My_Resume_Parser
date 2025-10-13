import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.schema import HumanMessage

load_dotenv()


api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("❌ GEMINI_API_KEY not found! Please check your .env file.")
else:
    print("✅ GEMINI_API_KEY loaded successfully!")

llm = ChatGoogleGenerativeAI(model="gemini-2.5-pro", google_api_key=api_key)

def analyze_resume_with_ai(resume_text: str) -> dict:
    """Use Gemini to rate resume and suggest improvements"""
    prompt = f"""
    You are a professional resume reviewer.
    Analyze this resume text and provide:
    1. Resume rating out of 10.
    2. Key improvement suggestions.
    3. New skills or technologies the person should learn.

    Resume Text:
    {resume_text}
    """

    try:
        response = llm([HumanMessage(content=prompt)])
        reply = response.content or ""
        print("🔹 GEMINI REPLY:", reply)  # For debugging

        # Try to extract sections cleanly
        rating = "N/A"
        if "Rating:" in reply:
            rating = reply.split("Rating:")[1].split("\n")[0].strip()

        return {
            "resume_rating": rating,
            "improvement_areas": reply or "No response from Gemini.",
            "upskill_suggestions": "Check improvement areas above."
        }

    except Exception as e:
        print("AI Analysis Error:", e)
        return {
            "resume_rating": "N/A",
            "improvement_areas": "Could not analyze due to API error.",
            "upskill_suggestions": "N/A"
        }
