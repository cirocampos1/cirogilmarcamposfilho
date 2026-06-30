import asyncio
import os
import json
from app.core.llm.openai_client import OpenAIClient
from app.core.config import settings

async def test_openai_tools():
    print(f"Testando OpenAI com modelo: {settings.openai_model}...")
    
    client = OpenAIClient(
        api_key=settings.openai_api_key,
        model=settings.openai_model
    )
    
    messages = [
        {"role": "user", "content": "Como está o clima em São Paulo?"}
    ]
    
    tools = [
        {
            "type": "function",
            "function": {
                "name": "get_weather",
                "description": "Get the current weather in a given location",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "location": {
                            "type": "string",
                            "description": "The city and state, e.g. San Francisco, CA",
                        }
                    },
                    "required": ["location"],
                },
            },
        }
    ]
    
    print("\n1. Enviando pergunta inicial...")
    response = await client.chat_completion(messages=messages, tools=tools)
    
    if "error" in response:
        print(f"ERRO: {response['error']}")
        return

    choice = response["choices"][0]["message"]
    if "tool_calls" in choice:
        print("Sucedido! O modelo solicitou o uso de ferramenta:")
        for tool_call in choice["tool_calls"]:
            print(f"- Ferramenta: {tool_call['function']['name']}")
            print(f"- Argumentos: {tool_call['function']['arguments']}")
    else:
        print("O modelo não solicitou ferramentas. Resposta:")
        print(choice.get("content", ""))

if __name__ == "__main__":
    asyncio.run(test_openai_tools())
