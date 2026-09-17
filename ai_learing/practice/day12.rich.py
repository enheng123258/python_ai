from rich.panel import Panel
from rich.console import Console
from rich.text import Text
from rich.markdown import Markdown

console = Console()
# console.print(Panel("Hello, world!",title="标题",border_styled="cyan"))
console.print(Panel("你好，AI助手", title="欢迎", border_style="cyan"))

console.print("这是普通的文字")
console.print("[red]红色字体[/red]")
console.print("[bold red]红色粗体字体[/bold red]")
console.print("[red on black]红字蓝底[/red on black]")

md = Markdown("""
# 这是一个标题
这是**加粗**的文字
这是*斜体*的文字
这是~~删除线~~的文字
- 列表1
- 列表2
""")
console.print(md)