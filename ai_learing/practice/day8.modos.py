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

def ask_with_ai(mode_key,user_input):
    """
    根据指定模式调用AI模型进行对话

    Args:
        mode_key: 模式键，用于从MODES中获取对应的提示词
        user_input: 用户输入的问题或指令

    Returns:
        str: AI模型的回复内容
    """
    # 根据模式调用ai
    mode = MODES[mode_key]
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": mode["prompt"]},
            {"role": "user", "content": user_input}
        ],
        temperature=0.7,
    )
    return response.choices[0].message.content
if __name__ == '__main__':
   print("【作文解释】")
   content=input("请输入作文标题：")
   print(ask_with_ai("5", content))
   print()