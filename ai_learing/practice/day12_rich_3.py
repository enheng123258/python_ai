from rich.console import  Console
from rich.panel import Panel

console = Console()

MODES = {
    "1": {"name": "翻译"},
    "2": {"name": "摘要"},
}

def show_enu():
    lines=[]
    for key,node in MODES.items():
        lines.append(f"[cyan]{key}[/cyan].[green]{node['name']}[/green]")
    console.print(Panel("\n".join(lines), title="请选择助手模式",border_style="green",title_align="center"))

if __name__=="__main__":
    show_enu()
