import datetime
def save(email, results):
    ts = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    fname = f"reports/scan_{ts}.txt"
    with open(fname, "w") as f:
        f.write(f"LOGIN TRACE REPORT\nTarget : {email}\nTime : {ts}\n\n")
        for p,s in results.items():
            f.write(f"{p:<15} : {s}\n")
    return fname
