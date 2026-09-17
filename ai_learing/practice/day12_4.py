import os
from rich.console import Console
from rich.panel import Panel
from openai import OpenAI
from dotenv import load_dotenv
from rich.markdown import Markdown
from rich.live import Live

load_dotenv()
api_key = os.getenv("DEEPSEEK_API_KEY")
client = OpenAI(api_key=api_key,base_url='https://api.deepseek.com')
console = Console()

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

def stream_chat(client,messages):
    response = client.chat.completions.create(model="deepseek-chat", messages=messages,stream=True)
    full_rely = ""
    with Live(Markdown(full_rely),refresh_per_second=10)as live:
        for chunk in response:
            delta = chunk.choices[0].delta.content
            if delta:
                full_rely += delta
                live.update(Markdown(full_rely))
    return full_rely
        
    
def chat_loop(mode_key):
    mode = MODES[mode_key]
    messages = [{"role": "system", "content": mode["prompt"]}]

    console.print(Panel(
        f"已进入 [bold cyan]{mode['name']}[/bold cyan] 模式\n"
        f"输入 [yellow]exit[/yellow] 返回菜单 | [yellow]clear[/yellow] 清空历史",
        border_style="cyan"
    ))

    while True:
        user_input = console.input("\n[bold green]你：[/bold green]").strip()

        if user_input.lower() in ["exit", "quit"]:
            console.print("[dim]已退出当前模式[/dim]\n")
            break

        if user_input.lower() == "clear":
            messages = [{"role": "system", "content": mode["prompt"]}]
            console.print("[yellow]✨ 已清空对话历史[/yellow]\n")
            continue

        if not user_input:
            continue

        messages.append({"role": "user", "content": user_input})

        try:
            console.print("\n[bold blue]AI：[/bold blue]")
            reply = stream_chat(client, messages)
            messages.append({"role": "assistant", "content": reply})
            console.print()
        except Exception as e:
            console.print(f"[red]❌ 出错了：{e}[/red]\n")
            messages.pop()

if __name__ == "__main__":
    user_input = console.input("[red]输入模式：[/red]").strip()
    if user_input in MODES:
        chat_loop(user_input)
    else:
        console.print("[red]未知模式[/red]")