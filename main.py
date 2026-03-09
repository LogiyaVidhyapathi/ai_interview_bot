from fastapi import FastAPI, Request, Response
from botbuilder.core import BotFrameworkAdapter, BotFrameworkAdapterSettings, TurnContext
from botbuilder.schema import Activity
import os

app = FastAPI()

APP_ID = os.getenv("MicrosoftAppId")
APP_PASSWORD = os.getenv("MicrosoftAppPassword")
APP_TENANT = os.getenv("MicrosoftAppTenantId")

settings = BotFrameworkAdapterSettings(
    APP_ID, 
    APP_PASSWORD, 
    channel_auth_tenant=APP_TENANT
)
adapter = BotFrameworkAdapter(settings)

@app.get("/")
async def root():
    return {"message": "AI Interview Bot Running"}

@app.post("/api/messages")
async def messages(req: Request):
    body = await req.json()
    activity = Activity().deserialize(body)

    auth_header = req.headers.get("Authorization", "")

    async def turn_logic(turn_context: TurnContext):
        await turn_context.send_activity("Hello from AI Interview Bot")

    await adapter.process_activity(
        activity, auth_header, turn_logic
    )

    return Response(status_code=200)




