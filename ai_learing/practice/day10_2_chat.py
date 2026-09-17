import os
from load_dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv('DEEPSEEK_API_KEY'),
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

def cloop_with_ai(key):
    if key == "":
        return
    else:
        mode = MODES[key]
        message = [{"role":"system","content":mode['prompt']}]
        while True:
            user_input =input("输入：").strip()
            if user_input.lower() == "exit":
                break
            elif user_input == "":
                continue
            else:
                message.append({"role":"user","content":user_input})
                response = client.chat.completions.create(model="deepseek-chat",messages=message)
                print("AI：",response.choices[0].message.content)
                message.append({"role":"assistant","content":response.choices[0].message.content})
        
def main():
    print("输入自己需要的模式")
    for key,mode in MODES.items():
        print(f"存在的模式{mode},对应编号：{key}")
    user_input = input("请输入模式编号：")
    if user_input == "0":
     print("再见！")
     return
    elif user_input in MODES:
        cloop_with_ai(user_input)
    else:
        print("不存在的编号")

if __name__ == "__main__":
    main()