import os
import google.generativeai as genai

def review_devops(content: str) -> str:
    genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
    model = genai.GenerativeModel("gemini-1.5-flash")
    prompt = f"You are a DevOps expert. I am stuck with this error, I need your expertise to troubleshoot & resolve this error. Explain in very detail:\n\n{content}"
    response = model.generate_content(prompt)
    return response.text
    return response.choices[0].message.content

