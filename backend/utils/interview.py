import os
import google.generativeai as genai

def handle_interview(question: str) -> str:
    genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
    model = genai.GenerativeModel("gemini-1.5-flash")
    prompt = f"You are a DevOps technical interview bot. You are also a DevOps expert with DevOps Interview Knowledge. Answer this question clearly & in very detail with examples well elaborated:\n\n{question}"
    response = model.generate_content(prompt)
    return response.text
