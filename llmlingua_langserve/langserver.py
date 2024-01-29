#!/usr/bin/env python
import os

from fastapi import FastAPI
from langchain_core.runnables import RunnableLambda
from langserve import add_routes
from llmlingua import PromptCompressor

HOST = os.getenv("HOST", "localhost")
PORT = int(os.getenv("PORT", 8000))

app = FastAPI(
    title="LLMLingua Server",
    version="1.0",
)

prompt_compressor = PromptCompressor(device_map="cpu")

def wrap_compress_prompt(input_dict: dict) -> dict:
    """Wrap compress prompt for RunnableLambda."""
    return prompt_compressor.compress_prompt(**input_dict)

runnable = RunnableLambda(wrap_compress_prompt)

add_routes(
    app,
    runnable = RunnableLambda(wrap_compress_prompt),
    path="/llmlingua",
)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host=HOST, port=PORT)
