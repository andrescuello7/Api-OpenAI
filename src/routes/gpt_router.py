import os

from src.models.gpt_model import MessageGPT
from fastapi import APIRouter
from openai import AzureOpenAI

router = APIRouter()

client = AzureOpenAI(
    azure_endpoint=os.environ.get('OPENAI_AZURE_URL'),
    api_key=os.environ.get('OPENAI_AZURE_KEY'),  
    api_version=os.environ.get('OPENAI_AZURE_MODEL')
)

@router.get('/')
def get_gpt_methods():
    response = { 'msg': 'Hello, world!' }
    return response

@router.post('/')
def post_gpt_methods(req: MessageGPT):

    response = client.chat.completions.create(
        model=os.environ.get('OPENAI_AZURE_VERSION'),
        messages=[{"role": "system", "content": req.message}]
    )
    # return response.choices[0].message.content
    return response