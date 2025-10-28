# agent_server.py
import os
from fastapi import FastAPI
from google.adk.agents.llm_agent import Agent

# define your agent
root_agent = Agent(
    model='gemini-2.5-flash',
    name='root_agent',
    description='A helpful assistant for user questions.',
    instruction='Answer user questions to the best of your knowledge',
)

app = FastAPI()

@app.post("/run")
async def run_agent(payload: dict):
    # assume payload has e.g. { "input": "hello, how are you?" }
    result = await root_agent.execute({"input": payload.get("input")})
    return {"result": result}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("PORT", "8000")))
