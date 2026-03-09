from fastapi import FastAPI, Request
from botbuilder.core import BotFrameworkAdapter, BotFrameworkAdapterSettings, TurnContext
from botbuilder.schema import Activity
import os

app = FastAPI()

APP_ID = os.getenv("MicrosoftAppId", "")
APP_PASSWORD = os.getenv("MicrosoftAppPassword", "")

settings = BotFrameworkAdapterSettings(APP_ID, APP_PASSWORD)
adapter = BotFrameworkAdapter(adapter_settings)

@app.get("/")
async def root():
    return {"message": "AI Interview Bot Running"}

@app.post("/api/messages")
async def messages(req: Request):
    body = await req.json()
    activity = Activity().deserialize(body)

    async def turn_logic(turn_context: TurnContext):
        await turn_context.send_activity("Hello from AI Interview Bot")

    await adapter.process_activity(
        activity, "", turn_logic
    )

    return {"status": "ok"}
