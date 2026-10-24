import json
from config import KEYS
import requests

# _gemini_client = genai.Client(api_key=KEYS["GEMINI_API_KEY"])
_OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"


def _openrouter_chat(model: str, prompt: str) -> str:
    response = requests.post(
        url=_OPENROUTER_URL,
        headers={
            "Authorization": f"Bearer {KEYS['OPENAI_API_KEY']}",
            "Content-Type": "application/json",
        },
        json={
            "model": model,
            "messages": [
                {"role": "system", "content": "Answer in no more than 150 words in English."},
                {"role": "user", "content": prompt},
            ],
        },
        timeout=120,
    )
    response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"]

# def generate_gemini_output(prompt: str) -> str:
#     """
#     Gemini Output Generator
#     """
#     response = _gemini_client.models.generate_content(
#         model="gemini-3-flash-preview",
#         contents=[prompt],
#         config=types.GenerateContentConfig(
#             system_instruction="Answer in no more than 150 words in English.",
#             temperature=0.8
#         )
#     )
#     return response.text

# def generate_gemini_output(prompt: str) -> str:
#     """
#     Gemini Output Generator
#     """
#     _model = genai.GenerativeModel(
#     model_name="gemini-3-flash-preview",
#     system_instruction="Answer in no more than 150 words in English."
#     )
#     response = _model.generate_content(
#         prompt,
#         generation_config={
#             "temperature": 0.8
#         }
#     )

#     return response.text

def generate_gemini_output(prompt: str) -> str:
    """
    Llama 4 Maverick Output Generator (keeps the legacy Model 1 function name).
    """
    return _openrouter_chat("meta-llama/llama-4-maverick-17b-128e-instruct", prompt)

def generate_gpt_output(prompt: str) -> str:
    """
    Qwen3.8-27B Output Generator (keeps the legacy Model 2 function name).
    """
    return _openrouter_chat("qwen/qwen3.8-27b", prompt)

def generate_deepseek_output(prompt: str) -> str:
    """
    DeepSeek Output Generator
    """
    response = requests.post(
    url=_OPENROUTER_URL,
    headers={
        "Authorization": f"Bearer {KEYS['OPENAI_API_KEY']}",
        "Content-Type": "application/json",
    },
    data=json.dumps({
            "model": "deepseek/deepseek-v3.2",
            "messages": [
                {
                    "role": "system",
                    "content": "Answer in no more than 150 words in English."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            "reasoning": {"enabled": True}
        })
    )
    response = response.json()
    response = response['choices'][0]['message']['content']
    return response


def generate_llama_output(prompt: str) -> str:
    """
    GPT-OSS-120B Output Generator
    """
    response = requests.post(
    url="https://openrouter.ai/api/v1/chat/completions",
    headers={
        "Authorization": f"Bearer {KEYS['OPENAI_API_KEY']}",
        "Content-Type": "application/json",
    },
    data=json.dumps({
        "model": "openai/gpt-oss-120b",
        "messages": [
                {
                    "role": "system",
                    "content": "Answer in no more than 150 words in English."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
        "reasoning": {"enabled": True}
    })
    )
    response = response.json()
    response = response['choices'][0]['message']['content']
    return response

