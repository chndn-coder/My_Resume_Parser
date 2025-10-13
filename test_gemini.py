import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    print("❌ Gemini API key not found! Please check your .env file.")
else:
    print("✅ Gemini API key loaded successfully!")

# Configure Gemini
genai.configure(api_key=api_key)

model = genai.GenerativeModel("models/gemini-2.5-pro")
response = model.generate_content("Hello Gemini! Please reply 'I am working fine'.")
print(response.text)

print("Available models for your API key:")
for model in genai.list_models():
    print("-", model.name)
