import os
from openai import OpenAI
from dotenv import load_dotenv
from rich.console import Console
from rich.panel import Panel

load_dotenv()
console = Console()

client=OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"
)

MODES={
     "1": {
        "name": "翻译",
        "prompt": "你是一个专业翻译助手。用户输入什么，你就翻译成英文。只输出翻译结果，不要任何解释。"
    },
    "2": {
        "name": "摘要",
        "prompt": "你是一个摘要助手。用户给你一段文字，你用不超过3句话总结核心内容。"
    },
    "3": {
        "name": "代码解释",
        "prompt": "你是一个编程导师。用户给你一段代码，你用通俗易懂的语言解释它的作用。"
    },
    "4": {
        "name": "润色",
        "prompt": "你是一个文字润色助手。用户给你一段文字，你把它改写得更通顺、更专业。"
    },
    "5": {
        "name": "写作",
        "prompt": "你是一个文字作文助手，用户给你一个标题，你写一篇三百字左右的小作文"
    },
}

def ask_with_ai(imput_prompt):
    user_input = console.input(f"[red]用户：[/red]")
    messages = [{'role':'system','content':MODES[imput_prompt]['prompt']},
    {'role':'user','content':user_input}]
    response =client.chat.completions.create(model='deepseek-chat', messages=messages,stream=True)
    ai_reply=""
    for chunk in response:
        ai_reply +=chunk.choices[0].delta.content
        print(ai_reply,end="",flush=True)
    return ai_reply

if __name__ == '__main__':
    imput_prompt=input("请输入1-5之间的数字：")
    if imput_prompt in MODES:
        reply=ask_with_ai(imput_prompt)
        # console.print(reply)
    else:
        console.print("输入错误")