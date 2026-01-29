from rich.progress import track
from config.platforms import PLATFORMS
def scan(email, table):
    results={}
    found=0
    for name in track(PLATFORMS,description="Tracing Digital Networks..."):
        ok=PLATFORMS[name](email)
        status="🟢 PRESENT" if ok else "⚫ NO TRACE"
        if ok: found+=1
        results[name]=status
        table.add_row(name,status)
    return results,found,len(PLATFORMS)
