# Version of OPENAI 1.7

import os
from openai import AzureOpenAI

client = AzureOpenAI(
  azure_endpoint=os.environ.get('OPENAI_AZURE_URL'),
  api_key=os.environ.get('OPENAI_AZURE_KEY'),  
  api_version=os.environ.get('OPENAI_AZURE_VERSION')
)

response = client.chat.completions.create(
    model=os.environ.get('OPENAI_AZURE_MODEL'),
    messages=[{ "role": "user", "content": "Hello world" }]
)
print(response)


# Version of OPENAI 0.28

# import os
# import openai

# openai.api_type = "azure"
# openai.api_base = os.environ.get('OPENAI_AZURE_URL')
# openai.api_key = os.environ.get('OPENAI_AZURE_KEY')
# openai.api_version = os.environ.get('OPENAI_AZURE_VERSION')
 
# response = openai.ChatCompletion.create(
#   engine=os.environ.get('OPENAI_AZURE_MODEL'),
#   messages=[{ "role": "user", "content": "Hello world" }]
#   temperature=0.7,
#   max_tokens=800,
#   top_p=0.95,
#   frequency_penalty=0,
#   presence_penalty=0,
#   stop=None
# )
# print(response)