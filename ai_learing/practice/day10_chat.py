import os
from load_dotenv import load_dotenv 
from openai import OpenAI

load_dotenv()
client = OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"
)

def ask_withAi_continue(system_prompt):
    messages = [{'role':'system','content':system_prompt}]
    print('开启对话模式,输入exit退出')
    while True:
        user_input = input('用户：').strip()
        if user_input.lower() == 'exit':
            print('退出对话模式')
            break
        if not user_input:
            continue
        messages.append({'role':'user','content':user_input})
        response = client.chat.completions.create(model="deepseek-chat", messages=messages)
        ai_reply = response.choices[0].message.content
        messages.append({'role':'assistant','content':ai_reply})
        print(f"AI:{ai_reply}")

if __name__ =="__main__":
    ask_withAi_continue('你是一个专业翻译助手。用户输入什么，你就翻译成英文。只输出翻译结果。')
 