from rich.console import Console
from core.ui import table,summary
from core.scanner import scan
from core.logger import save
console=Console()
console.print("\n[bold cyan]🔍 LOGIN TRACE ENGINE ACTIVE[/bold cyan]\n")
email=input("📧 Target Email ➜ ")
t=table()
results,found,total=scan(email,t)
console.print(t)
summary(found,total)
file=save(email,results)
console.print(f"\n[bold green]✔ Scan Completed[/bold green]")
console.print(f"[bold cyan]📁 Report saved → {file}[/bold cyan]\n")
