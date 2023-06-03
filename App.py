import openai
import os
from dotenv import load_dotenv
load_dotenv()




openai.api_key=os.environ["OPEN_AI_KEY"]

message=True

while message:
    user=input("input your query or Types exits")
    if user=='exit':
       message=False
    else:
        response=openai.Completion.create(engine='text-davinci-003',prompt=user,max_tokens=200)
        print(response['choices'][0]['text'])

