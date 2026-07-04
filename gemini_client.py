import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv(override=True)
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def generate_report(data_summary: str) -> str:
    try:
        # --- DEBUG: Print available models to your terminal ---
        print("Checking available models...")
        for m in genai.list_models():
            if 'generateContent' in m.supported_generation_methods:
                print(f"AVAILABLE MODEL: {m.name}")
        # ------------------------------------------------------

        # Try using a different model name format
        # Some accounts require 'gemini-1.5-flash-latest' or just 'gemini-pro'
        model = genai.GenerativeModel('gemini-flash-latest') 
        
        response = model.generate_content(data_summary)
        return response.text
    except Exception as e:
        print(f"!!! GOOGLE API ERROR: {e}")
        return "The AI was unable to process this. Check terminal for error details."