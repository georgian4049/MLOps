from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from google import genai

client = genai.Client()

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def instant():
    message = """Reply- Hi
    """
    messages = [{"role": "user", "content": message}]
    response = client.model.generate_content(model = "gemini-2.5-flash",
                                             content=messages)
    reply = response.text
    html = (
        f"<html><head><title> Live in an Instant! </title></head><body><p>{reply}</p></body></html>"
    )
    return html

if __name__ == '__main__':
    app.run(debug=True)