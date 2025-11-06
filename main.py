from dotenv import load_dotenv
from crew import legal_assistant_crew
from fastapi import FastAPI, Request
import uvicorn
import os

load_dotenv()

app = FastAPI()

def run(user_input: str):
    result = legal_assistant_crew.kickoff(inputs={"user_input": user_input})
    return result

@app.get("/")
def health_check():
    return {"status": "ok"}

@app.post("/ask")
async def ask(request: Request):
    data = await request.json()
    user_input = data.get("user_input", "")
    result = run(user_input)
    return {"result": result}

# Command-line use: python main.py
if __name__ == "__main__":
    user_input = (
        "A man broke into my house at night while my family was sleeping. "
        "He stole jewelry and cash from our bedroom. When I confronted him, "
        "he threatened me with a knife and ran away. We reported it to the police, "
        "but I'm not sure which legal charges should be filed under IPC."
    )
    print(run(user_input))
