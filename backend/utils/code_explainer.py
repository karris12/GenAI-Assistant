import os
import google.generativeai as genai

def explain_code(code: str) -> str:
    genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
    model = genai.GenerativeModel("gemini-1.5-flash")
    prompt = f"You are a DevOps Expert & I want You to Explain this code in detail with examples & real scenarios:\n\n{code}"
    response = model.generate_content(prompt)
    return response.text
