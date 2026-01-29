from rich.table import Table
from rich.panel import Panel
from rich.console import Console
from rich import box
console=Console()
def table():
    t=Table(title="📊 ACCOUNT PRESENCE MATRIX",box=box.DOUBLE_EDGE,show_lines=True)
    t.add_column("Platform",style="cyan")
    t.add_column("Status",justify="center")
    return t
def summary(found,total):
    txt=f"\nNetworks : {total}\nPresent  : {found}\nNo Trace : {total-found}\nRisk     : {'HIGH' if found>=2 else 'LOW'}\n"
    console.print(Panel(txt,title="🧠 FOOTPRINT ANALYSIS",style="bold green"))
