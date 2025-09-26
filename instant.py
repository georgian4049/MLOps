# from fastapi import FastAPI
# from fastapi.responses import HTMLResponse
# import google.generativeai as genai
# import os

# api_key = os.getenv("GOOGLE_API_KEY")
# genai.configure(api_key=api_key)

# # Check if the API key was configured
# try:
#     # Initialize the model
#     # Use 'gemini-1.5-flash' for the latest fast model or 'gemini-pro' for the standard one.
#     model = genai.GenerativeModel('gemini-2.5-flash')
# except Exception as e:
#     print(f"An error occurred: {e}")
#     print("\nPlease check the following:")
#     print("1. Is your API key correct and active?")
#     print("2. Is the model name ('gemini-1.5-flash') correct?")
#     print("3. Do you have a stable internet connection?")

# app = FastAPI()

# @app.get("/")
# def instant():
#     message = """Reply- Hi
#     """
#     messages = [{"role": "user", "content": message}]
#     # Generate content
#     response = model.generate_content("Explain how AI works in 5 lines")
    
#     # Print the response text
#     # print(response.text)
#     reply = response.text
    
#     # Return the response as HTML
#     html = (
#         f"<html><head><title> Live in an Instant! </title></head><body><p>{reply}</p></body></html>"
#     )
#     return HTMLResponse(content=html)


from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def instant():
    return "Live from production!"