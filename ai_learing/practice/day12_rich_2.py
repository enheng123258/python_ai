from rich.console import Console
from rich.panel import Panel
from rich.markdown import Markdown

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

def rich_menu():
    menu_text="\n".join([f"[cyan]{mode_id}[/cyan] [blue]{mode_info['name']}[/blue]" for mode_id, mode_info in MODES.items()])
    menu_text+="\n[red]退出程序[/red]"
    console.print(Panel(menu_text, title="请选择助手模式",border_style="green",title_align="center"))

if __name__ == "__main__":
    rich_menu() 