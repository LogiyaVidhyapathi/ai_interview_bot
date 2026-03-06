from fastapi import FastAPI, Request
from botbuilder.core import BotFrameworkAdapter, BotFrameworkAdapterSettings, TurnContext
from botbuilder.schema import Activity
import os

app = FastAPI()

APP_ID = os.getenv("MicrosoftAppId", "")
APP_PASSWORD = os.getenv("MicrosoftAppPassword", "")

adapter_settings = BotFrameworkAdapterSettings(APP_ID, APP_PASSWORD)
adapter = BotFrameworkAdapter(adapter_settings)

async def on_message_activity(turn_context: TurnContext):
    await turn_context.send_activity("Hello from AI Interview Bot")

@app.get("/")
async def home():
    return {"message": "AI Interview Bot Running"}

@app.post("/api/messages")
async def messages(req: Request):
    body = await req.json()

    activity = Activity().deserialize(body)
    auth_header = req.headers.get("Authorization", "")

    response = await adapter.process_activity(
        activity, auth_header, on_message_activity
    )

    if response:
        return response.body

    return {"status": "ok"}
