import google.generativeai as genai

key = "AIzaSyAIpcvHiXoz_-BD9mwU5xD8am7mE6cDj2s"

genai.configure(api_key=key)
model=genai.GenerativeModel("gemini-2.5-flash")

while True:
    user = input("What you want to search or type to exit for close: ")
    if user.lower()=="exit":
        print("byy byy")
        break
    response = model.generate_content(user)
    print("BOT -",response.text)