tp = ("Sergio", "Juan" ,"Diego", "Morty", "Sabrina","Oscar")
suma_tp = 0
for m in tp:
    if m == tp[0] or m == tp[3]:
        print(f"{m}\n")
    elif m == tp[len(tp)-1]:
        print(f"{m}\n")
